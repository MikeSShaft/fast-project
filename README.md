# Тестовое задание FastAPI

Описание проекта
Это веб-приложение на базе FastAPI , которое управляет данными о брендах обуви, странах их производства и связанных данных. Проект использует PostgreSQL в качестве базы данных и поддерживает миграции через Alembic . Приложение упаковано в контейнеры Docker для удобства развертывания.

Основные возможности:

CRUD-операции для управления данными.
Интеграция с PostgreSQL через SQLAlchemy.
Автоматическая генерация миграций с помощью Alembic.
Запуск приложения в Docker-контейнерах.
Технологии
Backend : FastAPI
ORM : SQLAlchemy
База данных : PostgreSQL
Миграции : Alembic
Контейнеризация : Docker, Docker Compose
Зависимости : Управление зависимостями через requirements.txt

# Установка и запуск
1. Предварительные требования
Для работы с проектом вам потребуется:
- Python 3.10+
- Docker и Docker Compose
- Git
2. Клонирование репозитория
Склонируйте репозиторий на локальную машину:
git clone https://github.com/MikeSShaft/fast-project.git 
cd fast-project

3. Установка зависимостей
Убедитесь, что у вас установлен Python 3.10+. Создайте виртуальное окружение и установите зависимости:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

4. Запуск через Docker
Проект настроен для работы в Docker-контейнерах. Для запуска выполните:
docker-compose up --build

После запуска:

Приложение будет доступно по адресу: http://localhost:8000.
Swagger UI для API: http://localhost:8000/docs.
5. Применение миграций
Если вы хотите применить миграции вручную (например, без Docker), выполните:
alembic upgrade head

Для генерации новых миграций:
alembic revision --autogenerate -m "Migration description"

# API Endpoints
Приложение предоставляет следующие API-эндпоинты:

GET /brands : Получить список всех брендов;
POST /brands : Создать новый бренд;
GET /countries : Получить список всех стран;
POST /countries : Создать новую страну;
GET /brand_countries : Получить связи между брендами и странами;
POST /brand_countries : Создать новую связь;
Документацию API можно просмотреть в интерактивном режиме через Swagger UI: http://localhost:8000/docs.
