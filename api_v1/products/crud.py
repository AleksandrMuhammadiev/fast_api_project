from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from core.models import Product, Category
from .schemas import ProductCreate, ProductUpdate, ProductPartial


# Функция получение список товаров чрез Сессию
async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)  # Асинхронно отправляет созданный запрос в базу данных на выполнение.
    products = result.scalars().all()  # распаковывает все объекты, оставляя только сами экземпляры модели Product
    return list(products)


# Функция получение  товара по id  чрез Сессию
async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


# Функция добавление товара чрез Сессию
async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product


async def get_products_by_category(session: AsyncSession, category_id: int) -> list[Product]:
    stmt = select(Product).where(Product.category_id == category_id).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


#  put - запрос делает обновление целиком
#  putch - запрос делает обновление некоторых полей

# Функция для put и patch запроса
async def update_product(session: AsyncSession, product: Product,
                         product_update: ProductUpdate | ProductPartial, partial: bool = False) -> Product:
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)

    await session.commit()
    return product


# async def update_product_partial(session: AsyncSession, product: Product, product_partial: ProductPartial):  # для putch
#
#     for name, value in product_partial.model_dump(exclude_unset=True).items():
#         setattr(product, name, value)
#
#     await session.commit()
#     return product


async def delete_product(session: AsyncSession, product: Product) -> None:
    await session.delete(product)
    await session.commit()