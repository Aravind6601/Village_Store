from fastapi import APIRouter

from app.routes.customers import router as customers_router
from app.routes.orders import router as orders_router

api_router = APIRouter()
api_router.include_router(orders_router)
api_router.include_router(customers_router)

__all__ = ["api_router"]
