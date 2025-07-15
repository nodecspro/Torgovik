from fastapi import APIRouter, Depends

from src.torgovik.api.dependencies import get_current_user
from src.torgovik.models.user import User
from src.torgovik.schemas.user import UserRead

router = APIRouter()

@router.get("/me", response_model=UserRead)
async def read_users_me(
    current_user: User = Depends(get_current_user)
):
    """
    Получение информации о текущем пользователе.
    """
    return current_user