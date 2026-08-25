from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

# Базовый класс модели для моделей с id полем по умолчанию
class Base(DeclarativeBase):
    __abstract__ = True  # Говорм что данная модель не должна быть создана в Бд делая класс Абстрактным

    @declared_attr.directive
    def __tablename__(cls) -> str:  # Метод который будит задавать имя табдицы от названия модели
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)