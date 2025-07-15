from datetime import datetime
from typing import Literal

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.torgovik.db.session import Base

# Определяем возможные роли пользователей
UserRole = Literal["buyer", "seller"]

class User(Base):
    """Модель пользователя."""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(254), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(128))
    role: Mapped[UserRole] = mapped_column(default="buyer")
    
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), # Значение по умолчанию на стороне БД
        default=datetime.utcnow
    )