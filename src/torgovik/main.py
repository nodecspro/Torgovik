from fastapi import FastAPI

from src.torgovik.api.v1.endpoints.auth import router as auth_router

app = FastAPI(
    title="Torgovik API",
    description="API для минималистичного маркетплейса 'Torgovik'",
    version="1.0.0"
)

# Подключаем роутер аутентификации
# Все пути в нем будут начинаться с /api/v1/auth
app.include_router(
    auth_router, 
    prefix="/api/v1/auth", 
    tags=["Authentication"]
)


@app.get("/")
def read_root():
    """
    Корневой эндпоинт.
    """
    return {"message": "Welcome to Torgovik API"}