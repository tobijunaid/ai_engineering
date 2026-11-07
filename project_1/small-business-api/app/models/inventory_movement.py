import uuid
from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.business import Business
    from app.models.product import Product

class InventoryMovement(Base):
    __tablename__ = "inventory_movements"

    __table_args__ = (
        # These constraints make PostgreSQL enforce valid values, even if an invalid value somehow gets past our API.
        CheckConstraint(
            "movement_type IN ('stock_in', 'sale', 'return', 'damage', 'adjustment')",
            name="ck_inventory_movements_type"
        ),
        CheckConstraint(
            "quantity > 0",
            name="ck_inventory_movements_quantity_positive"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    product_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("products.id"),
        nullable=False
    )

    business_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("businesses.id"),
        nullable=False
    )

    movement_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    reason: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    reference_id: Mapped[uuid.UUID | None] = mapped_column(
        nullable=True
    )

    created_by: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    
    business: Mapped["Business"] = relationship(
    "Business",
    back_populates="inventory_movements"
    )

    product: Mapped["Product"] = relationship(
    "Product",
    back_populates="inventory_movements"
    )