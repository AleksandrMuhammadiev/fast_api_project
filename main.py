import uvicorn
from fastapi import FastAPI, Query, Path, Body

# from items_views import router as users_router
from users.views import router as users_router

app = FastAPI()
# Подключили роутер к приложению для запуска вьюшек
app.include_router(users_router)

# pip install fastapi - Скачаивание библиотеки
# pip install uvicorn - Библиотка для запуска локального сервера
# uvicorn test:app --reload  Команда для запуска сервера
# uvicorn test:app --reload  --port 8080  Команда для запуска сервера  с указанием порта
# /redoc - Путь для перехода на страницу документации
# /docs - переход на страницу автодокументации API  swagger

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
    uvicorn.run("main:app", reload=True)
