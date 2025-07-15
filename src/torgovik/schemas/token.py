from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Не является Pydantic-моделью, но используется для Depends
# Это структура для OAuth2PasswordRequestForm
class TokenPayload(BaseModel):
    sub: Optional[int] = None