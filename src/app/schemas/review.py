from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, UUID4


class ReviewStatus(Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class ReviewBase(BaseModel):
    title: str = Field(min_length=2, max_length=150, examples=["Great Product!"])
    body: str = Field(min_length=1, max_length=63206, examples=["This product is amazing!"])
    product_id: UUID
    status: ReviewStatus = ReviewStatus.PENDING

class ReviewCreate(BaseModel):
    title: str = Field(min_length=2, max_length=150, example="Excellent Product")
    body: str = Field(min_length=10, max_length=1000, example="The product is amazing.")
    product_id: UUID
    status: Optional[ReviewStatus] = ReviewStatus.PENDING

class ReviewUpdate(ReviewBase):
    pass

class ReviewRead(BaseModel):
    id: UUID4
    title: str
    body: str
    product_id: UUID4
    status: str
    created_at: datetime

class ReviewDelete(BaseModel):
    id: UUID
    title: str
    body: str
    product_id: UUID
    status: ReviewStatus
    created_at: datetime