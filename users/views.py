from typing import Annotated
from base import get_user, all_user, save_user
from fastapi import Path, APIRouter

from .schemas import CreateUser
from .crud import create_user

router = APIRouter(tags=['Users'], prefix='/user')  # Создали роутер

@router.get('/all/')
def home():
    users = all_user()
    return users

# Отправка в запрос разные типы данных и нахождение данных по значению
# Path - Это фукция что бы можно было указать максимальное значение и минимальнео значения для pk
@router.get('/{pk}')
def get_user_by_pk(pk: Annotated[int, Path(ge=1, le=len(all_user()))]):
    user = get_user(pk)
    return user



# Запрос на получение данных по нескольким значениям
@router.get('/{pk}/username/{item}/')
def get_item(pk: int, item: str):
    for i in all_user():
        if i['id'] == pk and item == i['username']:
            return i


@router.post('/add/')
def add_user(user: CreateUser):
    save_user(tuple(user.model_dump().values()))  # Функция выполнит сохранение данных пользователя
    return create_user(user_in=user)  # Конроллер обработает и вернёт ответ




