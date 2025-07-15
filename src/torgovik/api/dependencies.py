from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.torgovik.core import security
from src.torgovik.db.session import get_db_session
from src.torgovik.models.user import User
from src.torgovik.services import user_service

async def get_current_user(
    token: str = Depends(security.oauth2_scheme),
    session: AsyncSession = Depends(get_db_session)
) -> User:
    """
    Зависимость для получения текущего пользователя из JWT токена.
    """
    token_data = security.verify_token(token)
    user = await user_service.get_user_by_id(
        user_id=int(token_data.sub), session=session
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user