from fastcrud import FastCRUD
from ..models.review import Review
from ..schemas.review import ReviewCreate, ReviewRead, ReviewUpdate, ReviewDelete

CRUDReview = FastCRUD[Review, ReviewCreate, ReviewUpdate, ReviewRead, ReviewDelete]
crud_review = CRUDReview(Review)