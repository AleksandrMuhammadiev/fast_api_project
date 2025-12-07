from typing import Annotated
from base import get_user, all_user, save_user
from fastapi import Path, APIRouter

from schemas import User

router = APIRouter(tags=['users'])  # Создали роутер

@router.get('/')
def home():
    users = all_user()
    return users

# Отправка в запрос разные типы данных и нахождение данных по значению
# Path - Это фукция что бы можно было указать максимальное значение и минимальнео значения для pk
@router.get('/user/{pk}')
def get_user_by_pk(pk: Annotated[int, Path(ge=1, le=len(all_user()))]):
    user = get_user(pk)
    return user



# Запрос на получение данных по нескольким значениям
@router.get('/user/{pk}/username/{item}/')
def get_item(pk: int, item: str):
    for i in all_user():
        if i['id'] == pk and item == i['username']:
            return i


@router.post('/add/user/')
def add_user(user: User):
    save_user(tuple(dict(user).values()))
    return user




