"""
Unit tests for Data Access Set (DAS) security layer.

Verifies:
  * Pandas DataFrame filtering (row-level security)
  * SQL predicate generation (safe, parameterised)
  * SQLAlchemy ORM clause generation
  * Cache key determinism
  * Deny-all default when no rules exist
"""

import uuid

import pandas as pd
import pytest

from app.shared.das_filters import (
    AccessLevel,
    DASRule,
    DASRuleType,
    DataAccessSetContext,
    DASSQLPredicate,
    apply_das_sql_predicate,
    das_sqlalchemy_filter,
    filter_ledger_balances_df,
)


# -----------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------

@pytest.fixture
def sample_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "ledger_id": [
                "US_PRIMARY", "US_PRIMARY", "US_PRIMARY",
                "US_SECONDARY", "US_SECONDARY", "US_SECONDARY",
                "EU_MAIN",
            ],
            "segment1": ["01", "02", "03", "01", "04", "05", "01"],
            "period_net_dr": [1000.0, 2000.0, 3000.0, 500.0, 700.0, 900.0, 100.0],
        }
    )


@pytest.fixture
def full_access_ctx() -> DataAccessSetContext:
    return DataAccessSetContext(
        user_id="user-full",
        rules=[DASRule(
            ledger_id="US_PRIMARY",
            rule_type=DASRuleType.FULL_LEDGER,
            access_level=AccessLevel.READ_WRITE,
        )],
    )


@pytest.fixture
def partial_access_ctx() -> DataAccessSetContext:
    return DataAccessSetContext(
        user_id="user-partial",
        rules=[
            DASRule(
                ledger_id="US_PRIMARY",
                rule_type=DASRuleType.FULL_LEDGER,
            ),
            DASRule(
                ledger_id="US_SECONDARY",
                rule_type=DASRuleType.PRIMARY_BSV,
                allowed_bsvs=["01", "05"],
            ),
        ],
    )


# -----------------------------------------------------------------------
# Pandas Filter Tests
# -----------------------------------------------------------------------

class TestPandasFilter:
    def test_full_ledger_returns_all_bsv(self, sample_df, full_access_ctx):
        result = filter_ledger_balances_df(sample_df, full_access_ctx)
        assert len(result) == 3
        assert set(result["segment1"]) == {"01", "02", "03"}

    def test_partial_access_filters_multi_ledger(self, sample_df, partial_access_ctx):
        result = filter_ledger_balances_df(sample_df, partial_access_ctx)
        expected = {"US_PRIMARY": {"01", "02", "03"}, "US_SECONDARY": {"01", "05"}}
        for _, row in result.iterrows():
            assert row["segment1"] in expected[row["ledger_id"]]
        assert len(result) == 5  # 3 US_PRIMARY + 2 US_SECONDARY

    def test_empty_rules_returns_empty_df(self, sample_df):
        ctx = DataAccessSetContext(user_id="none")
        result = filter_ledger_balances_df(sample_df, ctx)
        assert len(result) == 0

    def test_no_match_returns_empty(self, sample_df):
        ctx = DataAccessSetContext(
            user_id="no-match",
            rules=[DASRule(
                ledger_id="JP_MAIN",
                rule_type=DASRuleType.FULL_LEDGER,
            )],
        )
        result = filter_ledger_balances_df(sample_df, ctx)
        assert len(result) == 0

    def test_original_df_not_mutated(self, sample_df, full_access_ctx):
        original_len = len(sample_df)
        filter_ledger_balances_df(sample_df, full_access_ctx)
        assert len(sample_df) == original_len

    def test_custom_column_names(self, sample_df):
        df = sample_df.rename(columns={"ledger_id": "lid", "segment1": "bsv"})
        ctx = DataAccessSetContext(
            user_id="x",
            rules=[DASRule(ledger_id="US_PRIMARY", rule_type=DASRuleType.FULL_LEDGER)],
        )
        result = filter_ledger_balances_df(df, ctx, ledger_col="lid", bsv_col="bsv")
        assert len(result) == 3


# -----------------------------------------------------------------------
# SQL Predicate Tests
# -----------------------------------------------------------------------

