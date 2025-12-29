from __future__ import annotations

from typing import Iterable, Optional

from playwright.sync_api import Locator, Page


class BasePage:
    def __init__(self, page: Optional[Page] = None):
        self.page = page

    def go_back(self):
        self.page.go_back()

    def _first(self, selector: str) -> Locator:
        return self.page.locator(selector).first

    def is_visible(self, selector: str, timeout_ms: int = 500) -> bool:
        """
        Быстрая проверка видимости. Не падает, если элемента нет/DOM меняется.
        """
        try:
            return self._first(selector).is_visible(timeout=timeout_ms)
        except Exception:
            return False

    def click_if_visible(
        self,
        selector: str,
        *,
        timeout_ms: int = 500,
        click_timeout_ms: int = 2000,
        force: bool = True,
    ) -> bool:
        """
        Кликает по элементу, только если он видим. Возвращает True, если кликнули.
        """
        try:
            loc = self._first(selector)
            if not loc.is_visible(timeout=timeout_ms):
                return False
            loc.click(timeout=click_timeout_ms, force=force)
            return True
        except Exception:
            return False

    def click_first_visible(
        self,
        selectors: Iterable[str],
        *,
        timeout_ms: int = 500,
        click_timeout_ms: int = 2000,
        force: bool = True,
    ) -> Optional[str]:
        """
        Ищет первый видимый селектор из списка и кликает по нему.
        Возвращает селектор, по которому кликнули, иначе None.
        """
        for sel in selectors:
            if self.click_if_visible(sel, timeout_ms=timeout_ms, click_timeout_ms=click_timeout_ms, force=force):
                return sel
        return None

    def wait_hidden(self, selector: str, timeout_ms: int = 3000) -> bool:
        """
        Ждёт, что элемент станет hidden/detached. Не падает, возвращает bool.
        """
        try:
            self._first(selector).wait_for(state="hidden", timeout=timeout_ms)
            return True
        except Exception:
            return False

    def wait_all_hidden(self, selectors: Iterable[str], timeout_ms: int = 3000) -> bool:
        ok = True
        for sel in selectors:
            ok = self.wait_hidden(sel, timeout_ms=timeout_ms) and ok
        return ok