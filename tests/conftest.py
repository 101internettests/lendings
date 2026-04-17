import os
import time

import pytest
from playwright.sync_api import Error as PlaywrightError, Page as SyncPage, sync_playwright


def _env_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    val = raw.strip().lower()
    if val in ("1", "true", "yes", "y", "on"):
        return True
    if val in ("0", "false", "no", "n", "off", ""):
        return False
    return default


try:
    PAGE_NAVIGATION_TIMEOUT_MS = int(os.getenv("PAGE_NAVIGATION_TIMEOUT_MS", "45000"))
except Exception:
    PAGE_NAVIGATION_TIMEOUT_MS = 45000
try:
    PAGE_ACTION_TIMEOUT_MS = int(os.getenv("PAGE_ACTION_TIMEOUT_MS", "30000"))
except Exception:
    PAGE_ACTION_TIMEOUT_MS = 30000
try:
    STABLE_GOTO_RETRIES = int(os.getenv("STABLE_GOTO_RETRIES", "1"))
except Exception:
    STABLE_GOTO_RETRIES = 1
try:
    STABLE_GOTO_RETRY_SLEEP_SEC = float(os.getenv("STABLE_GOTO_RETRY_SLEEP_SEC", "0.6"))
except Exception:
    STABLE_GOTO_RETRY_SLEEP_SEC = 0.6
STABLE_GOTO_ENABLED = _env_bool("STABLE_GOTO_ENABLED", True)


def _is_navigation_timeout_error(exc: Exception) -> bool:
    text = str(exc).lower()
    markers = (
        "timeout",
        "timed out",
        "net::err_timed_out",
        "navigation timeout",
        "page.goto",
    )
    return any(marker in text for marker in markers)


def _patch_playwright_goto_once() -> None:
    """
    Patch Playwright Page.goto globally for this process.
    Needed because assigning page.goto on instance can be ignored/read-only.
    """
    if not STABLE_GOTO_ENABLED:
        return
    if getattr(SyncPage, "_stable_goto_patched", False):
        return

    original_goto = SyncPage.goto

    def _stable_goto(self, url, *args, **kwargs):
        attempts = max(1, STABLE_GOTO_RETRIES + 1)
        for attempt in range(attempts):
            call_kwargs = dict(kwargs)
            if attempt > 0:
                # Retry in lighter mode on transient full-load hangs.
                call_kwargs.setdefault("wait_until", "domcontentloaded")
                call_kwargs.setdefault("timeout", PAGE_NAVIGATION_TIMEOUT_MS)
            try:
                return original_goto(self, url, *args, **call_kwargs)
            except PlaywrightError as exc:
                if not _is_navigation_timeout_error(exc) or attempt == attempts - 1:
                    raise
                time.sleep(STABLE_GOTO_RETRY_SLEEP_SEC)

    SyncPage.goto = _stable_goto  # type: ignore[assignment]
    SyncPage._stable_goto_patched = True  # type: ignore[attr-defined]


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
    _patch_playwright_goto_once()
    # Создаем контекст и страницу
    context = browser_fixture.new_context(
        viewport={'width': 1920, 'height': 1080}
    )
    context.set_default_navigation_timeout(PAGE_NAVIGATION_TIMEOUT_MS)
    context.set_default_timeout(PAGE_ACTION_TIMEOUT_MS)
    page = context.new_page()
    page.set_default_navigation_timeout(PAGE_NAVIGATION_TIMEOUT_MS)
    page.set_default_timeout(PAGE_ACTION_TIMEOUT_MS)
    yield page
    # Закрываем контекст после использования
    context.close()


@pytest.fixture(scope="function")
def page_fixture_ignore_https(browser_fixture_ignore_https):
    """
    Фикстура для создания страницы с игнорированием ошибок HTTPS
    """
    _patch_playwright_goto_once()
    context = browser_fixture_ignore_https.new_context(ignore_https_errors=True)
    context.set_default_navigation_timeout(PAGE_NAVIGATION_TIMEOUT_MS)
    context.set_default_timeout(PAGE_ACTION_TIMEOUT_MS)
    page = context.new_page()
    page.set_default_navigation_timeout(PAGE_NAVIGATION_TIMEOUT_MS)
    page.set_default_timeout(PAGE_ACTION_TIMEOUT_MS)
    yield page
    context.close() 
