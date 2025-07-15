from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.torgovik.core.config import settings

# Используем асинхронный URL
engine = create_async_engine(settings.async_database_url, pool_pre_ping=True)

AsyncSessionFactory = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db_session() -> AsyncSession:
    """
    Зависимость FastAPI для получения сессии базы данных.
    """
    async with AsyncSessionFactory() as session:
        yield session