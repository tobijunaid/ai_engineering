import uuid
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    ForeignKey,
    Numeric,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.invoice import Invoice
    from app.models.product import Product

class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    __table_args__ = (
        CheckConstraint(
            "quantity > 0",
            name="ck_invoice_items_quantity_positive"
        ),
        CheckConstraint(
            "unit_price >= 0",
            name="ck_invoice_items_unit_price_nonnegative"
        ),
        CheckConstraint(
            "line_total >= 0",
            name="ck_invoice_items_line_total_nonnegative"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    invoice_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("invoices.id"),
        nullable=False
    )

    product_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("products.id"),
        nullable=False
    )

    # Snapshot of the product name when the invoice is created.
    product_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        nullable=False
    )

    unit_price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    line_total: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )
    
    invoice: Mapped["Invoice"] = relationship(
    "Invoice",
    back_populates="items"
    )

    product: Mapped["Product"] = relationship(
    "Product"
    )