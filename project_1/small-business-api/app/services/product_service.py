from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.inventory import Inventory
from app.models.product import Product
from app.models.user import User
from app.schemas.product import ProductCreate, ProductUpdate


# Custom exceptions let the router map each failure to the right HTTP status
# (404 vs 409) without the service knowing anything about HTTP.
class ProductNotFoundError(Exception):
    pass


class DuplicateSKUError(Exception):
    pass


def _sku_taken(db: Session, business_id: UUID, sku: str, exclude_id: UUID | None = None) -> bool:
    query = select(Product.id).where(
        Product.business_id == business_id,
        Product.sku == sku,
    )
    if exclude_id is not None:
        query = query.where(Product.id != exclude_id)
    return db.scalar(query) is not None


def create_product(db: Session, user: User, product_data: ProductCreate) -> Product:
    if _sku_taken(db, user.business_id, product_data.sku):
        raise DuplicateSKUError(f"A product with SKU '{product_data.sku}' already exists.")

    try:
        product = Product(
            # business_id comes from the logged-in user, never from the request body,
            # so a user cannot create products for another business.
            business_id=user.business_id,
            **product_data.model_dump(),
        )
        db.add(product)
        db.flush()  # get product.id without committing yet

        # Every product gets exactly one inventory row, starting at 0.
        # Stock is added later through the inventory module.
        db.add(Inventory(product_id=product.id, quantity=0))

        db.commit()  # product + inventory saved together, or not at all
        db.refresh(product)
        return product

    except Exception:
        db.rollback()
        raise


def list_products(db: Session, user: User, include_inactive: bool = False) -> list[Product]:
    query = select(Product).where(Product.business_id == user.business_id)
    if not include_inactive:
        query = query.where(Product.is_active.is_(True))
    return list(db.scalars(query.order_by(Product.name)))


def get_product(db: Session, user: User, product_id: UUID) -> Product:
    # Filtering by business_id means another business's product looks exactly like
    # a missing one (404). We don't even reveal that it exists.
    product = db.scalar(
        select(Product).where(
            Product.id == product_id,
            Product.business_id == user.business_id,
        )
    )
    if product is None:
        raise ProductNotFoundError("Product not found.")
    return product


def update_product(
    db: Session, user: User, product_id: UUID, product_data: ProductUpdate
) -> Product:
    product = get_product(db, user, product_id)

    # exclude_unset=True: only fields the client actually sent are updated.
    changes = product_data.model_dump(exclude_unset=True)

    if "sku" in changes and _sku_taken(db, user.business_id, changes["sku"], exclude_id=product.id):
        raise DuplicateSKUError(f"A product with SKU '{changes['sku']}' already exists.")

    for field, value in changes.items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)
    return product


def set_product_active(db: Session, user: User, product_id: UUID, is_active: bool) -> Product:
    # Soft delete: invoices will reference products, so deleting rows would break
    # historical records. Deactivated products are hidden from the default list.
    product = get_product(db, user, product_id)
    product.is_active = is_active
    db.commit()
    db.refresh(product)
    return product
