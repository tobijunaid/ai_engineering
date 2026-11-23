"""
Invoice lifecycle:

    draft ──confirm──> confirmed ──void──> void
      └──────────────void─────────────────┘

- draft:     items can be added/changed/removed. Stock is NOT touched (rule 6.1).
- confirm:   stock is reduced for every item, all-or-nothing (rule 6.1).
- void:      confirmed → stock restored with 'void_reversal' movements; draft → no stock change.
             Blocked if payments exist. Nothing is ever deleted (rule 6.2).
"""
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from app.models.business import Business
from app.models.invoice import Invoice
from app.models.invoice_item import InvoiceItem
from app.models.payment import Payment
from app.models.user import User
from app.schemas.invoice import InvoiceCreate, InvoiceItemCreate, InvoiceVoid
from app.services.customer_service import get_customer
from app.services.inventory_service import _apply_stock_change
from app.services.product_service import get_product


class InvoiceNotFoundError(Exception):
    pass


class InvoiceItemNotFoundError(Exception):
    pass


class InvoiceStateError(Exception):
    """The action isn't allowed in the invoice's current status."""


class ProductUnavailableError(Exception):
    pass


# --- helpers ----------------------------------------------------------------

def _next_invoice_number(db: Session, business_id: UUID) -> str:
    # Lock the business row so two invoices created at the same moment can't both
    # count N existing invoices and both take number N+1.
    db.scalar(select(Business).where(Business.id == business_id).with_for_update())
    count = db.scalar(select(func.count()).select_from(Invoice).where(Invoice.business_id == business_id))
    # Counting works because invoices are never deleted — numbering has no gaps.
    return f"INV-{count + 1:05d}"


def _recalculate_totals(invoice: Invoice) -> None:
    invoice.subtotal = sum((item.line_total for item in invoice.items), Decimal("0.00"))
    invoice.total = invoice.subtotal  # tax/discounts are out of scope (README §15)


def _require_status(invoice: Invoice, *allowed: str, action: str) -> None:
    if invoice.status not in allowed:
        raise InvoiceStateError(f"Cannot {action} an invoice with status '{invoice.status}'.")


def _add_item(db: Session, user: User, invoice: Invoice, data: InvoiceItemCreate) -> None:
    product = get_product(db, user, data.product_id)  # 404s for other businesses' products
    if not product.is_active:
        raise ProductUnavailableError(f"Product '{product.name}' is inactive.")

    # Same product added twice → one line with a bigger quantity.
    existing = next((i for i in invoice.items if i.product_id == product.id), None)
    if existing:
        existing.quantity += data.quantity
        existing.line_total = existing.unit_price * existing.quantity
        return

    invoice.items.append(InvoiceItem(
        product_id=product.id,
        product_name=product.name,          # snapshot
        quantity=data.quantity,
        unit_price=product.selling_price,   # snapshot
        line_total=product.selling_price * data.quantity,
    ))


def _commit_and_reload(db: Session, invoice: Invoice) -> Invoice:
    db.commit()
    db.refresh(invoice)
    return invoice


# --- queries ----------------------------------------------------------------

def get_invoice(db: Session, user: User, invoice_id: UUID, lock: bool = False) -> Invoice:
    query = select(Invoice).where(
        Invoice.id == invoice_id,
        Invoice.business_id == user.business_id,
    )
    if lock:
        # Used by confirm/void: stops two simultaneous "confirm" clicks from
        # both passing the status check and deducting stock twice.
        query = query.with_for_update()
    invoice = db.scalar(query)
    if invoice is None:
        raise InvoiceNotFoundError("Invoice not found.")
    return invoice


def list_invoices(
    db: Session,
    user: User,
    status: str | None = None,
    customer_id: UUID | None = None,
) -> list[Invoice]:
    query = (
        select(Invoice)
        .where(Invoice.business_id == user.business_id)
        # selectinload: fetch all invoices' items in ONE extra query, instead of one
        # query per invoice when the response is built (the "N+1 query" problem).
        .options(selectinload(Invoice.items), selectinload(Invoice.payments))
        .order_by(Invoice.invoice_number.desc())
    )
    if status:
        query = query.where(Invoice.status == status)
    if customer_id:
        query = query.where(Invoice.customer_id == customer_id)
    return list(db.scalars(query))


# --- draft editing ------------------------------------------------------------

