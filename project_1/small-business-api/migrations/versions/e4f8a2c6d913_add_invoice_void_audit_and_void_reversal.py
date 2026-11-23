"""add invoice void audit columns and void_reversal movement type

Revision ID: e4f8a2c6d913
Revises: b7c4e1a9f302
Create Date: 2026-11-23 15:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4f8a2c6d913'
down_revision: Union[str, Sequence[str], None] = 'b7c4e1a9f302'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

OLD_TYPES = "movement_type IN ('stock_in', 'sale', 'return', 'damage', 'adjustment')"
NEW_TYPES = "movement_type IN ('stock_in', 'sale', 'return', 'damage', 'adjustment', 'void_reversal')"


def upgrade() -> None:
    # 1. Void audit trail on invoices (all nullable: only voided invoices have them).
    op.add_column("invoices", sa.Column("voided_at", sa.DateTime(timezone=True), nullable=True))
    op.add_column("invoices", sa.Column("voided_by", sa.Uuid(), nullable=True))
    op.add_column("invoices", sa.Column("void_reason", sa.Text(), nullable=True))
    op.create_foreign_key(
        "fk_invoices_voided_by_users", "invoices", "users", ["voided_by"], ["id"]
    )

    # 2. A check constraint can't be edited in place: drop it and recreate it.
    op.drop_constraint("ck_inventory_movements_type", "inventory_movements", type_="check")
    op.create_check_constraint("ck_inventory_movements_type", "inventory_movements", NEW_TYPES)


def downgrade() -> None:
    # Note: downgrade fails if any 'void_reversal' rows exist — deliberately, so
    # ledger history is never silently lost.
    op.drop_constraint("ck_inventory_movements_type", "inventory_movements", type_="check")
    op.create_check_constraint("ck_inventory_movements_type", "inventory_movements", OLD_TYPES)

    op.drop_constraint("fk_invoices_voided_by_users", "invoices", type_="foreignkey")
    op.drop_column("invoices", "void_reason")
    op.drop_column("invoices", "voided_by")
    op.drop_column("invoices", "voided_at")
