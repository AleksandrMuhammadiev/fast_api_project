from fastapi import APIRouter, HTTPException, status, Depends
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import Category
from . import crud
from .schemas import CategoryCreate


router = APIRouter(tags=["Categories"])  # Роутер для подключения к прриложению


@router.get("/", response_model=list[Category])
async def get_categories(
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.get_categories(session=session)

# Функция для добавления нового товара
@router.post('/', response_model=Category)
async def create_category(category_in: CategoryCreate, session: AsyncSession = Depends(db_helper.scope_session_dependency),):

    return await crud.create_category(session=session, category_in=category_in)  # Иначе товар добавиться в Бд

@router.get("/{category_id}/", response_model=Category)
async def get_category(category_id: int, session: AsyncSession = Depends(db_helper.scope_session_dependency),):
    category =  await crud.get_category(session=session, category_id=category_id)
    if category is not None:
        return category

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product by {category_id} not found"
    )