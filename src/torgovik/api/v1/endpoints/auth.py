from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.torgovik.schemas.user import UserCreate, UserRead
from src.torgovik.db.session import get_db_session # Создадим эту функцию
from src.torgovik.services import user_service

router = APIRouter()

@router.post(
    "/register", 
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED
)
async def register_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(get_db_session),
):
    """
    Регистрация нового пользователя.
    """
    user = await user_service.create_user(user_data=user_in, session=session)
    return user