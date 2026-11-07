"""add invoice and inventory movement constraints

Revision ID: 891399bba4d9
Revises: 1e8775980a56
Create Date: 2026-11-06 21:21:36.828632

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '891399bba4d9'
down_revision: Union[str, Sequence[str], None] = '1e8775980a56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_check_constraint(
        "ck_invoices_status",
        "invoices",
        "status IN ('draft', 'confirmed', 'void')"
    )

    op.create_check_constraint(
        "ck_invoices_payment_status",
        "invoices",
        "payment_status IN ('unpaid', 'partially_paid', 'paid')"
    )

    op.create_check_constraint(
        "ck_inventory_movements_type",
        "inventory_movements",
        "movement_type IN ('stock_in', 'sale', 'return', 'damage', 'adjustment')"
    )


def downgrade() -> None:
    op.drop_constraint(
        "ck_inventory_movements_type",
        "inventory_movements",
        type_="check"
    )

    op.drop_constraint(
        "ck_invoices_payment_status",
        "invoices",
        type_="check"
    )

    op.drop_constraint(
        "ck_invoices_status",
        "invoices",
        type_="check"
    )
