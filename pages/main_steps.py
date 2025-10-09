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

    @allure.title("Нажать на кнопку Изменить город")
    def button_change_city_profit(self):
        self.page.locator(Profit.BUTTON_CHANGE_CITY).click()

    @allure.title("Закрыть попап")
    def close_popup(self):
        self.page.locator(Main.CLOSE).click()

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def open_popup_for_colorful_button(self):
        self.page.locator(Profit.BUTTON_FOR_OPEN).click()

    @allure.title("Отправить заявку в попап 'Заявка на подключение'")
    def send_popup_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Connection.STREET).type("Тестовая улица", delay=100)
            time.sleep(1)
            self.page.locator(Connection.HOUSE).fill("1")
            time.sleep(1)
            self.page.locator(Connection.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Connection.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап/форму 'Проверить адрес'")
    def send_popup_checkaddress(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Checkaddress.STREET).type("Тестовая улица", delay=100)
            time.sleep(1)
            self.page.locator(Checkaddress.HOUSE).fill("1")
            time.sleep(1)
            self.page.locator(Checkaddress.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Checkaddress.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в форму 'Не определились с тарифом?'")
    def send_form_undecided(self):
        with allure.step("Заполнить форму и отправить заявку"):
            self.page.locator(Undecided.STREET).type("Тестовая улица", delay=100)
            time.sleep(1)
            self.page.locator(Undecided.HOUSE).fill("1")
            time.sleep(1)
            self.page.locator(Undecided.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Undecided.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап 'Заявка на подключение для Бизнеса'")
    def send_popup_business(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Business.FULL_ADDRESS).type("Тестовый адрес, 1", delay=100)
            time.sleep(1)
            self.page.locator(Business.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Business.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап 'Заявка на подключение для Услуги переезд'")
    def send_popup_moving(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Moving.STREET).type("Тестовая улица", delay=100)
            time.sleep(1)
            self.page.locator(Moving.HOUSE).fill("1")
            time.sleep(1)
            self.page.locator(Moving.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Moving.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап 'Заявка на экспресс подключение'")
    def send_popup_express_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ExpressConnection.STREET).type("Тестовая улица", delay=100)
            time.sleep(1)
            self.page.locator(ExpressConnection.HOUSE).fill("1")
            time.sleep(1)
            self.page.locator(ExpressConnection.PHONE).fill("99999999999")
            time.sleep(1)
            self.page.locator(ExpressConnection.BUTTON_SEND).click()
            time.sleep(4)

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
                    new_page.wait_for_load_state("networkidle", timeout=15000)
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
            new_page.wait_for_load_state("networkidle", timeout=15000)
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
        self.page.wait_for_load_state("networkidle", timeout=15000)
        expect(self.page).not_to_have_url("**/404")

        if href_host and href_host.endswith(".mts-home.online") and href_host != "mts-home.online":
            assert href_host in (self.page.url or ""), (
                f"Открыт неверный домен для города {city_name}: {self.page.url} (ожидали {href_host})"
            )
        else:
            region_page = ChoiceRegionPage(page=self.page)
            try:
                region_page.verify_region_button_text_new(expected_city)
            except:
                # Если первой кнопки нет или она не кликабельна, продолжаем выполнение
                pass
            region_page.verify_region_button_text_tele(expected_city)

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
        self.page.wait_for_load_state("networkidle", timeout=15000)
        expect(self.page).not_to_have_url("**/404")
        region_page = ChoiceRegionPage(page=self.page)
        region_page.close_popup_super_offer_new()

        if href_host and href_host.endswith(".mts-home.online") and href_host != "mts-home.online":
            assert href_host in (self.page.url or ""), (
                f"Открыт неверный домен для города {city_name}: {self.page.url} (ожидали {href_host})"
            )
        else:
            region_page = ChoiceRegionPage(page=self.page)
            try:
                region_page.verify_region_button_text_new(expected_city)
            except:
                # Если первой кнопки нет или она не кликабельна, продолжаем выполнение
                pass
            region_page.verify_region_button_text_tele(expected_city)

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
        self.page.wait_for_load_state("networkidle", timeout=15000)
        expect(self.page).not_to_have_url("**/404")

        if href_host and href_host.endswith(".mts-home.online") and href_host != "mts-home.online":
            assert href_host in (self.page.url or ""), (
                f"Открыт неверный домен для города {city_name}: {self.page.url} (ожидали {href_host})"
            )
        else:
            region_page = ChoiceRegionPage(page=self.page)
            try:
                region_page.verify_region_button_text_new(expected_city)
            except:
                # Если первой кнопки нет или она не кликабельна, продолжаем выполнение
                pass
            region_page.verify_region_button_text_new(expected_city)

