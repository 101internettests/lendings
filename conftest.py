import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from config import bot, chat_id
# Загружаем переменные окружения из .env файла
load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL для тестов"""
    return "https://mts-home.online/"


@pytest.fixture(scope="session")
def second_url():
    """Базовый URL для тестов"""
    return "https://moskva.mts-home.online/"


@pytest.fixture(scope="session")
def third_url():
    """Базовый URL для тестов"""
    return "https://mts-home-gpon.ru/"


@pytest.fixture(scope="session")
def four_url():
    """Базовый URL для тестов"""
    return "https://mts-home-online.ru/"


@pytest.fixture(scope="session")
def five_url():
    """Базовый URL для тестов"""
    return "https://internet-mts-home.online/"


@pytest.fixture(scope="session")
def six_url():
    """Базовый URL для тестов"""
    return "https://mts-internet.online/"


@pytest.fixture(scope="session")
def seven_url():
    """Базовый URL для тестов"""
    return "http://mts-ru.ru/"


@pytest.fixture(scope="session")
def eight_url():
    """Базовый URL для тестов"""
    return "https://mega-premium.ru/"


@pytest.fixture(scope="session")
def eight_two_url():
    """Базовый URL для тестов"""
    return "https://mega-premium.ru/sankt-peterburg"


@pytest.fixture(scope="session")
def nine_url():
    """Базовый URL для тестов"""
    return "https://mega-home-internet.ru/"


@pytest.fixture(scope="session")
def nine_two_url():
    """Базовый URL для тестов"""
    return "https://sankt-peterburg.mega-home-internet.ru/"


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
        browser = playwright.chromium.launch(headless=headless)
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
    context = browser_fixture.new_context()
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


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(chat_id, "🤖 Отчет по лендингам готов!")