#!/bin/bash

echo "=== Запуск тестов в Docker ==="

# Собираем образ
docker-compose build

# Запускаем тесты
docker-compose up tests

# Останавливаем контейнеры
docker-compose down

echo "=== Тесты завершены ==="
echo "Отчеты сохранены в папке ./reports"