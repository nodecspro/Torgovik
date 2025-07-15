from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.torgovik.core.config import settings

# Создаем асинхронный движок для подключения к БД
# pool_pre_ping=True проверяет соединение перед каждым запросом
engine = create_async_engine(settings.database_url, pool_pre_ping=True)

# Создаем фабрику для асинхронных сессий
AsyncSessionFactory = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)

# Создаем базовый класс для всех наших моделей SQLAlchemy
# Все наши будущие модели (User, Product) будут наследоваться от него
class Base(DeclarativeBase):
    pass