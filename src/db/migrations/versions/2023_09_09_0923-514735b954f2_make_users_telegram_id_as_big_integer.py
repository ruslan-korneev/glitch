"""
make users telegram_id as big integer

Revision ID: 514735b954f2
Revises: b64e9cfdbe6e
Date: 2023-09-09 09:23:40.434636+03:00
"""

import sqlalchemy as sa
from alembic import op

revision = "514735b954f2"
down_revision = "b64e9cfdbe6e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("users", "telegram_id", type_=sa.BigInteger())


def downgrade() -> None:
    op.alter_column("users", "telegram_id", type_=sa.Integer())
