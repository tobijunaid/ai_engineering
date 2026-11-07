import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Numeric,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.inventory import Inventory
    from app.db.session import Base
    from app.models.business import Business
    from app.models.inventory_movement import InventoryMovement


class Product(Base):
    __tablename__ = "products"

    __table_args__ = (
        UniqueConstraint(
            "business_id",
            "sku",
            name="uq_products_business_sku"
        ),
        CheckConstraint(
            "selling_price >= 0",
            name="ck_products_selling_price_nonnegative"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    business_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("businesses.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    sku: Mapped[str] = mapped_column(String(50), nullable=False)

    selling_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    
    inventory: Mapped["Inventory"] = relationship(
    "Inventory",
    back_populates="product",
    uselist=False
    )
    
    business: Mapped["Business"] = relationship(
    "Business",
    back_populates="products"
)

    inventory_movements: Mapped[list["InventoryMovement"]] = relationship(
    "InventoryMovement",
    back_populates="product"
    )