from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str = Field(min_length=2, max_length=100, examples=["Laptop"])
    price: float = Field(gt=0, examples=[999.99])

class ProductCreate(ProductBase):
    name: str = Field(min_length=2, max_length=100, examples=["Laptop"])
    price: float = Field(gt=0, examples=[999.99])

class ProductRead(ProductBase):
    id: UUID

class ProductUpdate(ProductBase):
    pass

class ProductDelete(BaseModel):
    id: UUID
    name: str
    price: float
    created_at: datetime
    categories: list[UUID] = []