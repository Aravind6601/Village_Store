from fastapi import APIRouter

from app.routes.orders import router as orders_router
from app.routes.products import router as products_router

api_router = APIRouter()
api_router.include_router(orders_router)
api_router.include_router(products_router)

__all__ = ["api_router"]
