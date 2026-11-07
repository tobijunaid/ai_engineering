import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.customer import Customer
    from app.models.invoice import Invoice
    from app.models.user import User
    from app.models.product import Product
    from app.models.inventory_movement import InventoryMovement


class Business(Base):
    __tablename__ = "businesses"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    address: Mapped[str | None] = mapped_column(nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    
    users: Mapped[list["User"]] = relationship(
    "User",
    back_populates="business"
    )
    
    products: Mapped[list["Product"]] = relationship(
    "Product",
    back_populates="business"
    )

    inventory_movements: Mapped[list["InventoryMovement"]] = relationship(
    "InventoryMovement",
    back_populates="business"
    )
    
    customers: Mapped[list["Customer"]] = relationship(
    "Customer",
    back_populates="business"
    )

    invoices: Mapped[list["Invoice"]] = relationship(
    "Invoice",
    back_populates="business"
    )