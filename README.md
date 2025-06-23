# Тестовое задание FastAPI

Описание проекта<br>
Это веб-приложение на базе FastAPI , которое управляет данными о брендах обуви, странах их производства и связанных данных. Проект использует PostgreSQL в качестве базы данных и поддерживает миграции через Alembic.<br>
Приложение упаковано в контейнеры Docker для удобства развертывания.

Основные возможности:

CRUD-операции для управления данными.<br>
Интеграция с PostgreSQL через SQLAlchemy.<br>
Автоматическая генерация миграций с помощью Alembic.<br>
Запуск приложения в Docker-контейнерах.<br>

# Технологии

Backend : FastAPI<br>
ORM : SQLAlchemy<br>
База данных : PostgreSQL<br>
Миграции : Alembic<br>
Контейнеризация : Docker, Docker Compose<br>
Зависимости : Управление зависимостями через requirements.txt<br>

# Установка и запуск
1. Предварительные требования для работы с проектом вам потребуется:
- Python 3.10+<br>
- Docker и Docker Compose<br>
- Git<br>
2. Клонирование репозитория<br>
Склонируйте репозиторий на локальную машину:<br>
git clone https://github.com/MikeSShaft/fast-project.git <br>
cd fast-project<br>

3. Установка зависимостей
Убедитесь, что у вас установлен Python 3.10+. Создайте виртуальное окружение и установите зависимости:<br>
python3 -m venv .venv<br>
source .venv/bin/activate<br>
pip install -r requirements.txt<br>

4. Запуск через Docker
Проект настроен для работы в Docker-контейнерах. Для запуска выполните:<br>
docker-compose up --build<br>

После запуска:

Приложение будет доступно по адресу: http://localhost:8000.<br>
Swagger UI для API: http://localhost:8000/docs.<br>

5. Применение миграций

Если вы хотите применить миграции вручную (например, без Docker), выполните:<br>
alembic upgrade head<br>

Для генерации новых миграций:<br>
alembic revision --autogenerate -m "Migration description"<br>

# API Endpoints<br>
Приложение предоставляет следующие API-эндпоинты:<br>
![testAPI](https://github.com/user-attachments/assets/efc68a5c-5455-49b4-a08b-86d8e83497d5)

