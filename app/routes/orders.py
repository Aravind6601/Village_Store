"""API routes for grocery order operations."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas import OrderCreate, OrderRead
from app.services.order_service import create_order, list_orders

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/", response_model=list[OrderRead])
def get_orders(db: Session = Depends(get_db)):
    """Fetch all grocery orders."""
    return list_orders(db)


@router.post("/", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
def post_order(payload: OrderCreate, db: Session = Depends(get_db)):
    """Create a new grocery order."""
    return create_order(db, payload)
