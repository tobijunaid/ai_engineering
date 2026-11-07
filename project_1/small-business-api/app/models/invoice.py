import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Numeric,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Invoice(Base):
    __tablename__ = "invoices"

    __table_args__ = (
        # These constraints make PostgreSQL enforce valid values, even if an invalid value somehow gets past our API.
        CheckConstraint(
            "status IN ('draft', 'confirmed', 'void')",
            name="ck_invoices_status"
        ),
        CheckConstraint(
            # These constraints make PostgreSQL enforce valid values, even if an invalid value somehow gets past our API.
            "payment_status IN ('unpaid', 'partially_paid', 'paid')",
            name="ck_invoices_payment_status"
        ),
        
        UniqueConstraint(
            "business_id",
            "invoice_number",
            name="uq_invoices_business_number"
        ),
        CheckConstraint(
            "subtotal >= 0",
            name="ck_invoices_subtotal_nonnegative"
        ),
        CheckConstraint(
            "total >= 0",
            name="ck_invoices_total_nonnegative"
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

    customer_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("customers.id"),
        nullable=False
    )

    invoice_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="draft"
    )

    payment_status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="unpaid"
    )

    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00")
    )

    total: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=Decimal("0.00")
    )

    created_by: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    confirmed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
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