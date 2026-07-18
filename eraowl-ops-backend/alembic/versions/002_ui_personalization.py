"""UI personalization: ui_standard_templates + user_ui_personalizations (admin)

Revision ID: 002
Revises: 001
Create Date: 2026-07-18
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "002"
down_revision: Union[str, None] = "001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "ui_standard_templates",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("page_key", sa.String(255), nullable=False),
        sa.Column("schema_version", sa.String(50), nullable=False),
        sa.Column("base_layout_json", postgresql.JSONB(), nullable=False, server_default=sa.text("'{}'::jsonb")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("page_key", name="uq_ui_standard_templates_page_key"),
        schema="admin",
    )
    op.create_index("ix_ui_standard_templates_page_key", "ui_standard_templates", ["page_key"], schema="admin")

    op.create_table(
        "user_ui_personalizations",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("page_key", sa.String(255), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("admin.users.user_id", ondelete="CASCADE"), nullable=True),
        sa.Column("role_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("admin.roles.role_id", ondelete="CASCADE"), nullable=True),
        sa.Column("override_json", postgresql.JSONB(), nullable=False, server_default=sa.text("'{}'::jsonb")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        schema="admin",
    )
    op.create_index("ix_user_ui_personalizations_page_key", "user_ui_personalizations", ["page_key"], schema="admin")


def downgrade() -> None:
    op.drop_index("ix_user_ui_personalizations_page_key", table_name="user_ui_personalizations", schema="admin")
    op.drop_table("user_ui_personalizations", schema="admin")
    op.drop_index("ix_ui_standard_templates_page_key", table_name="ui_standard_templates", schema="admin")
    op.drop_table("ui_standard_templates", schema="admin")
