"""
Data Access Set (DAS) — Oracle Fusion Cloud Security Layer
===========================================================

Prevents unauthorized data visibility by enforcing Ledger-level and
Balancing Segment Value (BSV) restrictions at the application layer.

Concept:
  A Data Access Set defines what Ledger and which BSVs (Company Codes)
  a user can access. This module implements two security enforcement
  strategies simultaneously:

  1. Memory-layer filtering (Pandas)   — for analytical/export workloads
  2. SQL predicate push-down (asyncpg) — for transactional queries

Inspired by Oracle Fusion Cloud's Data Access Set security model.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from enum import Enum

import pandas as pd
from pydantic import BaseModel, Field, field_validator


# =========================================================================
# Pydantic Schemas
# =========================================================================


class AccessLevel(str, Enum):
    """Oracle Fusion–equivalent: READ_WRITE allows modifications."""
    READ_WRITE = "READ_WRITE"
    READ_ONLY  = "READ_ONLY"


class DASRuleType(str, Enum):
    """
    FULL_LEDGER  → User sees every BSV in the Ledger (no BSV filter).
    PRIMARY_BSV  → User is restricted to a specific list of BSV values.
    """
    FULL_LEDGER  = "FULL_LEDGER"
    PRIMARY_BSV  = "PRIMARY_BSV"


class DASRule(BaseModel):
    """A single Data Access Set rule binding a Ledger to its BSV scope."""

    ledger_id: str = Field(..., description="Ledger identifier (e.g. 'US_PRIMARY')")
    rule_type: DASRuleType = Field(..., description="FULL_LEDGER or PRIMARY_BSV")
    allowed_bsvs: list[str] = Field(
        default_factory=list,
        description="Balancing Segment Values the user may see. "
                    "Empty list means FULL_LEDGER ignores this field.",
    )
    access_level: AccessLevel = Field(default=AccessLevel.READ_ONLY)

    @field_validator("allowed_bsvs", mode="before")
    @classmethod
    def _normalise_bsvs(cls, v: object) -> list[str]:
        if isinstance(v, list):
            return sorted(set(str(x) for x in v))
        return []


class DataAccessSetContext(BaseModel):
    """
    Complete security profile for one user session.

    Example::

        ctx = DataAccessSetContext(
            user_id="user-123",
            rules=[
                DASRule(ledger_id="US_PRIMARY", rule_type="FULL_LEDGER",
                        access_level=AccessLevel.READ_WRITE),
                DASRule(ledger_id="US_SECONDARY", rule_type="PRIMARY_BSV",
                        allowed_bsvs=["01", "03", "05"]),
            ],
        )
    """

    user_id: str
    rules: list[DASRule] = Field(default_factory=list)
    cache_key: str = Field(default="", init_var=False)

    def model_post_init(self, __context: object) -> None:
        object.__setattr__(
            self,
            "cache_key",
            _das_cache_key(self.user_id, self.rules),
        )


# =========================================================================
# Internal helpers
# =========================================================================


def _das_cache_key(user_id: str, rules: list[DASRule]) -> str:
    payload = {
        "u": user_id,
        "r": [
            {"l": r.ledger_id, "t": r.rule_type.value, "b": r.allowed_bsvs}
            for r in sorted(rules, key=lambda x: x.ledger_id)
        ],
    }
    digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()[:16]
    return f"das:v1:{digest}"


# =========================================================================
# 1. Memory-Layer Filtering (Pandas)
# =========================================================================


def filter_ledger_balances_df(
    df: pd.DataFrame,
    ctx: DataAccessSetContext,
    *,
    ledger_col: str = "ledger_id",
    bsv_col: str = "segment1",
) -> pd.DataFrame:
    """
    Slice a Pandas DataFrame containing GL Balances according to the user's
    Data Access Set rules.

    Args:
        df: DataFrame with at minimum ``ledger_col`` and ``bsv_col`` columns.
        ctx: Security context for the current user session.
        ledger_col: Column name for the Ledger ID.
        bsv_col: Column name for the Balancing Segment Value (Company Code).

    Returns:
        A **copy** of the DataFrame containing only rows the user is
        authorised to view.  No in-place mutation.

    Performance note:
        Uses boolean-mask chaining with ``isin`` so the operation is
        vectorised and does not iterate row-by-row.
    """
    if df.empty or not ctx.rules:
        return df.iloc[:0]

    masks: list[pd.Series] = []

    for rule in ctx.rules:
        ledger_mask = df[ledger_col] == rule.ledger_id

        if rule.rule_type == DASRuleType.FULL_LEDGER:
            masks.append(ledger_mask)
        else:
            bsv_mask = df[bsv_col].isin(rule.allowed_bsvs)
            masks.append(ledger_mask & bsv_mask)

    if not masks:
        return df.iloc[:0]

    combined = masks[0]
    for m in masks[1:]:
        combined = combined | m

    return df.loc[combined].copy()


# =========================================================================
# 2. SQL Predicate Push-Down (asyncpg / SQLAlchemy)
# =========================================================================


@dataclass(frozen=True, slots=True)
class DASSQLPredicate:
    """Safe, parameterised SQL fragment for use with asyncpg or SQLAlchemy."""

    clause: str
    params: dict[str, object]


def apply_das_sql_predicate(
    ctx: DataAccessSetContext,
    *,
    table_alias: str = "gl",
    ledger_col: str = "ledger_id",
    bsv_col: str = "segment1",
    param_prefix: str = "das",
) -> DASSQLPredicate:
    """
    Build a ``WHERE`` clause fragment that enforces DAS security at the
    database layer.

    The generated SQL uses indexed parameters (``:param_name``) compatible
    with both asyncpg's ``$n``-style and SQLAlchemy's named-parameter
    binding when the prefix is consistent.

    Args:
        ctx: User security context.
        table_alias: Table alias or schema-qualified table name.
        ledger_col: DB column for Ledger ID.
        bsv_col: DB column for Balancing Segment Value.

    Returns:
        A ``DASSQLPredicate`` whose ``.clause`` can be appended to a
        ``WHERE`` and whose ``.params`` should be unpacked into the
        execution context.

    Example::

        pred = apply_das_sql_predicate(ctx, table_alias="gl")
        query = f"SELECT * FROM gl_balances gl WHERE {pred.clause}"
        rows = await conn.fetch(query, **pred.params)
    """
    if not ctx.rules:
        return DASSQLPredicate(clause="FALSE", params={})

    groups: list[str] = []
    params: dict[str, object] = {}
    counter = 0

    for i, rule in enumerate(ctx.rules):
        counter += 1
        l_param = f"{param_prefix}_ledger_{counter}"
        params[l_param] = rule.ledger_id

        if rule.rule_type == DASRuleType.FULL_LEDGER:
            groups.append(
                f"({table_alias}.{ledger_col} = :{l_param})"
            )
        else:
            bsv_params: list[str] = []
            for bsv in rule.allowed_bsvs:
                counter += 1
                b_param = f"{param_prefix}_bsv_{counter}"
                params[b_param] = bsv
                bsv_params.append(f":{b_param}")

            groups.append(
                f"({table_alias}.{ledger_col} = :{l_param} AND "
                f"{table_alias}.{bsv_col} IN ({', '.join(bsv_params)}))"
            )

    clause = "(" + " OR ".join(groups) + ")"
    return DASSQLPredicate(clause=clause, params=params)


# =========================================================================
# 3. SQLAlchemy ORM Integration
# =========================================================================


def das_sqlalchemy_filter(
    ctx: DataAccessSetContext,
    model_column_ledger: object,
    model_column_bsv: object,
) -> object:
    """
    Build a SQLAlchemy binary expression suitable for `.where()` filtering.

    Uses SQLAlchemy's ``or_`` / ``and_`` / ``in_`` to produce the same
    security logic as ``apply_das_sql_predicate`` but returns an ORM-safe
    clause element.

    Args:
        ctx: User security context.
        model_column_ledger: SQLAlchemy column attribute (e.g. ``GLBalances.ledger_id``).
        model_column_bsv: SQLAlchemy column attribute (e.g. ``GLBalances.segment1``).

    Returns:
        A SQLAlchemy clause that can be passed to ``select().where()``.
    """
    from sqlalchemy import and_, or_

    if not ctx.rules:
        return _sqlalchemy_literal_false()

    conditions: list[object] = []

    for rule in ctx.rules:
        ledger_cond = model_column_ledger == rule.ledger_id

        if rule.rule_type == DASRuleType.FULL_LEDGER:
            conditions.append(ledger_cond)
        else:
            bsv_cond = model_column_bsv.in_(rule.allowed_bsvs)
            conditions.append(and_(ledger_cond, bsv_cond))

    return or_(*conditions) if len(conditions) > 1 else conditions[0]


def _sqlalchemy_literal_false() -> object:
    from sqlalchemy import literal
    return literal(False)


# =========================================================================
# 4. Caching Stub (Redis-ready)
# =========================================================================


@dataclass
class DASCacheEntry:
    """Pre-computed result keyed by a DAS context fingerprint."""

    key: str
    data: bytes
    ttl_seconds: int


class DASCacheManager:
    """
    Redis-backed cache for pre-aggregated Essbase-like cube slices.

    In production, inject a ``redis.asyncio.Redis`` client.  This stub
    demonstrates the contract and can be swapped for a real Redis backend
    without changing consumer code.

    Usage::

        mgr = DASCacheManager(redis_client=redis.from_url(...))
        cached = await mgr.get("das:v1:abc123")
        if cached is None:
            data = compute_expensive_cube(ctx)
            await mgr.set(ctx.cache_key, data, ttl=3600)
    """

    def __init__(self, redis_client: object | None = None) -> None:
        self._redis = redis_client

    async def get(self, key: str) -> bytes | None:
        """Retrieve cached result or ``None`` on cache miss."""
        if self._redis is None:
            return None
        return await self._redis.get(key)  # type: ignore[union-attr]

    async def set(self, key: str, value: bytes, ttl: int = 3600) -> None:
        """Store a result in the cache with an expiry."""
        if self._redis is None:
            return
        await self._redis.set(key, value, ex=ttl)  # type: ignore[union-attr]

    async def invalidate_user(self, user_id: str) -> None:
        """Drop all cached entries for a user whose DAS rules changed."""
        if self._redis is None:
            return
        pattern = "das:v1:*"
        cursor = 0
        while True:
            cursor, keys = await self._redis.scan(  # type: ignore[union-attr]
                cursor, match=pattern, count=100
            )
            if keys:
                await self._redis.delete(*keys)  # type: ignore[union-attr]
            if cursor == 0:
                break


# =========================================================================
# 5. Async FastAPI Dependency
# =========================================================================


async def resolve_das_context(
    user_id: str,
    *,
    db_session: object | None = None,
) -> DataAccessSetContext:
    """
    Resolve the active Data Access Set for a user.

    In production this queries ``admin.user_business_units`` and related
    DAS-assignment tables.  The stub below returns a full-access context
    for demonstration.

    Args:
        user_id: Authenticated user's UUID.
        db_session: Optional async DB session for live look-up.

    Returns:
        A populated ``DataAccessSetContext``.
    """
    _ = db_session
    return DataAccessSetContext(
        user_id=user_id,
        rules=[
            DASRule(
                ledger_id="US_PRIMARY",
                rule_type=DASRuleType.FULL_LEDGER,
                access_level=AccessLevel.READ_WRITE,
            ),
        ],
    )
