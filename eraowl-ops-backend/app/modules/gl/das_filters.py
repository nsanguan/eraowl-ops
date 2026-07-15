"""
General Ledger — Data Access Set (DAS) Security
================================================

Module-specific DAS enforcement for the General Ledger domain.

Re-exports the shared ``das_filters`` primitives and adds GL-specific
conveniences such as a FastAPI dependency that loads the user's DAS
context from the admin security tables.
"""

from __future__ import annotations

import uuid
from typing import Optional

from fastapi import Depends, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.shared.das_filters import (
    # Schemas
    AccessLevel,
    DASRule,
    DASRuleType,
    DataAccessSetContext,
    # Filtering
    apply_das_sql_predicate,
    das_sqlalchemy_filter,
    filter_ledger_balances_df,
    # Caching
    DASCacheEntry,
    DASCacheManager,
    # Predicate
    DASSQLPredicate,
    # Resolver
    resolve_das_context,
)

__all__ = [
    # Schemas
    "AccessLevel",
    "DASRule",
    "DASRuleType",
    "DataAccessSetContext",
    # Filters
    "filter_ledger_balances_df",
    "apply_das_sql_predicate",
    "das_sqlalchemy_filter",
    "DASSQLPredicate",
    # Cache
    "DASCacheEntry",
    "DASCacheManager",
    # Resolver
    "resolve_das_context",
    "get_gl_das_context",
]


# =========================================================================
# GL-specific FastAPI dependency
# =========================================================================


async def get_gl_das_context(
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> DataAccessSetContext:
    """
    FastAPI dependency that resolves the GL Data Access Set for the
    authenticated user by querying ``admin.user_business_units``.

    Falls back to a deny-all context when no BU assignments exist,
    ensuring the user sees zero rows rather than everything.
    """
    from app.core.security import decode_token

    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return _deny_all_context()

    token = auth_header[7:]
    payload = decode_token(token)
    user_id = payload.get("sub")
    if not user_id:
        return _deny_all_context()

    rows = await db.execute(
        select("business_unit_id").where("user_id = :uid"),
        {"uid": uuid.UUID(user_id)},
    )
    bu_ids = [str(r[0]) for r in rows.fetchall()]

    if not bu_ids:
        return _deny_all_context()

    rules: list[DASRule] = [
        DASRule(
            ledger_id="US_PRIMARY",
            rule_type=DASRuleType.PRIMARY_BSV,
            allowed_bsvs=bu_ids,
            access_level=AccessLevel.READ_ONLY,
        ),
    ]

    return DataAccessSetContext(user_id=user_id, rules=rules)


def _deny_all_context() -> DataAccessSetContext:
    return DataAccessSetContext(user_id="anonymous", rules=[])
