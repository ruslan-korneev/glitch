"""
create user table

Revision ID: c2b5c4d9f78b
Revises:
Date: 2023-07-30 21:16:09.595491+03:00
"""

import sqlalchemy as sa
from alembic import op

revision = "c2b5c4d9f78b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "telegram_id",
            sa.SmallInteger(),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("gitlab_profile_id", sa.SmallInteger(), nullable=True),
        sa.Column("username", sa.String(), nullable=True),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("telegram_id"),
    )


def downgrade() -> None:
    op.drop_table("users")
