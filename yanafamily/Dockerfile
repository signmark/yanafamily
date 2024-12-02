# Используем официальный Python образ
FROM python:3.10

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Команда для запуска приложения
CMD ["gunicorn", "yanafamily.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]
