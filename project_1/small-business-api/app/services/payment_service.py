"""
Payments (rule 6.3):
- Only confirmed invoices can be paid (a draft isn't a bill yet; a void one is cancelled).
- A payment can never exceed the outstanding balance.
- Every payment updates the invoice's payment_status.
- Payments are never edited or deleted — they are the money trail.
"""
from decimal import Decimal
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.models.payment import Payment
from app.models.user import User
from app.schemas.payment import PaymentCreate
from app.services.invoice_service import InvoiceStateError, get_invoice


class OverpaymentError(Exception):
    pass


def _payment_status(invoice: Invoice) -> str:
    if invoice.amount_paid <= Decimal("0.00"):
        return "unpaid"
    if invoice.balance_due > Decimal("0.00"):
        return "partially_paid"
    return "paid"


def record_payment(db: Session, user: User, invoice_id: UUID, data: PaymentCreate) -> Payment:
    # lock=True: two cashiers recording payments at the same moment can't both see
    # the same balance and together overpay the invoice.
    invoice = get_invoice(db, user, invoice_id, lock=True)
    try:
        if invoice.status != "confirmed":
            raise InvoiceStateError(
                f"Payments can only be recorded on confirmed invoices (this one is '{invoice.status}')."
            )
        if data.amount > invoice.balance_due:
            raise OverpaymentError(
                f"Payment of {data.amount} exceeds the outstanding balance of {invoice.balance_due}."
            )

        payment = Payment(
            invoice_id=invoice.id,
            amount=data.amount,
            payment_method=data.payment_method,
            reference=data.reference,
            recorded_by=user.id,
        )
        # Appending to the relationship (not just db.add) means invoice.amount_paid
        # includes this payment immediately when we recalculate the status below.
        invoice.payments.append(payment)
        invoice.payment_status = _payment_status(invoice)

        db.commit()
        db.refresh(payment)
        return payment
    except Exception:
        db.rollback()
        raise


def list_payments(db: Session, user: User, invoice_id: UUID) -> list[Payment]:
    invoice = get_invoice(db, user, invoice_id)  # business isolation → 404
    return list(db.scalars(
        select(Payment)
        .where(Payment.invoice_id == invoice.id)
        .order_by(Payment.created_at)
    ))
