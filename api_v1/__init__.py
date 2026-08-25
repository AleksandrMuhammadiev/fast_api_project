from fastapi import APIRouter
from .products.views import router as products_router
from .category.views import router as category_router


router = APIRouter()
router.include_router(router=products_router, prefix='/products')  # Роутер для получения api товара
router.include_router(router=category_router, prefix='/categories')

