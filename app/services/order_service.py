"""Business logic for grocery orders."""

from sqlalchemy.orm import Session

from app.models.order import Order
from app.schemas import OrderCreate


def create_order(db: Session, payload: OrderCreate) -> Order:
    """Create and persist a new grocery order."""
    order = Order(
        customer_name=payload.customer_name,
        delivery_address=payload.delivery_address,
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def list_orders(db: Session) -> list[Order]:
    """Return all orders sorted by newest first."""
    return db.query(Order).order_by(Order.created_at.desc()).all()
