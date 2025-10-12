import os
import pytest
import allure
import time
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Error as PlaywrightError
from config import bot, chat_id
# Загружаем переменные окружения из .env файла
load_dotenv()

# Хранилище метаданных по тестам для итогового отчета (title, description, feature/url)
TEST_META = {}

def extract_run_labels(session, stats) -> list:
    """Возвращает список названий папок запуска (например, test_beeline),
    определённых по аргументам запуска pytest и/или по путям тестов из отчётов."""
    labels = set()
    try:
        root = str(session.config.rootpath)
        args = getattr(session.config, 'args', None) or []
        for arg in args:
            ap = os.path.abspath(arg)
            if not os.path.exists(ap):
                ap2 = os.path.abspath(os.path.join(root, arg))
                ap = ap2 if os.path.exists(ap2) else ap
            if not os.path.exists(ap):
                continue
            rel = os.path.relpath(ap, root)
            parts = rel.replace('\\', '/').split('/')
            if parts and parts[0] == 'tests' and len(parts) > 1:
                labels.add(parts[1])
            elif parts:
                labels.add(parts[0])
    except Exception:
        pass

    if not labels:
        try:
            for key, reports in (stats or {}).items():
                for report in reports:
                    if getattr(report, 'when', 'call') != 'call':
                        continue
                    path = report.nodeid.split('::', 1)[0]
                    parts = path.split('/')
                    if 'tests' in parts:
                        idx = parts.index('tests')
                        if idx is not None and len(parts) > idx + 1:
                            labels.add(parts[idx + 1])
        except Exception:
            pass

    return sorted(labels)


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
    # Фиксируем метаданные для тестов: на падениях (любой стадии) и на успешном выполнении call-этапа
    if (call.excinfo is not None and call.when in ("call", "setup", "teardown")) or (call.excinfo is None and call.when == "call"):
        try:
            # Извлекаем allure.title, если указан декоратором
            title = None
            # Варианты хранения заголовка в объекте теста
            for attr_name in (
                "__allure_display_name__",
                "__allure_title__",
                "allure_title",
                "allure_display_name",
            ):
                title = getattr(getattr(item, "obj", None) or getattr(item, "function", None), attr_name, None)
                if isinstance(title, str) and title.strip():
                    break

            # Попытка достать из маркеров (иногда хранится как маркер)
            if not title:
                try:
                    marker = next(item.iter_markers(name="allure_title"), None)
                    if marker and marker.args:
                        title = str(marker.args[0])
                except Exception:
                    pass

            # Извлекаем allure.description, если есть
            description = None
            for attr_name in (
                "__allure_description__",
                "allure_description",
                "description",
            ):
                description = getattr(getattr(item, "obj", None) or getattr(item, "function", None), attr_name, None)
                if isinstance(description, str) and description.strip():
                    break
            if not description:
                try:
                    marker = next(item.iter_markers(name="allure_description"), None)
                    if marker and marker.args:
                        description = str(marker.args[0])
                except Exception:
                    pass

            # Извлекаем URL: сначала пробуем найти в маркерах allure.feature (или других) строку, похожую на URL
            feature_url = None
            try:
                for m in item.iter_markers():
                    # Собираем все значения аргументов и kwargs
                    values = []
                    try:
                        values.extend(list(m.args))
                    except Exception:
                        pass
                    try:
                        values.extend(list(m.kwargs.values()))
                    except Exception:
                        pass
                    for v in values:
                        if isinstance(v, str) and v.startswith("http"):
                            feature_url = v
                            break
                    if feature_url:
                        break
            except Exception:
                pass

            # Фолбэк: берем первый параметр-URL из funcargs
            if not feature_url:
                try:
                    for k, v in (item.funcargs or {}).items():
                        if isinstance(v, str) and v.startswith("http"):
                            feature_url = v
                            break
                except Exception:
                    pass

            # Сохраняем мета в глобальном словаре для последующего отчета
            TEST_META[item.nodeid] = {
                "title": title,
                "description": description,
                "feature_url": feature_url,
                "when": call.when,
            }
        except Exception:
            # Не мешаем основному ходу, если метаданные не удалось собрать
            pass

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
def mega_home_internet():
    """Базовый URL для тестов"""
    return "https://moskva.mega-home-internet.ru/"


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
def ttk_internet():
    """Базовый URL для тестов"""
    return "https://ttk-internet.ru/"


@pytest.fixture(scope="session")
def ttk_online():
    """Базовый URL для тестов"""
    return "https://ttk-ru.online/"


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
    return "https://serpukhov.rtk-ru.online/"


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
    # Сообщения после прохода отключены. Оставлен пустой хук.
    return


