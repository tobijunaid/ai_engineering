from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.inventory import Inventory
from app.models.inventory_movement import InventoryMovement
from app.models.product import Product
from app.models.user import User
from app.schemas.inventory import MovementCreate, StockAdjustment
from app.services.product_service import get_product


class InsufficientStockError(Exception):
    pass


class NoStockChangeError(Exception):
    pass


# Which way each movement type moves stock.
DIRECTION = {
    "stock_in": +1,
    "return": +1,
    "sale": -1,
    "damage": -1,
}


def _get_locked_inventory(db: Session, product_id: UUID) -> Inventory:
    # with_for_update() = SELECT ... FOR UPDATE. PostgreSQL locks this row until the
    # transaction ends, so two simultaneous sales can't both read "5 in stock" and
    # both succeed. The second request waits for the first to commit.
    return db.scalar(
        select(Inventory).where(Inventory.product_id == product_id).with_for_update()
    )


def _apply_stock_change(
    db: Session,
    user: User,
    product: Product,
    movement_type: str,
    change: int,
    reason: str | None = None,
    reference_id: UUID | None = None,
) -> InventoryMovement:
    """
    The ONE place stock is changed. Updates the inventory row and writes the matching
    movement record. Does NOT commit, so callers can group several changes into one
    transaction (e.g. confirming an invoice with many items, later on).
    `change` is signed: positive adds stock, negative removes it.
    """
    inventory = _get_locked_inventory(db, product.id)
    new_quantity = inventory.quantity + change

    if new_quantity < 0:
        raise InsufficientStockError(
            f"Insufficient stock for '{product.name}': "
            f"{inventory.quantity} available, {abs(change)} requested."
        )

    inventory.quantity = new_quantity

    movement = InventoryMovement(
        product_id=product.id,
        business_id=user.business_id,
        movement_type=movement_type,
        quantity=abs(change),
        quantity_after=new_quantity,
        reason=reason,
        reference_id=reference_id,
        created_by=user.id,
    )
    db.add(movement)
    return movement


def record_movement(
    db: Session, user: User, product_id: UUID, data: MovementCreate
) -> InventoryMovement:
    product = get_product(db, user, product_id)  # also enforces business isolation (404)
    try:
        movement = _apply_stock_change(
            db, user, product,
            movement_type=data.movement_type,
            change=DIRECTION[data.movement_type] * data.quantity,
            reason=data.reason,
        )
        db.commit()
        db.refresh(movement)
        return movement
    except Exception:
        db.rollback()
        raise


def adjust_stock(
    db: Session, user: User, product_id: UUID, data: StockAdjustment
) -> InventoryMovement:
    product = get_product(db, user, product_id)
    try:
        current = _get_locked_inventory(db, product.id).quantity
        change = data.new_quantity - current
        if change == 0:
            raise NoStockChangeError(f"Stock is already {current}; nothing to adjust.")

        movement = _apply_stock_change(
            db, user, product, "adjustment", change, reason=data.reason
        )
        db.commit()
        db.refresh(movement)
        return movement
    except Exception:
        db.rollback()
        raise


def _stock_level_query(user: User):
    # A join: one query returns product info + stock together.
    return (
        select(Product.id, Product.name, Product.sku, Inventory.quantity, Inventory.updated_at)
        .join(Inventory, Inventory.product_id == Product.id)
        .where(Product.business_id == user.business_id)
    )


def _to_stock_level(row) -> dict:
    return {
        "product_id": row.id,
        "product_name": row.name,
        "sku": row.sku,
        "quantity": row.quantity,
        "updated_at": row.updated_at,
    }


def list_stock_levels(db: Session, user: User, include_inactive: bool = False) -> list[dict]:
    query = _stock_level_query(user)
    if not include_inactive:
        query = query.where(Product.is_active.is_(True))
    return [_to_stock_level(row) for row in db.execute(query.order_by(Product.name))]


def get_stock_level(db: Session, user: User, product_id: UUID) -> dict:
    get_product(db, user, product_id)  # raises ProductNotFoundError -> 404
    row = db.execute(_stock_level_query(user).where(Product.id == product_id)).one()
    return _to_stock_level(row)


def list_movements(db: Session, user: User, product_id: UUID) -> list[InventoryMovement]:
    get_product(db, user, product_id)
    return list(db.scalars(
        select(InventoryMovement)
        .where(
            InventoryMovement.product_id == product_id,
            InventoryMovement.business_id == user.business_id,
        )
        .order_by(InventoryMovement.created_at.desc())
    ))
