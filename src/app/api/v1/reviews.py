from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.core.db.database import async_get_db
from src.app.crud.crud_review import crud_review
from src.app.models import Product, Review
from src.app.schemas.review import ReviewRead, ReviewCreate, ReviewUpdate, ReviewStatus

router = APIRouter(tags=["reviews"])

@router.post("/", response_model=ReviewRead, status_code=status.HTTP_201_CREATED)
async def create_review(review: ReviewCreate, db: AsyncSession = Depends(async_get_db)):
    # Fetch the product instance
    product = await db.get(Product, review.product_id)

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    # Create the review object
    review_obj = Review(
        title=review.title,
        body=review.body,
        status=review.status.value if isinstance(review.status, ReviewStatus) else review.status,
        product_id=review.product_id,
        product=product
    )

    db.add(review_obj)
    await db.commit()
    await db.refresh(review_obj)

    return review_obj

@router.get("/{review_id}", response_model=ReviewRead)
async def read_review(review_id: UUID, db: AsyncSession = Depends(async_get_db)):
    review = await crud_review.get(db, id=review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@router.put("/{review_id}", response_model=ReviewRead)
async def update_review(review_id: UUID, review: ReviewUpdate, db: AsyncSession = Depends(async_get_db)):
    return await crud_review.update(db, id=review_id, object=review)

@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_review(review_id: UUID, db: AsyncSession = Depends(async_get_db)):
    await crud_review.delete(db, id=review_id)