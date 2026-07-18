"""User Profiles (EBS Profile Options): profile_levels, profile_options, _tl, _values

Revision ID: 003
Revises: 002
Create Date: 2026-07-18
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "003"
down_revision: Union[str, None] = "002"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # --- profile_levels ---
    op.create_table(
        "profile_levels",
        sa.Column("profile_level_id", sa.Integer(), primary_key=True),
        sa.Column("level_code", sa.String(30), nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("precedence", sa.Integer(), nullable=False, server_default=sa.text("100")),
        sa.UniqueConstraint("level_code", name="uq_profile_levels_level_code"),
        schema="admin",
    )
    op.create_index("ix_profile_levels_level_code", "profile_levels", ["level_code"], schema="admin")

    # --- profile_options ---
    op.create_table(
        "profile_options",
        sa.Column("profile_option_id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("profile_option_name", sa.String(255), nullable=False),
        sa.Column("user_profile_option_name", sa.String(255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("value_type", sa.String(20), nullable=False, server_default=sa.text("'text'")),
        sa.Column("sql_validation", sa.Text(), nullable=True),
        sa.Column("site_enabled", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        sa.Column("application_enabled", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("role_enabled", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("user_enabled", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("is_system", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("is_deleted", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        sa.UniqueConstraint("profile_option_name", name="uq_profile_options_name"),
        schema="admin",
    )
    op.create_index("ix_profile_options_name", "profile_options", ["profile_option_name"], schema="admin")

    # --- profile_options_tl ---
    op.create_table(
        "profile_options_tl",
        sa.Column("profile_option_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("admin.profile_options.profile_option_id", ondelete="CASCADE"), nullable=False),
        sa.Column("language", sa.String(10), nullable=False),
        sa.Column("user_profile_option_name", sa.String(255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("source_lang", sa.String(10), nullable=False, server_default=sa.text("'en'")),
        sa.PrimaryKeyConstraint("profile_option_id", "language", name="pk_profile_options_tl"),
        schema="admin",
    )

    # --- profile_option_values ---
    op.create_table(
        "profile_option_values",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("profile_option_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("admin.profile_options.profile_option_id", ondelete="CASCADE"), nullable=False),
        sa.Column("level", sa.String(30), nullable=False),
        sa.Column("level_key", sa.String(255), nullable=True),
        sa.Column("profile_option_value", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
        schema="admin",
    )
    op.create_index("ix_profile_option_values_option", "profile_option_values", ["profile_option_id"], schema="admin")
    op.create_index("ix_profile_option_values_level", "profile_option_values", ["level"], schema="admin")


def downgrade() -> None:
    op.drop_table("profile_option_values", schema="admin")
    op.drop_table("profile_options_tl", schema="admin")
    op.drop_table("profile_options", schema="admin")
    op.drop_index("ix_profile_levels_level_code", "profile_levels", schema="admin")
    op.drop_table("profile_levels", schema="admin")
