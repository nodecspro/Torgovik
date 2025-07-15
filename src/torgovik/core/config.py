from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Класс для хранения настроек приложения, загружаемых из .env файла.
    """
    # Загружаем переменные из .env файла
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Настройки базы данных
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    
    @property
    def database_url(self) -> str:
        """Генерирует URL для подключения к базе данных."""
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

# Создаем единственный экземпляр настроек, который будем использовать во всем приложении
settings = Settings()