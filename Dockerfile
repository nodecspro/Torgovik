# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код нашего приложения
COPY ./src/torgovik ./src/torgovik

# Указываем команду, которая будет выполняться при запуске контейнера
# Запускаем uvicorn, чтобы он был доступен извне контейнера (host 0.0.0.0)
CMD ["uvicorn", "src.torgovik.main:app", "--host", "0.0.0.0", "--port", "8000"]