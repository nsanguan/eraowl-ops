"""rename schema log to tms and prod to prd

Revision ID: c3f39ee82df0
Revises: 422e15db3ddf
Create Date: 2026-07-20 12:46:04.895046
"""
from typing import Sequence, Union

from alembic import op


revision: str = 'c3f39ee82df0'
down_revision: Union[str, None] = '422e15db3ddf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('ALTER SCHEMA "log" RENAME TO "tms"')
    op.execute('ALTER SCHEMA "prod" RENAME TO "prd"')


def downgrade() -> None:
    op.execute('ALTER SCHEMA "tms" RENAME TO "log"')
    op.execute('ALTER SCHEMA "prd" RENAME TO "prod"')
