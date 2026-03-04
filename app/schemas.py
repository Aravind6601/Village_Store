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


class ProductBase(BaseModel):
    name: str
    price: float
    category: str
    stock: int
    unit: str


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CustomerBase(BaseModel):
    name: str
    phone_number: str
    village: str
    address: str


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
