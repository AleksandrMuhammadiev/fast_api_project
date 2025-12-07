# Контроллеры на основе функций

from .schemas import CreateUser

def create_user(user_in: CreateUser):
    user = user_in.model_dump()  # Преобразуем данные в словарь
    return {
        "success": True,
        'user': user
    }


