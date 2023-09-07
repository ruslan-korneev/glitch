"""
alter column types for users

Revision ID: b64e9cfdbe6e
Revises: c2b5c4d9f78b
Date: 2023-08-06 11:37:40.235587+03:00
"""

import sqlalchemy as sa
from alembic import op

revision = "b64e9cfdbe6e"
down_revision = "c2b5c4d9f78b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("users", "telegram_id", type_=sa.Integer())
    op.alter_column("users", "gitlab_profile_id", type_=sa.Integer())
    op.alter_column("users", "username", type_=sa.String(64))
    op.alter_column("users", "first_name", type_=sa.String(64))
    op.alter_column("users", "last_name", type_=sa.String(64))


def downgrade() -> None:
    op.alter_column("users", "telegram_id", type_=sa.SmallInteger())
    op.alter_column("users", "gitlab_profile_id", type_=sa.SmallInteger())
    op.alter_column("users", "username", type_=sa.String())
    op.alter_column("users", "first_name", type_=sa.String())
    op.alter_column("users", "last_name", type_=sa.String())
