@echo off
echo === Запуск тестов в Docker ===

echo Очистка...
docker-compose down

echo Сборка...
docker-compose build --no-cache

echo Запуск тестов...
docker-compose up tests

echo === Тесты завершены ===
echo Проверь отчет: reports/report.html
pause