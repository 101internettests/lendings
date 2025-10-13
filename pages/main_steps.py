import time
import allure
import random
import re
from urllib.parse import urlparse
from playwright.sync_api import expect
from locators.mts.mts_home_online import MTSHomeOnlineMain
from locators.all_locators import Main
from pages.base_page import BasePage
from pages.page_mts.mts_page import ChoiceRegionPage
from locators.all_locators import (
    Profit,
    Connection,
    Checkaddress,
    Undecided,
    Business,
    Moving,
    ExpressConnection,
)
from locators.mts.mts_home_online import RegionChoice


class MainSteps(BasePage):

    @allure.title("Отправить заявку в попап 'Выгодное спецпредложение!' с домом 1")
    def send_popup_profit(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Profit.STREET).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Profit.HOUSE).fill("1")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(Profit.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Profit.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап 'Выгодное спецпредложение!' с домом 2")
    def send_popup_profit_second_house(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Profit.STREET).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Profit.HOUSE).fill("2")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(Profit.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Profit.BUTTON_SEND).click()
            time.sleep(4)

    def _click_first_available_house(self):
        try:
            self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click(timeout=3000)
            return
        except Exception:
            pass
        try:
            self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE_SECOND).click(timeout=3000)
            return
        except Exception:
            pass
        raise AssertionError("Не удалось кликнуть по варианту дома: нет первого и второго вариантов")

    def _verify_city_label_accepts_variants(self, expected_city: str):
        # Принимаем как валидные варианты:
        # 1) Точное совпадение названия города
        # 2) Текст вида "Вы находитесь в городе <город>"
        # 3) Для падежных форм допускаем замену последней буквы города на "у" или "е"
        candidates = [
            RegionChoice.NEW_REGION_CHOICE_BUTTON,
            RegionChoice.TELE_REGION_CHOICE_BUTTON,
            RegionChoice.REGION_CHOICE_BUTTON,
        ]

        def normalize(text: str) -> str:
            return re.sub(r"\s+", " ", (text or "").strip())

        expected_norm = normalize(expected_city)

        def city_variants(base: str):
            variants = {base}
            if len(base) >= 2:
                variants.add(base[:-1] + "у")
                variants.add(base[:-1] + "е")
            return list(variants)

        variants = city_variants(expected_norm)
        accepted_patterns = []
        for v in variants:
            accepted_patterns.append(v)
            accepted_patterns.append(f"Вы находитесь в городе {v}")

        found_texts = []
        for sel in candidates:
            try:
                loc = self.page.locator(sel)
                if loc.count() == 0:
                    continue
                text = normalize(loc.first.text_content() or "")
                if text:
                    found_texts.append(text)
                    if any((pat == text) or (pat in text) for pat in accepted_patterns):
                        return
            except Exception:
                continue

        # Фоллбэк: проверим текст всей страницы
        try:
            body_text = normalize(self.page.locator("body").text_content() or "")
            if any(pat in body_text for pat in accepted_patterns):
                return
        except Exception:
            pass

        raise AssertionError(
            f"Город не подтверждён. Допустимые варианты: {accepted_patterns}. Найденные тексты: {found_texts}"
        )

    @allure.title("Нажать на кнопку Изменить город")
    def button_change_city_profit(self):
        self.page.locator(Profit.BUTTON_CHANGE_CITY).click()

    @allure.title("Нажать на кнопку Изменить город")
    def button_change_city_connection(self):
        self.page.locator(Connection.BUTTON_CHANGE_CITY).click()

    @allure.title("Нажать на кнопку Изменить город")
    def button_change_city_checkaddress(self):
        self.page.locator(Checkaddress.BUTTON_CHANGE_CITY).click()

    @allure.title("Нажать на кнопку Изменить город")
    def button_change_city_moving(self):
        self.page.locator(Moving.BUTTON_CHANGE_CITY).click()

    @allure.title("Нажать на кнопку Изменить город")
    def button_change_city_express_connection(self):
        self.page.locator(ExpressConnection.BUTTON_CHANGE_CITY).click()

    @allure.title("Нажать на кнопку Изменить город в блоке 'Остались вопросы?' по индексу (1-based)")
    def button_change_city_undecideds(self, index: int):
        self.page.locator(Undecided.BUTTON_CHANGE_CITY).nth(index - 1).click()

    @allure.title("Нажать на кнопку Изменить город в блоке 'Проверить адрес' по индексу (1-based)")
    def button_change_city_checkaddress_block(self, index: int):
        self.page.locator(Checkaddress.BUTTON_CHANGE_CITY_BLOCK).nth(index - 1).click()

    @allure.title("Закрыть попап")
    def close_popup(self):
        self.page.locator(Main.CLOSE).click()

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def open_popup_for_colorful_button(self):
        self.page.locator(Profit.COLORFUL_BUTTON).click()

    @allure.title("Нажать на кнопку Подключиться в хедере")
    def open_popup_express_connection_button(self):
        self.page.locator(ExpressConnection.FORM_BUTTON).click()

    @allure.title("Кликнуть на кнопку Подключить по индексу (1-based)")
    def click_connect_button_index(self, index: int):
        selector = f"xpath=(//button[contains(@class,'connection_address_button')])[{index}]"
        self.page.locator(selector).click()

    @allure.title("Кликнуть на кнопку Подключить по индексу (1-based)")
    def click_connect_button_index_cards(self, index: int):
        selector = f"xpath=(//button[contains(@class,'connection_address_card_button')])[{index}]"
        self.page.locator(selector).click()

    @allure.title("Кликнуть на кнопку Проверить адрес по индексу (1-based)")
    def click_checkaddress_popup_index(self, index: int):
        selector = f"xpath=(//button[contains(@class,'checkaddress_address_button')])[{index}]"
        self.page.locator(selector).click()

    @allure.title("Кликнуть на кнопку Переехать по индексу (1-based)")
    def click_moving_popup_index(self, index: int):
        selector = f"xpath=(//button[contains(@class,'moving_address_button')])[{index}]"
        self.page.locator(selector).click()

    @allure.title("Посчитать количество кнопок Подключить")
    def count_connect_buttons(self) -> int:
        return self.page.locator(Connection.CONNECT_BUTTON).count()

    @allure.title("Посчитать количество кнопок Подключить")
    def count_connect_buttons_cards(self) -> int:
        return self.page.locator(Connection.CONNECT_BUTTON).count()

    @allure.title("Посчитать количество кнопок Проверить адрес")
    def count_checkaddress_popup_buttons(self) -> int:
        return self.page.locator(Checkaddress.CHECKADDRESS_BUTTON_POPUP).count()

    @allure.title("Посчитать количество блоков Проверить адрес")
    def count_checkaddress_blocks(self) -> int:
        return self.page.locator(Checkaddress.CHECKADDRESS_BLOCK).count()

    @allure.title("Посчитать количество блоков формы Остались вопросы?")
    def count_undecided_blocks(self) -> int:
        return self.page.locator(Undecided.UNDECIDED_BLOCK).count()

    @allure.title("Посчитать количество кнопок Переехать")
    def count_moving_popup_buttons(self) -> int:
        return self.page.locator(Moving.MOVING_BUTTON).count()

    @allure.title("Посчитать количество кнопок Подробнее на странице бизнеса")
    def count_business_buttons(self) -> int:
        first_count = self.page.locator(Business.MORE_BUTTON).count()
        if first_count > 0:
            return first_count
        second_count = self.page.locator(Business.MORE_BUTTON_SECOND).count()
        if second_count > 0:
            return second_count
        return self.page.locator(Business.MORE_BUTTON_ANY).count()

    @allure.title("Клик по бизнес-кнопке: хедер или 'Подробнее' по индексу")
    def click_business_button(self, index: int = 0):
        # index <= 0: клик по кнопке в хэдере (первой доступной)
        # index >= 1: клик по кнопке 'Подробнее' на странице бизнеса по индексу (1-based)
        if index <= 0:
            header_candidates = [
                getattr(Business, "BUSINESS_BUTTON", None),
                getattr(Business, "BUSINESS_BUTTON_SECOND", None),
                getattr(Business, "BUSINESS_BUTTON_THIRD", None),
            ]
            for sel in header_candidates:
                if not sel:
                    continue
                try:
                    self.page.locator(sel).click(timeout=3000)
                    return
                except Exception:
                    continue
            raise AssertionError("Кнопка Бизнес не появилась")

        # Иначе кликаем по кнопкам 'Подробнее' по индексу
        buttons_primary = self.page.locator(Business.MORE_BUTTON)
        total_primary = buttons_primary.count()
        if total_primary >= index and total_primary > 0:
            buttons_primary.nth(index - 1).click()
            return

        buttons_fallback = self.page.locator(Business.MORE_BUTTON_SECOND)
        total_fallback = buttons_fallback.count()
        if total_fallback >= index and total_fallback > 0:
            buttons_fallback.nth(index - 1).click()
            return

        # Третий вариант: любой элемент с классом services-business
        buttons_any = self.page.locator(Business.MORE_BUTTON_ANY)
        total_any = buttons_any.count()
        if total_any >= index and total_any > 0:
            buttons_any.nth(index - 1).click()
            return

        raise AssertionError(f"Кнопка Подробнее №{index} не найдена")

    @allure.title("Нажать на кнопку Подключить на странице бизнеса")
    def connect_business_page(self):
        try:
            self.page.locator(Business.CONNECT_BUTTON).click(timeout=3000)
            return
        except Exception:
            pass
        try:
            self.page.locator(Business.CONNECT_BUTTON_SECOND).click(timeout=3000)
            return
        except Exception:
            pass
        raise AssertionError("Кнопка Подключить на странице бизнеса не найдена")
        self.page.locator(Business.CONNECT_BUTTON_SECOND).click()

    @allure.title("Отправить заявку в попап 'Заявка на подключение'")
    def send_popup_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Connection.STREET).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Connection.HOUSE).fill("1")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(Connection.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Connection.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап 'Заявка на подключение'")
    def send_popup_connection_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Connection.STREET).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Connection.HOUSE).fill("2")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(Connection.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Connection.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап/форму 'Проверить адрес'")
    def send_popup_checkaddress(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Checkaddress.STREET).last.type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Checkaddress.HOUSE).last.fill("1")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(Checkaddress.PHONE).last.fill("99999999999")
            time.sleep(1)
            self.page.locator(Checkaddress.BUTTON_SEND).last.click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап/форму 'Проверить адрес'")
    def send_popup_checkaddress_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Checkaddress.STREET).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Checkaddress.HOUSE).fill("2")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(Checkaddress.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Checkaddress.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в блоке 'Проверить адрес' по индексу (1-based)")
    def send_popup_checkaddress_block(self, index: int):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Checkaddress.STREET).nth(index - 1).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).first.click()
            time.sleep(1)
            self.page.locator(Checkaddress.HOUSE).nth(index - 1).fill("1")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(Checkaddress.PHONE).nth(index - 1).fill("99999999999")
            time.sleep(1)
            self.page.locator(Checkaddress.BUTTON_SEND).nth(index - 1).click()
            time.sleep(4)

    @allure.title("Отправить заявку в блоке 'Проверить адрес' по индексу (1-based)")
    def send_popup_checkaddress_block_second(self, index: int):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Checkaddress.STREET).nth(index - 1).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).first.click()
            time.sleep(1)
            self.page.locator(Checkaddress.HOUSE).nth(index - 1).fill("2")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(Checkaddress.PHONE).nth(index - 1).fill("99999999999")
            time.sleep(1)
            self.page.locator(Checkaddress.BUTTON_SEND).nth(index - 1).click()
            time.sleep(4)

    @allure.title("Отправить заявку в форму 'Не определились с тарифом?'")
    def send_form_undecided(self, index: int):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Undecided.STREET).nth(index - 1).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).first.click()
            time.sleep(1)
            self.page.locator(Undecided.HOUSE).nth(index - 1).fill("1")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(Undecided.PHONE).nth(index - 1).fill("99999999999")
            time.sleep(1)
            self.page.locator(Undecided.BUTTON_SEND).nth(index - 1).click()
            time.sleep(4)

    @allure.title("Отправить заявку в форму 'Не определились с тарифом?'")
    def send_form_undecided_second(self, index: int):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Undecided.STREET).nth(index - 1).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).first.click()
            time.sleep(1)
            self.page.locator(Undecided.HOUSE).nth(index - 1).fill("2")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(Undecided.PHONE).nth(index - 1).fill("99999999999")
            time.sleep(1)
            self.page.locator(Undecided.BUTTON_SEND).nth(index - 1).click()
            time.sleep(4)

    @allure.title("Отправить заявку в форму 'Не определились с тарифом?'")
    def send_form_undecided_third(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Undecided.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Undecided.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап 'Заявка на подключение для Бизнеса'")
    def send_popup_business(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Business.FULL_ADDRESS).last.type("Тестадрес", delay=100)
            time.sleep(1)
            self.page.locator(Business.PHONE).last.fill("99999999999")
            time.sleep(1)
            self.page.locator(Business.BUTTON_SEND).last.click()
            time.sleep(1)

    @allure.title("Отправить заявку в попап 'Заявка на подключение для Услуги переезд'")
    def send_popup_moving(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Moving.STREET).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).first.click()
            time.sleep(1)
            self.page.locator(Moving.HOUSE).fill("1")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(Moving.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Moving.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап 'Заявка на подключение для Услуги переезд'")
    def send_popup_moving_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Moving.STREET).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).first.click()
            time.sleep(1)
            self.page.locator(Moving.HOUSE).fill("2")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(Moving.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Moving.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап 'Заявка на экспресс подключение'")
    def send_popup_express_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ExpressConnection.STREET).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).first.click()
            time.sleep(1)
            self.page.locator(ExpressConnection.HOUSE).fill("1")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(ExpressConnection.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(ExpressConnection.BUTTON_SEND).click()
            time.sleep(2)

    @allure.title("Отправить заявку в попап 'Заявка на экспресс подключение'")
    def send_popup_express_connection_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ExpressConnection.STREET).type("Лен", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).first.click()
            time.sleep(1)
            self.page.locator(ExpressConnection.HOUSE).fill("2")
            self._click_first_available_house()
            time.sleep(1)
            self.page.locator(ExpressConnection.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(ExpressConnection.BUTTON_SEND).click()
            time.sleep(2)

    @allure.title("Перейти по случайным ссылкам городов из попапа выбора города и проверить")
    def check_random_city_links(self, desired_count: int = 20):
        with allure.step(f"Открыть попап выбора города и перейти по {desired_count} случайным ссылкам"):
            # Попап должен быть уже открыт извне
            self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).first.wait_for(state="visible", timeout=10000)

            # Получаем список всех доступных городов
            total = self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).count()
            if total == 0:
                raise AssertionError("Список городов пуст")

            target = min(desired_count, total)
            visited_cities = set()

            while len(visited_cities) < target:
                total_now = self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).count()
                # XPath индексация 1-based, поэтому randint [1, total_now]
                rand_index = random.randint(1, total_now)
                indexed_city_selector = f"{RegionChoice.RANSOM_CITY_BUTTON}[{rand_index}]"
                city_item = self.page.locator(indexed_city_selector)
                city_name = (city_item.text_content() or "").strip()
                expected_city = re.sub(r"\s*\(.*?\)\s*$", "", city_name).strip()
                city_href = city_item.get_attribute("href") or ""
                href_host = urlparse(city_href).netloc

                # Пропускаем пустые и уже посещенные
                if not city_name or city_name in visited_cities:
                    continue

                with allure.step(f"Открыть город: {city_name} (idx {rand_index}) в новой вкладке"):
                    with self.page.context.expect_page() as new_page_info:
                        city_item.click(modifiers=["Control"], force=True)  # открываем в новой вкладке
                    new_page = new_page_info.value
                    try:
                        new_page.wait_for_load_state("networkidle", timeout=15000)
                    except Exception:
                        try:
                            new_page.wait_for_load_state("load", timeout=10000)
                        except Exception:
                            pass
                    # Подстраховка: ждём появления любых известных контролов выбора региона
                    try:
                        new_page.locator(RegionChoice.NEW_REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=5000)
                    except Exception:
                        try:
                            new_page.locator(RegionChoice.TELE_REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=3000)
                        except Exception:
                            try:
                                new_page.locator(RegionChoice.REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=3000)
                            except Exception:
                                pass
                    expect(new_page).not_to_have_url("**/404")

                    # Если это сабдомен (например, abakan.mts-home.online), проверяем домен URL
                    if href_host and href_host.endswith(".mts-home.online") and href_host != "mts-home.online":
                        assert href_host in (new_page.url or ""), f"Открыт неверный домен для города {city_name}: {new_page.url}"
                    else:
                        # Иначе проверяем текст города в хедере
                        region_page = ChoiceRegionPage(page=new_page)
                        region_page.verify_region_button_text_new(expected_city)

                    new_page.close()

                visited_cities.add(city_name)
                time.sleep(1)

    @allure.title("Перейти по одному случайному городу из уже открытого попапа и проверить")
    def click_random_city_and_verify(self):
        # Попап должен быть уже открыт извне
        self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).first.wait_for(state="visible", timeout=10000)
        total_now = self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).count()
        if total_now == 0:
            raise AssertionError("Список городов пуст")

        rand_index = random.randint(1, total_now)
        indexed_city_selector = f"{RegionChoice.RANSOM_CITY_BUTTON}[{rand_index}]"
        city_item = self.page.locator(indexed_city_selector)
        city_name = (city_item.text_content() or "").strip()
        expected_city = re.sub(r"\s*\(.*?\)\s*$", "", city_name).strip()
        city_href = city_item.get_attribute("href") or ""
        href_host = urlparse(city_href).netloc

        with allure.step(f"Открыть город: {city_name} (idx {rand_index}) в новой вкладке"):
            with self.page.context.expect_page() as new_page_info:
                city_item.click(modifiers=["Control"], force=True)  # открываем в новой вкладке
            new_page = new_page_info.value
            try:
                new_page.wait_for_load_state("networkidle", timeout=15000)
            except Exception:
                try:
                    new_page.wait_for_load_state("load", timeout=10000)
                except Exception:
                    pass
            try:
                new_page.locator(RegionChoice.NEW_REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=5000)
            except Exception:
                try:
                    new_page.locator(RegionChoice.TELE_REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=3000)
                except Exception:
                    try:
                        new_page.locator(RegionChoice.REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=3000)
                    except Exception:
                        pass
            expect(new_page).not_to_have_url("**/404")

            if href_host and href_host.endswith(".mts-home.online") and href_host != "mts-home.online":
                assert href_host in (new_page.url or ""), f"Открыт неверный домен для города {city_name}: {new_page.url}"
            else:
                region_page = ChoiceRegionPage(page=new_page)
                region_page.verify_region_button_text_new(expected_city)

            new_page.close()

    @allure.title("Перейти по одному случайному городу (в той же вкладке) из уже открытого попапа и проверить")
    def click_random_city_and_verify_same_tab(self):
        # Попап должен быть уже открыт извне
        try:
            self.page.locator("xpath=//table[@class='city_list']").wait_for(state="visible", timeout=7000)
        except Exception:
            self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).first.wait_for(state="attached", timeout=7000)

        total_now = self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).count()
        if total_now == 0:
            raise AssertionError("Список городов пуст")

        rand_index = random.randint(1, total_now)
        city_item = self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).nth(rand_index - 1)
        city_name = (city_item.text_content() or "").strip()
        expected_city = re.sub(r"\s*\(.*?\)\s*$", "", city_name).strip()
        city_href = city_item.get_attribute("href") or ""
        href_host = urlparse(city_href).netloc

        with allure.step(f"Открыть город: {city_name} (idx {rand_index}) в той же вкладке"):
            city_item.scroll_into_view_if_needed()
            city_item.click(force=True)

        # Ожидаем навигацию и выполняем строгую проверку: при несоответствии тест падает
        try:
            self.page.wait_for_load_state("networkidle", timeout=15000)
        except Exception:
            try:
                self.page.wait_for_load_state("load", timeout=10000)
            except Exception:
                pass
        try:
            self.page.locator(RegionChoice.NEW_REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=5000)
        except Exception:
            try:
                self.page.locator(RegionChoice.TELE_REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=3000)
            except Exception:
                try:
                    self.page.locator(RegionChoice.REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=3000)
                except Exception:
                    pass
        expect(self.page).not_to_have_url("**/404")

        if href_host and href_host.endswith(".mts-home.online") and href_host != "mts-home.online":
            assert href_host in (self.page.url or ""), (
                f"Открыт неверный домен для города {city_name}: {self.page.url} (ожидали {href_host})"
            )
        else:
            self._verify_city_label_accepts_variants(expected_city)

    @allure.title("Перейти по одному случайному городу (в той же вкладке) из уже открытого попапа и проверить")
    def click_random_city_and_verify_same_tab_popup(self):
        # Попап должен быть уже открыт извне
        try:
            self.page.locator("xpath=//table[@class='city_list']").wait_for(state="visible", timeout=7000)
        except Exception:
            self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).first.wait_for(state="attached", timeout=7000)

        total_now = self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).count()
        if total_now == 0:
            raise AssertionError("Список городов пуст")

        rand_index = random.randint(1, total_now)
        city_item = self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).nth(rand_index - 1)
        city_name = (city_item.text_content() or "").strip()
        expected_city = re.sub(r"\s*\(.*?\)\s*$", "", city_name).strip()
        city_href = city_item.get_attribute("href") or ""
        href_host = urlparse(city_href).netloc

        with allure.step(f"Открыть город: {city_name} (idx {rand_index}) в той же вкладке"):
            city_item.scroll_into_view_if_needed()
            city_item.click(force=True)

        # Ожидаем навигацию и выполняем строгую проверку: при несоответствии тест падает
        try:
            self.page.wait_for_load_state("networkidle", timeout=15000)
        except Exception:
            try:
                self.page.wait_for_load_state("load", timeout=10000)
            except Exception:
                pass
        try:
            self.page.locator(RegionChoice.NEW_REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=5000)
        except Exception:
            try:
                self.page.locator(RegionChoice.TELE_REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=3000)
            except Exception:
                try:
                    self.page.locator(RegionChoice.REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=3000)
                except Exception:
                    pass
        expect(self.page).not_to_have_url("**/404")
        region_page = ChoiceRegionPage(page=self.page)
        region_page.close_popup_super_offer_new()

        if href_host and href_host.endswith(".mts-home.online") and href_host != "mts-home.online":
            assert href_host in (self.page.url or ""), (
                f"Открыт неверный домен для города {city_name}: {self.page.url} (ожидали {href_host})"
            )
        else:
            self._verify_city_label_accepts_variants(expected_city)

    @allure.title("Перейти по одному случайному городу (в той же вкладке) из уже открытого попапа и проверить")
    def click_random_city_and_verify_same_tab_new(self):
        # Попап должен быть уже открыт извне
        try:
            self.page.locator("xpath=//table[@class='city_list']").wait_for(state="visible", timeout=7000)
        except Exception:
            self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).first.wait_for(state="attached", timeout=7000)

        total_now = self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).count()
        if total_now == 0:
            raise AssertionError("Список городов пуст")

        rand_index = random.randint(1, total_now)
        city_item = self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).nth(rand_index - 1)
        city_name = (city_item.text_content() or "").strip()
        expected_city = re.sub(r"\s*\(.*?\)\s*$", "", city_name).strip()
        city_href = city_item.get_attribute("href") or ""
        href_host = urlparse(city_href).netloc

        with allure.step(f"Открыть город: {city_name} (idx {rand_index}) в той же вкладке"):
            city_item.scroll_into_view_if_needed()
            city_item.click(force=True)

        # Ожидаем навигацию и выполняем строгую проверку: при несоответствии тест падает
        try:
            self.page.wait_for_load_state("networkidle", timeout=15000)
        except Exception:
            try:
                self.page.wait_for_load_state("load", timeout=10000)
            except Exception:
                pass
        try:
            self.page.locator(RegionChoice.NEW_REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=5000)
        except Exception:
            try:
                self.page.locator(RegionChoice.TELE_REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=3000)
            except Exception:
                try:
                    self.page.locator(RegionChoice.REGION_CHOICE_BUTTON).first.wait_for(state="attached", timeout=3000)
                except Exception:
                    pass
        expect(self.page).not_to_have_url("**/404")

        if href_host and href_host.endswith(".mts-home.online") and href_host != "mts-home.online":
            assert href_host in (self.page.url or ""), (
                f"Открыт неверный домен для города {city_name}: {self.page.url} (ожидали {href_host})"
            )
        else:
            self._verify_city_label_accepts_variants(expected_city)

