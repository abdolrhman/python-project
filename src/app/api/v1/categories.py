from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.core.db.database import async_get_db
from src.app.crud.crud_category import crud_category
from src.app.schemas.category import CategoryRead, CategoryCreate, CategoryUpdate

router = APIRouter(tags=["categories"])

@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
async def create_category(category: CategoryCreate, db: AsyncSession = Depends(async_get_db)):
    return await crud_category.create(db, object=category)

@router.get("/{category_id}", response_model=CategoryRead)
async def read_category(category_id: UUID, db: AsyncSession = Depends(async_get_db)):
    category = await crud_category.get(db, id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=CategoryRead)
async def update_category(category_id: UUID, category: CategoryUpdate, db: AsyncSession = Depends(async_get_db)):
    return await crud_category.update(db, id=category_id, object=category)

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: UUID, db: AsyncSession = Depends(async_get_db)):
    await crud_category.delete(db, id=category_id)