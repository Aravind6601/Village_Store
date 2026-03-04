"""Business logic for customer operations."""

from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.schemas import CustomerCreate


def create_customer(db: Session, payload: CustomerCreate) -> Customer:
    """Create and persist a new customer."""
    customer = Customer(**payload.model_dump())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


def list_customers(db: Session) -> list[Customer]:
    """Return all customers sorted alphabetically by name."""
    return db.query(Customer).order_by(Customer.name.asc()).all()


def get_customer_by_id(db: Session, customer_id: int) -> Customer | None:
    """Fetch a customer by id."""
    return db.query(Customer).filter(Customer.id == customer_id).first()
