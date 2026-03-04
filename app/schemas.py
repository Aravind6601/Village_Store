"""Pydantic schemas used by the API layer."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    customer_name: str
    delivery_address: str


class OrderCreate(OrderBase):
    pass


class OrderRead(OrderBase):
    id: int
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