class TestSQLPredicate:
    def test_full_ledger_predicate(self):
        ctx = DataAccessSetContext(
            user_id="u",
            rules=[DASRule(ledger_id="L1", rule_type=DASRuleType.FULL_LEDGER)],
        )
        pred = apply_das_sql_predicate(ctx)
        assert "(gl.ledger_id = :das_ledger_1)" in pred.clause
        assert pred.params["das_ledger_1"] == "L1"

    def test_primary_bsv_predicate(self):
        ctx = DataAccessSetContext(
            user_id="u",
            rules=[DASRule(
                ledger_id="L1",
                rule_type=DASRuleType.PRIMARY_BSV,
                allowed_bsvs=["01", "03"],
            )],
        )
        pred = apply_das_sql_predicate(ctx)
        assert "IN (:das_bsv_2, :das_bsv_3)" in pred.clause
        assert pred.params["das_bsv_2"] == "01"
        assert pred.params["das_bsv_3"] == "03"

    def test_multi_rule_predicate(self):
        ctx = DataAccessSetContext(
            user_id="u",
            rules=[
                DASRule(ledger_id="L1", rule_type=DASRuleType.FULL_LEDGER),
                DASRule(
                    ledger_id="L2",
                    rule_type=DASRuleType.PRIMARY_BSV,
                    allowed_bsvs=["X"],
                ),
            ],
        )
        pred = apply_das_sql_predicate(ctx)
        assert " OR " in pred.clause
        assert "(gl.ledger_id = :das_ledger_1)" in pred.clause
        assert "gl.segment1 IN" in pred.clause

    def test_empty_rules_generates_false(self):
        ctx = DataAccessSetContext(user_id="u", rules=[])
        pred = apply_das_sql_predicate(ctx)
        assert pred.clause == "FALSE"
        assert pred.params == {}

    def test_custom_table_alias(self):
        ctx = DataAccessSetContext(
            user_id="u",
            rules=[DASRule(ledger_id="L1", rule_type=DASRuleType.FULL_LEDGER)],
        )
        pred = apply_das_sql_predicate(ctx, table_alias="xla")
        assert "(xla.ledger_id = :das_ledger_1)" in pred.clause


# -----------------------------------------------------------------------
# SQLAlchemy Integration Tests
# -----------------------------------------------------------------------

class TestSQLAlchemyIntegration:
    def test_sqlalchemy_filter_builds_clause(self):
        from sqlalchemy import Column, MetaData, String, Table

        t = Table("gl", MetaData(), Column("ledger_id", String), Column("segment1", String))

        ctx = DataAccessSetContext(
            user_id="u",
            rules=[
                DASRule(ledger_id="L1", rule_type=DASRuleType.FULL_LEDGER),
                DASRule(
                    ledger_id="L2",
                    rule_type=DASRuleType.PRIMARY_BSV,
                    allowed_bsvs=["01"],
                ),
            ],
        )
        clause = das_sqlalchemy_filter(ctx, t.c.ledger_id, t.c.segment1)
        sql_str = str(clause.compile(compile_kwargs={"literal_binds": True}))
        assert "L1" in sql_str
        assert "L2" in sql_str
        assert "01" in sql_str

    def test_empty_rules_produces_false(self):
        from sqlalchemy import Column, MetaData, String, Table

        t = Table("gl", MetaData(), Column("ledger_id", String), Column("segment1", String))
        ctx = DataAccessSetContext(user_id="u", rules=[])
        clause = das_sqlalchemy_filter(ctx, t.c.ledger_id, t.c.segment1)
        assert "false" in str(clause.compile(compile_kwargs={"literal_binds": True})).lower()


# -----------------------------------------------------------------------
# Cache & Utility Tests
# -----------------------------------------------------------------------

class TestCacheKey:
    def test_deterministic_cache_key(self):
        rules = [DASRule(ledger_id="L1", rule_type=DASRuleType.FULL_LEDGER)]
        ctx1 = DataAccessSetContext(user_id="u1", rules=rules)
        ctx2 = DataAccessSetContext(user_id="u1", rules=rules)
        assert ctx1.cache_key == ctx2.cache_key

    def test_different_users_have_different_keys(self):
        r = [DASRule(ledger_id="L1", rule_type=DASRuleType.FULL_LEDGER)]
        ctx1 = DataAccessSetContext(user_id="u1", rules=r)
        ctx2 = DataAccessSetContext(user_id="u2", rules=r)
        assert ctx1.cache_key != ctx2.cache_key

    def test_bsv_order_does_not_matter(self):
        ctx1 = DataAccessSetContext(
            user_id="u",
            rules=[DASRule(ledger_id="L1", rule_type="PRIMARY_BSV", allowed_bsvs=["05", "01", "03"])],
        )
        ctx2 = DataAccessSetContext(
            user_id="u",
            rules=[DASRule(ledger_id="L1", rule_type="PRIMARY_BSV", allowed_bsvs=["01", "03", "05"])],
        )
        assert ctx1.cache_key == ctx2.cache_key
