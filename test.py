import uvicorn
from fastapi import FastAPI, Query, Path, Body
from schemas import Book, User
from typing import List, Optional
from main import get_user, save_user, all_user

app = FastAPI()


# pip install fastapi - Скачаивание библиотеки
# pip install uvicorn - Библиотка для запуска локального сервера
# uvicorn test:app --reload  Команда для запуска сервера
# uvicorn test:app --reload  --port 8080  Команда для запуска сервера  с указанием порта
# /redoc - Путь для перехода на страницу документации
# /docs - переход на страницу автодокументации API  swagger

@app.get('/')
def home():
    users = all_user()
    return users

# Отправка в запрос разные типы данных и нахождение данных по значению
# Path - Это фукция что бы можно было указать максимальное значение и минимальнео значения для pk
@app.get('/user/{pk}')
def get_user_by_pk(pk: int = Path(..., ge=0, le=len(all_user()), )):
    user = get_user(pk)
    return user



# Запрос на получение данных по нескольким значениям
@app.get('/user/{pk}/username/{item}/')
def get_item(pk: int, item: str):
    for i in all_user():
        if i['id'] == pk and item == i['username']:
            return i


@app.post('/add/user/')
def add_user(user: User):
    save_user(tuple(dict(user).values()))
    return user



#  Зпрос на отправку данных Post - зпрос
# Body - это функция при помощи которой в запрос можно передавать доп значения
# Book=Body(..., embed=True) за счёт параметка можно указать что словарь будит передоватся под ключём
# @app.post('/book')
# def create_book(book: Book= Body(..., embed=True), price: int = Body(...)):
#     return {'book': book, 'price': price}
#
#
# # Запрос на поиск по совпадению с максимальным и минимальным значением
# # При помощи тайпинга List можно в q передавать списком сразу несколько значений
# # Query - это функция при помощи которой можно пердать по умолчанию значение а так же описание к запросу
#
# @app.get('/book/')
# def search_user(q: str = Query(None, description='search user')):
#     if q:
#         user = []
#         for i in lst:
#             if q in i['username'] or q in i['name']:
#                 user.append(i)
#         return user
#     else:
#         return q



if __name__ == "__main__":
    uvicorn.run("test:app", reload=True)