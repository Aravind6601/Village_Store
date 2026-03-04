"""FastAPI entrypoint for the grocery delivery backend."""

from fastapi import FastAPI

from app.database.connection import Base, engine
from app.routes import api_router
from app.routes.products import router as products_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Grocery Delivery API", version="0.1.0")
app.include_router(api_router)
app.include_router(products_router)


@app.get("/")
def health_check():
    """Simple health endpoint."""
    return {"status": "ok", "message": "Grocery delivery backend is running."}
