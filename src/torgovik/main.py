from fastapi import FastAPI

app = FastAPI(
    title="Torgovik API",
    description="API для минималистичного маркетплейса 'Torgovik'",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """
    Корневой эндпоинт, который возвращает приветственное сообщение.
    """
    return {"message": "Welcome to Torgovik API"}