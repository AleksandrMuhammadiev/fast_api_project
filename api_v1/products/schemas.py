from pydantic import BaseModel, ConfigDict


# Классы аннатации

# Базовый класс для работы с товаром
class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    category_id: int


# Класс аннотации для добавление нового товара
class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass

class ProductPartial(ProductCreate):
    name: str | None = None
    description: str | None = None
    price: int | None = None
    category_id: int | None = None

# Класс аннотации для получение одного или всех товаров
class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int



