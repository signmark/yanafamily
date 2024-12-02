FROM python:3.10

# Установка рабочей директории
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . /app/

# Команда запуска приложения
CMD ["gunicorn", "yanafamily.wsgi:application", "--bind", "0.0.0.0:8000"]
