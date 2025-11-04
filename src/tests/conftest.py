import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from src.pages.main_page import MainPage
import os


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="browser: chrome or firefox"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="run in headless mode"
    )
    parser.addoption(
        "--url",
        action="store",
        default="https://effective-mobile.ru/",
        help="base application URL"
    )


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def is_headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="function")
def driver(browser_type, is_headless, base_url):
    driver = None

    try:
        if browser_type.lower() == "chrome":
            options = Options()

            # Обязательные опции для Docker
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-extensions")

            # В Docker всегда headless
            options.add_argument("--headless=new")

            # Используем удаленный Selenium (в готовом образе)
            driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=options
            )

            print("✓ ChromeDriver успешно инициализирован через Selenium Grid")

        else:
            raise ValueError(f"Unsupported browser: {browser_type}")

        driver.implicitly_wait(10)
        driver.get(base_url)
        print(f"✓ Страница загружена: {driver.current_url}")

        yield driver

    except Exception as e:
        print(f"❌ Ошибка при инициализации драйвера: {e}")
        raise e
    finally:
        if driver:
            driver.quit()
            print("✓ Драйвер закрыт")


@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)