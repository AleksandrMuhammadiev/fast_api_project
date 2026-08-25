from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from core.models import  Category
from .schemas import CategoryCreate


# Функция получение список категорий   через Сессию
async def get_categories(session: AsyncSession) -> list[Category]:
    stmt = select(Category).order_by(Category.id)
    result: Result = await session.execute(stmt)
    categories = result.scalars().all()
    return list(categories)

# Функция получение  категории по id  через Сессию
async def get_category(session: AsyncSession, category_id: int) -> Category | None:
    return await session.get(Category, category_id)

async def create_category(session: AsyncSession, category_in: CategoryCreate) -> Category:
    category = Category(**category_in.model_dump())
    session.add(category)
    await session.commit()
    # await session.refresh(product)
    return category