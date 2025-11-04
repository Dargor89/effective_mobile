@echo off
chcp 65001 >nul
echo 🎯 Effective Mobile Tests
echo =========================

echo 🔨 Сборка Docker образа...
docker build -t effective-tests .

if %errorlevel% neq 0 (
    echo ❌ Ошибка сборки образа
    pause
    exit /b 1
)

echo 🚀 Запуск тестов в Docker...
docker run --rm effective-tests

if %errorlevel% neq 0 (
    echo.
    echo ❌ Тесты завершены с ошибками
) else (
    echo.
    echo ✅ Тесты завершены успешно!
)

pause