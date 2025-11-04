import os


class Settings:
    """Настройки приложения"""

    # Настройки браузera
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    WINDOW_SIZE = os.getenv("WINDOW_SIZE", "1920,1080")
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "15"))

    # URL тестируемого приложения
    BASE_URL = "https://effective-mobile.ru/"

    # Настройки тестов
    DEFAULT_TIMEOUT = 15
    PAGE_LOAD_TIMEOUT = 60


# Глобальный экземпляр настроек
settings = Settings()