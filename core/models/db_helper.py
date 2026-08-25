from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession

from core.config import settings
from asyncio import create_task


class DataBaseHelper:  # Класс помошник по созданию таблиц в Бд на основе моделей
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(  # Движок для запуска SQL алхимии
            url=url,
            echo=echo
        )
        # Работа с сессией
        self.session_factory = async_sessionmaker(
            bind=self.engine,  # Указали движок для сессии
            autoflush=False,  # Автоматический флаш перед подготовкой к коммиту
            autocommit=False,  # Автоматическое подтверждение
            expire_on_commit=False,  # отключение автоматического удаление
        )

    # Метод для создания сессии
    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=create_task
        )
        return session

    # Метод для объявления сессии
    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scope_session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()


db_helper = DataBaseHelper(url=settings.db_url, echo=settings.db_echo)  # Создание объекта помошника по созданию таблиц
