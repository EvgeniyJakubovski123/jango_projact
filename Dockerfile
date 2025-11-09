# 1. Базовый образ
FROM python:3.11-slim

# 2. Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 3. Создаём рабочую директорию
WORKDIR /app

# 4. Копируем зависимости и устанавливаем Python-библиотеки
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем проект
COPY app .

# 6. Переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 7. Запуск приложения
CMD ["gunicorn", "library.wsgi:application", "--bind", "0.0.0.0:8000"]
