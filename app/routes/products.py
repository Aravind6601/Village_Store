"""API routes for grocery product operations."""

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas import ProductCreate, ProductRead, ProductUpdate
from app.services.product_service import (
    create_product,
    delete_product,
    get_product_by_id,
    list_products,
    update_product,
)

router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=list[ProductRead])
def get_products(db: Session = Depends(get_db)):
    """Fetch all products."""
    return list_products(db)


@router.post("", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def post_product(payload: ProductCreate, db: Session = Depends(get_db)):
    """Create a new product."""
    return create_product(db, payload)


@router.put("/{id}", response_model=ProductRead)
def put_product(id: int, payload: ProductUpdate, db: Session = Depends(get_db)):
    """Update an existing product."""
    product = get_product_by_id(db, id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return update_product(db, product, payload)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_product(id: int, db: Session = Depends(get_db)):
    """Delete a product."""
    product = get_product_by_id(db, id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    delete_product(db, product)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
