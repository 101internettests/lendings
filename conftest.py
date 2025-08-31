import os
import pytest
import allure
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Error as PlaywrightError
from config import bot, chat_id
# Загружаем переменные окружения из .env файла
load_dotenv()


def check_page_status_code(page, url):
    """
    Проверяет статус код страницы и добавляет информацию в Allure отчет
    """
    try:
        # Получаем все ответы для данного URL
        responses = []
        for response_obj in page.context.request.all():
            if url in response_obj.url:
                responses.append(response_obj)
        
        if responses:
            # Берем последний ответ для основного URL
            main_response = responses[-1]
            status_code = main_response.status
            
            with allure.step(f"Проверка статус кода для {url}"):
                allure.attach(
                    f"URL: {url}\nСтатус код: {status_code}",
                    name="Статус код страницы",
                    attachment_type=allure.attachment_type.TEXT
                )
                
                if status_code >= 400:
                    allure.attach(
                        f"Ошибка HTTP: {status_code}\nURL: {url}",
                        name="Ошибка HTTP",
                        attachment_type=allure.attachment_type.TEXT
                    )
                    return False, status_code
                return True, status_code
        else:
            with allure.step(f"Не удалось получить статус код для {url}"):
                allure.attach(
                    f"URL: {url}\nПричина: Нет ответов от сервера",
                    name="Ошибка получения статус кода",
                    attachment_type=allure.attachment_type.TEXT
                )
                return False, None
                
    except Exception as e:
        with allure.step(f"Ошибка при проверке статус кода для {url}"):
            allure.attach(
                f"URL: {url}\nОшибка: {str(e)}",
                name="Исключение при проверке статус кода",
                attachment_type=allure.attachment_type.TEXT
            )
            return False, None


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для перехвата ошибок и добавления информации о статус коде в Allure отчет
    """
    if call.when == "call" and call.excinfo is not None:
        # Получаем фикстуру page если она есть
        page_fixture = None
        for fixture_name in item.funcargs:
            if 'page' in fixture_name:
                page_fixture = item.funcargs[fixture_name]
                break
        
        if page_fixture:
            try:
                # Получаем URL из параметров теста
                url = None
                for param_name, param_value in item.funcargs.items():
                    if 'url' in param_name and isinstance(param_value, str):
                        url = param_value
                        break
                
                if url:
                    success, status_code = check_page_status_code(page_fixture, url)
                    
                    # Добавляем информацию об ошибке в отчет
                    with allure.step("Анализ ошибки"):
                        allure.attach(
                            f"Тип ошибки: {type(call.excinfo.value).__name__}\n"
                            f"Сообщение: {str(call.excinfo.value)}\n"
                            f"URL: {url}\n"
                            f"Статус код: {status_code if status_code else 'Не определен'}",
                            name="Детали ошибки",
                            attachment_type=allure.attachment_type.TEXT
                        )
                        
                        if isinstance(call.excinfo.value, PlaywrightError):
                            allure.attach(
                                f"Playwright ошибка: {str(call.excinfo.value)}",
                                name="Playwright ошибка",
                                attachment_type=allure.attachment_type.TEXT
                            )
                            
            except Exception as e:
                with allure.step("Ошибка при анализе статус кода"):
                    allure.attach(
                        f"Не удалось проверить статус код: {str(e)}",
                        name="Ошибка анализа",
                        attachment_type=allure.attachment_type.TEXT
                    )


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


@pytest.fixture(scope="session")
def providerdom_url():
    """Базовый URL для тестов"""
    return "https://providerdom.ru/"


@pytest.fixture(scope="session")
def msk_providerdom_url():
    """Базовый URL для тестов"""
    return "https://moskva.providerdom.ru/"


@pytest.fixture(scope="session")
def dom_provider_online_url():
    """Базовый URL для тестов"""
    return "https://dom-provider.online/"


@pytest.fixture(scope="session")
def beeline_online():
    """Базовый URL для тестов"""
    return "https://beeline-ru.online/"


@pytest.fixture(scope="session")
def online_beeline():
    """Базовый URL для тестов"""
    return "https://online-beeline.ru/"


@pytest.fixture(scope="session")
def msk_beeline_online():
    """Базовый URL для тестов"""
    return "https://moskva.beeline-ru.online/"


@pytest.fixture(scope="session")
def beeline_internet_online():
    """Базовый URL для тестов"""
    return "https://beeline-internet.online/"


@pytest.fixture(scope="session")
def beeline_pro():
    """Базовый URL для тестов"""
    return "https://beeline-ru.pro/"


@pytest.fixture(scope="session")
def beeline_home_online():
    """Базовый URL для тестов"""
    return "https://beeline-home.online/"


@pytest.fixture(scope="session")
def beeline_internet():
    """Базовый URL для тестов"""
    return "https://beelline-internet.ru/"


@pytest.fixture(scope="session")
def msk_beeline_online_dom():
    """Базовый URL для тестов"""
    return "https://moskva.beeline-ru.online/domashnij-internet"


@pytest.fixture(scope="session")
def msk_beeline_online_tv():
    """Базовый URL для тестов"""
    return "https://moskva.beeline-ru.online/domashnij-internet-tv"


@pytest.fixture(scope="session")
def msk_beeline_online_tariffs():
    """Базовый URL для тестов"""
    return "https://moskva.beeline-ru.online/tariffs-up"


@pytest.fixture(scope="session")
def msk_beeline_online_all_tariffs():
    """Базовый URL для тестов"""
    return "https://moskva.beeline-ru.online/all-tariffs"


@pytest.fixture(scope="session")
def tele_two():
    """Базовый URL для тестов"""
    return "https://t2-official.ru/"


@pytest.fixture(scope="session")
def msk_rtk_online():
    """Базовый URL для тестов"""
    return "https://moskva.rtk-ru.online/"


@pytest.fixture(scope="session")
def rtk_online_ru():
    """Базовый URL для тестов"""
    return "https://rtk-ru.online/"


@pytest.fixture(scope="session")
def rtk_internet_online_ru():
    """Базовый URL для тестов"""
    return "https://rt-internet.online/"


@pytest.fixture(scope="session")
def rtk_home_internet_ru():
    """Базовый URL для тестов"""
    return "https://rtk-home-internet.ru/"


@pytest.fixture(scope="session")
def rtk_internet_online_second():
    """Базовый URL для тестов"""
    return "https://rtk-internet.online/"


@pytest.fixture(scope="session")
def rtk_home_ru_second():
    """Базовый URL для тестов"""
    return "https://rtk-home.ru/"


@pytest.fixture(scope="session")
def msk_rtk_online_home_inter():
    """Базовый URL для тестов"""
    return "https://moskva.rtk-ru.online/domashnij-internet"


@pytest.fixture(scope="session")
def msk_rtk_online_home_inter_tv():
    """Базовый URL для тестов"""
    return "https://moskva.rtk-ru.online/internet-tv"


@pytest.fixture(scope="session")
def msk_rtk_online_home_inter_tv_mobile():
    """Базовый URL для тестов"""
    return "https://moskva.rtk-ru.online/internet-tv-mobile"


@pytest.fixture(scope="session")
def msk_rtk_online_home_tariffs():
    """Базовый URL для тестов"""
    return "https://moskva.rtk-ru.online/all-tariffs"


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