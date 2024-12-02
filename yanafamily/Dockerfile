FROM python:3.10

# Установка рабочей директории
WORKDIR /app

# Копируем файл зависимостей перед копированием остального кода
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . /app/

# Команда запуска приложения
CMD ["gunicorn", "yanafamily.wsgi:application", "--bind", "0.0.0.0:8000"]
