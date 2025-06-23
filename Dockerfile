FROM python:3.10-slim

# Установка UV
RUN pip install uv

# Создание рабочей директории
WORKDIR /app

# Копирование файла зависимостей
COPY requirements.txt .

# Установка зависимостей через UV в системное окружение
RUN uv pip install --system -r requirements.txt

# Копирование остальных файлов проекта
COPY . .

# Запуск приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]