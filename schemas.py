# Использование Pydantic для сериализации данных при post запросе
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: Optional[str] = None  # Поле не обязательным и что оно может быть пустым


class User(BaseModel):
    name: str
    username: str
    name: str
    email: EmailStr
    phone: str
    address: str

# Что бы указать полю что туда должна попадать почта нужно скачать
#  pip install pydantic[email]
#  pip install email-validator
