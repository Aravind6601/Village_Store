"""Business logic for product inventory CRUD operations."""

from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas import ProductCreate, ProductUpdate


def list_products(db: Session) -> list[Product]:
    """Return all products sorted alphabetically by name."""
    return db.query(Product).order_by(Product.name.asc()).all()


def create_product(db: Session, payload: ProductCreate) -> Product:
    """Create and persist a new product."""
    product = Product(**payload.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_product_by_id(db: Session, product_id: int) -> Product | None:
    """Fetch a product by id."""
    return db.query(Product).filter(Product.id == product_id).first()


def update_product(db: Session, product: Product, payload: ProductUpdate) -> Product:
    """Update an existing product and persist the changes."""
    for field, value in payload.model_dump().items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product: Product) -> None:
    """Delete a product from the inventory."""
    db.delete(product)
    db.commit()
