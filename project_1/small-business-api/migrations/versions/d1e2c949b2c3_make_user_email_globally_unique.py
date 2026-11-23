"""make user email globally unique

Revision ID: d1e2c949b2c3
Revises: 891399bba4d9
Create Date: 2026-11-09 20:19:12.582178

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1e2c949b2c3'
down_revision: Union[str, Sequence[str], None] = '891399bba4d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        "uq_users_business_email",
        "users",
        type_="unique"
    )

    op.create_unique_constraint(
        "uq_users_email",
        "users",
        ["email"]
    )


def downgrade() -> None:
    op.drop_constraint(
        "uq_users_email",
        "users",
        type_="unique"
    )

    op.create_unique_constraint(
        "uq_users_business_email",
        "users",
        ["business_id", "email"]
    )