"""API routes for customer operations."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas import CustomerCreate, CustomerRead
from app.services.customer_service import create_customer, get_customer_by_id, list_customers

router = APIRouter(prefix="/customers", tags=["customers"])


@router.post("", response_model=CustomerRead, status_code=status.HTTP_201_CREATED)
def post_customer(payload: CustomerCreate, db: Session = Depends(get_db)):
    """Create a new customer."""
    return create_customer(db, payload)


@router.get("", response_model=list[CustomerRead])
def get_customers(db: Session = Depends(get_db)):
    """Fetch all customers."""
    return list_customers(db)


@router.get("/{id}", response_model=CustomerRead)
def get_customer(id: int, db: Session = Depends(get_db)):
    """Fetch a customer by id."""
    customer = get_customer_by_id(db, id)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer
