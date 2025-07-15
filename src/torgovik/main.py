from fastapi import FastAPI

from src.torgovik.api.v1.endpoints.auth import router as auth_router
from src.torgovik.api.v1.endpoints.users import router as users_router

app = FastAPI(
    title="Torgovik API",
    description="API для минималистичного маркетплейса 'Torgovik'",
    version="1.0.0"
)

# Роутер аутентификации
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])

# Роутер пользователей
app.include_router(users_router, prefix="/api/v1/users", tags=["Users"])


@app.get("/")
def read_root():
    """
    Корневой эндпоинт.
    """
    return {"message": "Welcome to Torgovik API"}