def create_invoice(db: Session, user: User, data: InvoiceCreate) -> Invoice:
    customer = get_customer(db, user, data.customer_id)  # 404s for other businesses' customers
    try:
        invoice = Invoice(
            business_id=user.business_id,
            customer_id=customer.id,
            invoice_number=_next_invoice_number(db, user.business_id),
            status="draft",
            payment_status="unpaid",
            created_by=user.id,
        )
        db.add(invoice)
        for item in data.items:
            _add_item(db, user, invoice, item)
        _recalculate_totals(invoice)
        return _commit_and_reload(db, invoice)
    except Exception:
        db.rollback()
        raise


def add_item(db: Session, user: User, invoice_id: UUID, data: InvoiceItemCreate) -> Invoice:
    invoice = get_invoice(db, user, invoice_id)
    _require_status(invoice, "draft", action="edit")
    try:
        _add_item(db, user, invoice, data)
        _recalculate_totals(invoice)
        return _commit_and_reload(db, invoice)
    except Exception:
        db.rollback()
        raise


def _get_item(invoice: Invoice, item_id: UUID) -> InvoiceItem:
    item = next((i for i in invoice.items if i.id == item_id), None)
    if item is None:
        raise InvoiceItemNotFoundError("Invoice item not found.")
    return item


def update_item(db: Session, user: User, invoice_id: UUID, item_id: UUID, quantity: int) -> Invoice:
    invoice = get_invoice(db, user, invoice_id)
    _require_status(invoice, "draft", action="edit")
    item = _get_item(invoice, item_id)
    item.quantity = quantity
    item.line_total = item.unit_price * quantity
    _recalculate_totals(invoice)
    return _commit_and_reload(db, invoice)


def remove_item(db: Session, user: User, invoice_id: UUID, item_id: UUID) -> Invoice:
    invoice = get_invoice(db, user, invoice_id)
    _require_status(invoice, "draft", action="edit")
    item = _get_item(invoice, item_id)
    # cascade="all, delete-orphan" on Invoice.items: removing it from the list deletes the row.
    invoice.items.remove(item)
    _recalculate_totals(invoice)
    return _commit_and_reload(db, invoice)


# --- lifecycle --------------------------------------------------------------

def confirm_invoice(db: Session, user: User, invoice_id: UUID) -> Invoice:
    invoice = get_invoice(db, user, invoice_id, lock=True)
    try:
        _require_status(invoice, "draft", action="confirm")
        if not invoice.items:
            raise InvoiceStateError("Cannot confirm an invoice with no items.")

        # Reduce stock for every line. _apply_stock_change doesn't commit, so if
        # ANY item lacks stock it raises, we roll back, and NO stock changes at all.
        for item in invoice.items:
            product = get_product(db, user, item.product_id)
            _apply_stock_change(
                db, user, product,
                movement_type="sale",
                change=-item.quantity,
                reason=f"Invoice {invoice.invoice_number} confirmed",
                reference_id=invoice.id,
            )

        invoice.status = "confirmed"
        invoice.confirmed_at = datetime.now(timezone.utc)
        return _commit_and_reload(db, invoice)
    except Exception:
        db.rollback()
        raise


def void_invoice(db: Session, user: User, invoice_id: UUID, data: InvoiceVoid) -> Invoice:
    invoice = get_invoice(db, user, invoice_id, lock=True)
    try:
        _require_status(invoice, "draft", "confirmed", action="void")

        has_payments = db.scalar(
            select(func.count()).select_from(Payment).where(Payment.invoice_id == invoice.id)
        )
        if has_payments:
            raise InvoiceStateError("Cannot void an invoice that has payments recorded.")

        # Only confirmed invoices took stock out, so only they put it back.
        if invoice.status == "confirmed":
            for item in invoice.items:
                product = get_product(db, user, item.product_id)
                _apply_stock_change(
                    db, user, product,
                    movement_type="void_reversal",
                    change=+item.quantity,
                    reason=f"Invoice {invoice.invoice_number} voided",
                    reference_id=invoice.id,
                )

        invoice.status = "void"
        invoice.voided_at = datetime.now(timezone.utc)
        invoice.voided_by = user.id
        invoice.void_reason = data.reason
        return _commit_and_reload(db, invoice)
    except Exception:
        db.rollback()
        raise
