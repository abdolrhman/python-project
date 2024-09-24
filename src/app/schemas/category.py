from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(min_length=2, max_length=50, examples=["Electronics"])
    parent_id: UUID | None = Field(default=None, examples=["uuid-of-parent-category"])

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id: UUID
    created_at: datetime

class CategoryDelete(BaseModel):
    id: UUID
    name: str
    parent_id: UUID | None
    created_at: datetime