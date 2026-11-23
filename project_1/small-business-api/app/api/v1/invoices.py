from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.security import get_current_user, require_role
from app.db.dependencies import get_db
from app.models.user import User
from app.schemas.invoice import (
    InvoiceCreate,
    InvoiceItemCreate,
    InvoiceItemUpdate,
    InvoiceResponse,
    InvoiceStatus,
    InvoiceVoid,
)
from app.services import invoice_service
from app.services.customer_service import CustomerNotFoundError
from app.services.inventory_service import InsufficientStockError
from app.services.invoice_service import (
    InvoiceItemNotFoundError,
    InvoiceNotFoundError,
    InvoiceStateError,
    ProductUnavailableError,
)
from app.services.product_service import ProductNotFoundError

router = APIRouter(prefix="/invoices", tags=["Invoices"])

'''
Permissions:
- Owners and staff: create drafts, edit draft items, confirm, view.
- Owners only: void (it reverses a sale and rewrites stock).

Error mapping (service exception -> HTTP status) lives in ONE place below,
so every endpoint answers the same way.
'''

ERROR_STATUS = {
    InvoiceNotFoundError: status.HTTP_404_NOT_FOUND,
    InvoiceItemNotFoundError: status.HTTP_404_NOT_FOUND,
    CustomerNotFoundError: status.HTTP_404_NOT_FOUND,
    ProductNotFoundError: status.HTTP_404_NOT_FOUND,
    InvoiceStateError: status.HTTP_409_CONFLICT,
    InsufficientStockError: status.HTTP_409_CONFLICT,
    ProductUnavailableError: status.HTTP_409_CONFLICT,
}


def _run(action, *args):
    """Call a service function and translate known errors into HTTP responses."""
    try:
        return action(*args)
    except tuple(ERROR_STATUS) as error:
        raise HTTPException(status_code=ERROR_STATUS[type(error)], detail=str(error)) from error


@router.post("", response_model=InvoiceResponse, status_code=status.HTTP_201_CREATED)
def create_invoice(
    data: InvoiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return _run(invoice_service.create_invoice, db, current_user, data)


@router.get("", response_model=list[InvoiceResponse])
def list_invoices(
    # alias: the URL says ?status=confirmed, but the Python name doesn't shadow
    # the `status` module imported above.
    status_filter: InvoiceStatus | None = Query(default=None, alias="status"),
    customer_id: UUID | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return invoice_service.list_invoices(db, current_user, status_filter, customer_id)


@router.get("/{invoice_id}", response_model=InvoiceResponse)
def get_invoice(
    invoice_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return _run(invoice_service.get_invoice, db, current_user, invoice_id)


@router.post("/{invoice_id}/items", response_model=InvoiceResponse)
def add_item(
    invoice_id: UUID,
    data: InvoiceItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return _run(invoice_service.add_item, db, current_user, invoice_id, data)


@router.patch("/{invoice_id}/items/{item_id}", response_model=InvoiceResponse)
def update_item(
    invoice_id: UUID,
    item_id: UUID,
    data: InvoiceItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return _run(invoice_service.update_item, db, current_user, invoice_id, item_id, data.quantity)


@router.delete("/{invoice_id}/items/{item_id}", response_model=InvoiceResponse)
def remove_item(
    invoice_id: UUID,
    item_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return _run(invoice_service.remove_item, db, current_user, invoice_id, item_id)


@router.post("/{invoice_id}/confirm", response_model=InvoiceResponse)
def confirm_invoice(
    invoice_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return _run(invoice_service.confirm_invoice, db, current_user, invoice_id)


@router.post("/{invoice_id}/void", response_model=InvoiceResponse)
def void_invoice(
    invoice_id: UUID,
    data: InvoiceVoid,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("owner")),
):
    return _run(invoice_service.void_invoice, db, current_user, invoice_id, data)
