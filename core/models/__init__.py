__all__ = (  # Указали наименовиние того что должно запускатся в пакете models
    "Base",
    'db_helper',
    'DataBaseHelper',
    "Product",
    "Category",
)

from .base import Base
from .db_helper import db_helper, DataBaseHelper
from .product import Product, Category
