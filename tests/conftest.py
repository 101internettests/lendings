import os
import pytest
import allure
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# Load environment variables from .env file


@pytest.fixture(scope="function")
def browser_fixture():
    """
    Фикстура для создания и управления браузером.
    Режим headless контролируется через .env файл
    """
    # Получаем значение HEADLESS из .env (по умолчанию True если не указано)
    headless = os.getenv("HEADLESS", "True").lower() == "true"
    
    with sync_playwright() as playwright:
        # Запускаем браузер с нужными настройками
        browser = playwright.chromium.launch(
            headless=headless
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def browser_fixture_ignore_https():
    """
    Фикстура для создания браузера с игнорированием ошибок HTTPS
    """
    headless = os.getenv("HEADLESS", "True").lower() == "true"
    
    with sync_playwright() as playwright:
        # Запускаем браузер с отключенной проверкой сертификатов
        browser = playwright.chromium.launch(
            headless=headless,
            ignore_https_errors=True
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page_fixture(browser_fixture):
    """
    Фикстура для создания новой страницы в браузере
    """
    # Создаем контекст и страницу
    context = browser_fixture.new_context(
        viewport={'width': 1920, 'height': 1080}
    )
    page = context.new_page()
    yield page
    # Закрываем контекст после использования
    context.close()


@pytest.fixture(scope="function")
def page_fixture_ignore_https(browser_fixture_ignore_https):
    """
    Фикстура для создания страницы с игнорированием ошибок HTTPS
    """
    context = browser_fixture_ignore_https.new_context(ignore_https_errors=True)
    page = context.new_page()
    yield page
    context.close() 