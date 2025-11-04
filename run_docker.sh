#!/bin/bash

echo "=== Запуск тестов в Docker ==="

# Очищаем предыдущие контейнеры
docker-compose down

# Собираем образ
docker-compose build --no-cache

# Запускаем тесты
docker-compose up tests

echo "=== Тесты завершены ==="
echo "Отчет: file://$(pwd)/reports/report.html"