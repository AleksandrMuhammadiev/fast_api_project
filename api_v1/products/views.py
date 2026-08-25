from fastapi import APIRouter, HTTPException, status, Depends
from core.models import db_helper, Category
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from .schemas import Product, ProductCreate, ProductUpdate, ProductPartial
from .dependencies import product_by_id

router = APIRouter(tags=["Products"])  # Роутер для подключения к прриложению


# =======================    Функция для получения списка товаров  =============================
@router.get("/", response_model=list[Product])
async def get_products(
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.get_products(session=session)


# ============================= Функция для добавления нового товара =================================
@router.post('/', response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product_in: ProductCreate,
                         session: AsyncSession = Depends(db_helper.scope_session_dependency), ):
    category = await session.get(Category, product_in.category_id)  # Проверка на сущ указанной id категории
    if not category:  # Если категория не найдена
        raise HTTPException(status_code=404, detail="Category not found")  # Вернётся запрос с ошибкой
    return await crud.create_product(session=session, product_in=product_in)  # Иначе товар добавиться в Бд


#  ============================ Функция для получения товара по id  ==================================
#
# Было изночально до зависимости
# @router.get("/{product_id}/", response_model=Product)
# async def get_product(product_id: int, session: AsyncSession = Depends(db_helper.scope_session_dependency),):
#
#     product =  await crud.get_product(session=session, product_id=product_id)
#     if product is not None:
#         return product
#
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"Product by {product_id} not found"
#     )

# Стыало после зависимости
@router.get("/{product_id}/", response_model=Product)
async def get_product(product: Product = Depends(product_by_id)):
    return product


#  ===============================Функция для получения товаров по id категории===============================

@router.get("/category/{category_id}/", response_model=list[Product])
async def get_products_by_category_id(category_id: int,
                                      session: AsyncSession = Depends(db_helper.scope_session_dependency),
                                      ):
    return await crud.get_products_by_category(session=session, category_id=category_id)


#  ========================   Функция для изменения данных о товаре  =======================================

@router.put("/{product_id}/")
async def update_product(
        product_update: ProductUpdate,
        product: Product = Depends(product_by_id),
        session: AsyncSession = Depends(db_helper.scope_session_dependency)):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update
    )


@router.patch("/{product_id}/")
async def update_product_partial(
        product_update: ProductPartial,
        product: Product = Depends(product_by_id),
        session: AsyncSession = Depends(db_helper.scope_session_dependency)):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True
    )

@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
        product: Product = Depends(product_by_id),
        session: AsyncSession = Depends(db_helper.scope_session_dependency)) -> None:
    await crud.delete_product(session=session, product=product)
