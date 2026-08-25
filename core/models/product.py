from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


# Модель категории
class Category(Base):
    name: Mapped[str]



# Модель Товара
class Product(Base):
    # __tablename__ = "product"  # Испольуем что бы казать название тыблицы в бд

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
