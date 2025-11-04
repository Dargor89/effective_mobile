FROM python:3.10-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Создаем директории и копируем драйвер
RUN mkdir -p reports drivers

# Делаем драйвер исполняемым (если это бинарный файл)
RUN if [ -f "/app/drivers/chromedriver" ]; then chmod +x /app/drivers/chromedriver; fi

# Или если драйвер в другой директории, скопируйте его
# COPY drivers/chromedriver /app/drivers/chromedriver
# RUN chmod +x /app/drivers/chromedriver