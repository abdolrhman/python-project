from fastapi import APIRouter

from .login import router as login_router
from .logout import router as logout_router
from .users import router as users_router
from .categories import router as categories_router
from .products import router as products_router
from .reviews import router as reviews_router

router = APIRouter(prefix="/v1")
router.include_router(login_router)
router.include_router(logout_router)
router.include_router(users_router)
router.include_router(categories_router, prefix="/categories", tags=["categories"])
router.include_router(products_router, prefix="/products", tags=["products"])
router.include_router(reviews_router, prefix="/reviews", tags=["reviews"])

