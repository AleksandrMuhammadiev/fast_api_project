from pydantic import BaseModel, ConfigDict


# Класс валидации Категории
class CategoryBase(BaseModel):
    name: str

# Класс валидации добавления Категории
class CategoryCreate(CategoryBase):
    pass

# Класс валидации получения 1 Категории или всех с id и названием
class Category(CategoryBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
