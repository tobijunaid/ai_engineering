from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.dependencies import get_db
from app.models.user import User
from app.schemas.payment import PaymentCreate, PaymentResponse
from app.services.invoice_service import InvoiceNotFoundError, InvoiceStateError
from app.services.payment_service import OverpaymentError, list_payments, record_payment

# Payments live under their invoice: /invoices/{invoice_id}/payments
router = APIRouter(prefix="/invoices/{invoice_id}/payments", tags=["Payments"])

'''
Owners and staff can record and view payments (design doc §5).
'''


@router.post("", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def record_payment_endpoint(
    invoice_id: UUID,
    data: PaymentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return record_payment(db, current_user, invoice_id, data)
    except InvoiceNotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error
    except (InvoiceStateError, OverpaymentError) as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error)) from error


@router.get("", response_model=list[PaymentResponse])
def list_payments_endpoint(
    invoice_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        return list_payments(db, current_user, invoice_id)
    except InvoiceNotFoundError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error
