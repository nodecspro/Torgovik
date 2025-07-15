from pydantic import BaseModel, EmailStr, Field

# Общая базовая схема с настройками
class UserBase(BaseModel):
    email: EmailStr

# Схема для создания пользователя (при регистрации)
# Принимаем пароль
class UserCreate(UserBase):
    password: str = Field(min_length=8)
    role: str = "buyer" # По умолчанию роль 'buyer'

# Схема для чтения пользователя (когда мы отдаем данные)
# НЕ ДОЛЖНА содержать пароль!
class UserRead(UserBase):
    id: int
    role: str

    class Config:
        # Эта настройка позволяет Pydantic читать данные
        # из объектов SQLAlchemy (ORM)
        from_attributes = True 