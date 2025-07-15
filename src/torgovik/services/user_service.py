from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.torgovik.models.user import User
from src.torgovik.schemas.user import UserCreate

# Утилиты для хэширования паролей (создадим их на след. шаге)
from src.torgovik.core import security 

async def get_user_by_email(email: str, session: AsyncSession) -> User | None:
    """Получение пользователя по email."""
    query = select(User).where(User.email == email)
    result = await session.execute(query)
    return result.scalars().first()

async def create_user(user_data: UserCreate, session: AsyncSession) -> User:
    """Создание нового пользователя."""
    # 1. Проверяем, не занят ли email
    existing_user = await get_user_by_email(user_data.email, session)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",
        )
    
    # 2. Хэшируем пароль
    hashed_password = security.get_password_hash(user_data.password)

    # 3. Создаем объект модели SQLAlchemy
    new_user = User(
        email=user_data.email,
        hashed_password=hashed_password,
        role=user_data.role,
    )

    # 4. Сохраняем в БД
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return new_user