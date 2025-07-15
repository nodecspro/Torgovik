from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.torgovik.schemas.user import UserCreate, UserRead
from src.torgovik.schemas.token import Token
from src.torgovik.db.session import get_db_session
from src.torgovik.services import user_service
from src.torgovik.core import security

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

@router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_db_session),
):
    """
    Получение JWT токена.
    """
    # Аутентифицируем пользователя
    user = await user_service.authenticate_user(
        email=form_data.username, # В OAuth2 форме email передается в поле username
        password=form_data.password,
        session=session
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Создаем токен
    access_token = security.create_access_token(
        data={"sub": str(user.id)} # 'sub' - стандартное поле для идентификатора
    )
    
    return {"access_token": access_token, "token_type": "bearer"}