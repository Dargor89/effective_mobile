import os
import subprocess


def check_docker_setup():
    print("=== Проверка Docker окружения ===")

    # Проверяем Chrome
    try:
        result = subprocess.run(['which', 'google-chrome'], capture_output=True, text=True)
        print(f"Chrome путь: {result.stdout.strip()}")
    except:
        print("Chrome не найден")

    # Проверяем ChromeDriver
    try:
        result = subprocess.run(['which', 'chromedriver'], capture_output=True, text=True)
        print(f"ChromeDriver путь: {result.stdout.strip()}")
    except:
        print("ChromeDriver не найден")

    # Проверяем Python зависимости
    try:
        import selenium
        print(f"✓ Selenium установлен: {selenium.__version__}")
    except ImportError:
        print("✗ Selenium не установлен")

    print("=== Проверка завершена ===")


if __name__ == "__main__":
    check_docker_setup()