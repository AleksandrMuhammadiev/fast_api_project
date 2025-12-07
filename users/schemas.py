# Использование Pydantic для сериализации данных при post запросе
from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional
from typing import Annotated
from annotated_types import MinLen, MaxLen


class CreateUser(BaseModel):
    name: str
    # username: str = Field(..., min_length=5, max_length=20)
    username: Annotated[str, MaxLen(5), MaxLen(20)]
    name: str
    email: EmailStr
    phone: str
    address: str

# Что бы указать полю что туда должна попадать почта нужно скачать
#  pip install pydantic[email]
#  pip install email-validator
