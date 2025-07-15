# API для маркетплейса "Torgovik" 🚀

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green.svg)
![Docker](https://img.shields.io/badge/Docker-20.10-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-lightgrey.svg)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![linter: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Это бэкенд-сервис (API) для минималистичного маркетплейса. Проект создан в качестве портфолио и демонстрирует применение современного стека технологий и лучших практик в Python-разработке.

## 🌟 Ключевые возможности

*   **Аутентификация и авторизация**:
    *   Регистрация пользователей с ролями (`buyer`, `seller`).
    *   Аутентификация на основе JWT-токенов (`access token`).
    *   Защищенные эндпоинты, доступные только авторизованным пользователям.
*   **Управление пользователями**:
    *   Создание пользователя.
    *   Получение информации о текущем пользователе (`/users/me`).
*   **Работа с базой данных**:
    *   Использование асинхронной ORM **SQLAlchemy 2.0**.
    *   Система миграций базы данных с помощью **Alembic**.
*   **Полная контейнеризация**:
    *   Весь проект и его зависимости (PostgreSQL) запускаются одной командой с помощью **Docker** и **Docker Compose**.
*   **Автоматическая документация API**:
    *   Интерактивная документация (Swagger UI и ReDoc) генерируется автоматически благодаря **FastAPI**.


## 🛠️ Стек технологий

| Категория               | Технология                                               |
| ----------------------- | -------------------------------------------------------- |
| **Бэкенд**              | Python 3.11, FastAPI                                     |
| **База данных**         | PostgreSQL                                               |
| **ORM и миграции**      | SQLAlchemy 2.0 (async), Alembic                          |
| **Валидация данных**    | Pydantic                                                 |
| **Аутентификация**      | JWT (python-jose), хэширование паролей (passlib, bcrypt) |
| **Контейнеризация**     | Docker, Docker Compose                                   |
| **Веб-сервер**          | Uvicorn                                                  |
| **Код-стайл и линтинг** | Black, Ruff                                              |
| **Зависимости**         | Pip, requirements.txt                                    |

## 📂 Структура проекта

Проект имеет модульную структуру для легкой поддержки и расширения.

```
.
├── alembic/                # Конфигурация и версии миграций Alembic
├── alembic.ini             # Главный конфиг Alembic
├── docker-compose.yml      # Файл для оркестрации Docker-контейнеров
├── Dockerfile              # Инструкция по сборке Docker-образа приложения
├── .env.example            # Пример файла с переменными окружения
├── requirements.txt        # Основные зависимости проекта
└── src/
    └── torgovik/
        ├── api/              # API-эндпоинты
        │   ├── dependencies.py # Зависимости FastAPI
        │   └── v1/
        │       └── endpoints/  # Роутеры для разных сущностей
        ├── core/             # Ядро приложения: конфиг, безопасность
        ├── db/               # Настройки подключения и сессий БД
        ├── models/           # Модели SQLAlchemy (описание таблиц)
        ├── schemas/          # Схемы Pydantic (валидация данных)
        ├── services/         # Бизнес-логика
        └── main.py           # Точка входа в приложение FastAPI
```

## 🚀 Запуск проекта локально

### Требования
*   [Docker](https://www.docker.com/get-started)
*   [Docker Compose](https://docs.docker.com/compose/install/) (обычно идет вместе с Docker Desktop)

### Пошаговая инструкция

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/nodecspro/torgovik
    cd torgovik
    ```

2.  **Создайте файл с переменными окружения:**
    Скопируйте `.env.example` в `.env` и при необходимости измените значения.
    ```bash
    cp .env.example .env
    ```

3.  **Запустите проект с помощью Docker Compose:**
    Эта команда соберет образ для FastAPI-приложения и запустит контейнеры для API и базы данных PostgreSQL.
    ```bash
    docker-compose up --build -d
    ```
    *   `--build` - принудительно пересобрать образ.
    *   `-d` - запустить в фоновом режиме (detached).

4.  **Готово!**
    *   API будет доступно по адресу: `http://localhost:8000`
    *   Интерактивная документация Swagger UI: `http://localhost:8000/docs`
    *   Альтернативная документация ReDoc: `http://localhost:8000/redoc`

## 🐘 Работа с миграциями Alembic

Alembic используется для управления версиями схемы базы данных.

### Создание новой миграции

После внесения изменений в модели SQLAlchemy (в папке `src/torgovik/models/`), создайте новую миграцию:
```bash
# Для macOS / Linux
POSTGRES_SERVER=localhost alembic revision --autogenerate -m "Краткое описание миграции"

# Для Windows (PowerShell)
$env:POSTGRES_SERVER="localhost"; alembic revision --autogenerate -m "Краткое описание миграции"
```
*Эта команда должна выполняться из активированного локального виртуального окружения.*

### Применение миграций

Чтобы применить все последние миграции к базе данных:
```bash
POSTGRES_SERVER=localhost alembic upgrade head
```
*(Для Windows команда аналогична примеру выше)*

## ⚙️ Переменные окружения

Все настройки хранятся в файле `.env`. Пример содержимого можно найти в `.env.example`:

```env
# Настройки PostgreSQL
POSTGRES_SERVER=db
POSTGRES_PORT=5432
POSTGRES_USER=torgovik_user
POSTGRES_PASSWORD=your_strong_password
POSTGRES_DB=torgovik_db

# Настройки JWT
JWT_SECRET_KEY=your_super_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 📝 Лицензия

Проект распространяется под лицензией MIT.