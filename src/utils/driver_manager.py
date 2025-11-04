from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config.settings import settings
import allure
import os
import time
import requests


class DriverManager:
    """Менеджер для инициализации WebDriver с удаленным Selenium"""

    @staticmethod
    def wait_for_selenium(host='selenium', port=4444, timeout=60):
        """Ожидание готовности Selenium"""
        start_time = time.time()
        url = f"http://{host}:{port}/wd/hub/status"

        print(f"⏳ Ожидаем запуск Selenium на {host}:{port}...")

        while time.time() - start_time < timeout:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    if data.get('value', {}).get('ready', False):
                        print("✅ Selenium готов к работе!")
                        return True
            except requests.exceptions.RequestException as e:
                print(f"⏳ Selenium еще не готов: {e}")

            time.sleep(2)

        raise Exception(f"❌ Selenium не запустился за {timeout} секунд")

    @staticmethod
    @allure.step("Инициализировать браузер")
    def get_driver():
        """Инициализация Chrome драйвера для удаленного Selenium"""
        # Получаем хост Selenium из переменных окружения
        selenium_host = os.getenv('SELENIUM_HOST', 'localhost')

        # Ждем готовности Selenium
        if os.getenv('WAIT_FOR_SELENIUM', 'true').lower() == 'true':
            DriverManager.wait_for_selenium(selenium_host)

        chrome_options = ChromeOptions()

        # Настройки для Chrome в Docker
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument(f"--window-size={settings.WINDOW_SIZE}")
        chrome_options.add_argument("--remote-allow-origins=*")

        # Дополнительные настройки для стабильности
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        # Подключаемся к удаленному Selenium
        try:
            selenium_url = f'http://{selenium_host}:4444/wd/hub'
            print(f"🔗 Подключаемся к Selenium: {selenium_url}")

            driver = webdriver.Remote(
                command_executor=selenium_url,
                options=chrome_options
            )

            # Настройки времени ожидания
            driver.implicitly_wait(settings.IMPLICIT_WAIT)
            driver.set_page_load_timeout(settings.PAGE_LOAD_TIMEOUT)

            print("✅ Драйвер успешно создан!")
            return driver
        except Exception as e:
            print(f"❌ Ошибка при создании драйвера: {e}")
            raise

    @staticmethod
    @allure.step("Закрыть браузер")
    def close_driver(driver):
        """Корректное закрытие драйвера"""
        if driver:
            try:
                driver.quit()
                print("✅ Драйвер успешно закрыт")
            except Exception as e:
                print(f"⚠️ Ошибка при закрытии драйвера: {e}")