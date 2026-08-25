from os import getenv
from pydantic_settings import BaseSettings
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent  # Контатна указывающая абсолютный путь для хнанения файла бд
# Класс настроки какая Бд будит использоватся
class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    db_echo: bool = False  # Что бы не видеть какие запросы были
    # db_echo: bool = True

settings = Settings()




