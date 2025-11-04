import platform
import sys
import os
from config.settings import settings


class OSUtils:
    """Утилиты для работы с разными ОС"""

    @staticmethod
    def get_os_info():
        """Получить информацию об ОС"""
        return {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "architecture": platform.architecture(),
            "processor": platform.processor(),
            "python_version": platform.python_version()
        }

    @staticmethod
    def print_os_info():
        """Вывести информацию об ОС"""
        info = OSUtils.get_os_info()
        print("🤖 Информация о системе:")
        for key, value in info.items():
            print(f"   {key}: {value}")

    @staticmethod
    def make_executable(path):
        """Сделать файл исполняемым (для Unix систем)"""
        if not settings.IS_WINDOWS and path.exists():
            try:
                os.chmod(path, 0o755)
                print(f"✅ Файл {path} сделан исполняемым")
            except Exception as e:
                print(f"⚠️ Не удалось сделать файл исполняемым: {e}")

    @staticmethod
    def setup_environment():
        """Настройка окружения для текущей ОС"""
        print("🔧 Настройка окружения...")
        OSUtils.print_os_info()

        # Создаем необходимые директории
        for directory in [settings.DRIVERS_DIR, settings.REPORTS_DIR,
                          settings.SCREENSHOTS_DIR, settings.LOGS_DIR]:
            directory.mkdir(exist_ok=True)

        print("✅ Окружение настроено")


if __name__ == "__main__":
    OSUtils.setup_environment()