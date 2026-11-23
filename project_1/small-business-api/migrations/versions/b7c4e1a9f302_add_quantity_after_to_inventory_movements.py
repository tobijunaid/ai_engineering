"""add quantity_after to inventory_movements

Revision ID: b7c4e1a9f302
Revises: d1e2c949b2c3
Create Date: 2026-11-23 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7c4e1a9f302'
down_revision: Union[str, Sequence[str], None] = 'd1e2c949b2c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # server_default="0" lets the NOT NULL column be added even if rows already exist;
    # we then drop the default so the application must always supply a real value.
    op.add_column(
        "inventory_movements",
        sa.Column("quantity_after", sa.Integer(), nullable=False, server_default="0"),
    )
    op.alter_column("inventory_movements", "quantity_after", server_default=None)

    op.create_check_constraint(
        "ck_inventory_movements_quantity_after_nonnegative",
        "inventory_movements",
        "quantity_after >= 0",
    )


def downgrade() -> None:
    op.drop_constraint(
        "ck_inventory_movements_quantity_after_nonnegative",
        "inventory_movements",
        type_="check",
    )
    op.drop_column("inventory_movements", "quantity_after")
