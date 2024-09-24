from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.core.db.database import async_get_db
from src.app.crud.crud_product import crud_product
from src.app.schemas.product import ProductRead, ProductCreate, ProductUpdate

router = APIRouter(tags=["products"])

@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, db: AsyncSession = Depends(async_get_db)):
    product_obj = await crud_product.create(db=db, object=product)
    return product_obj

@router.get("/{product_id}", response_model=ProductRead)
async def read_product(product_id: UUID, db: AsyncSession = Depends(async_get_db)):
    product = await crud_product.get(db, id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductRead)
async def update_product(product_id: UUID, product: ProductUpdate, db: AsyncSession = Depends(async_get_db)):
    return await crud_product.update(db, id=product_id, object=product)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: UUID, db: AsyncSession = Depends(async_get_db)):
    await crud_product.delete(db, id=product_id)