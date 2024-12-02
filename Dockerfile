FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы с зависимостями в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения в контейнер
COPY . /app/

# Экспортируем порт 8000 (если необходимо)
EXPOSE 8000

# Запускаем приложение
CMD ["gunicorn", "yanafamily.wsgi:application", "--bind", "0.0.0.0:8000"]
