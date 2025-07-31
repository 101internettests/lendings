import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain
from locators.beeline.beeline_locators import BeelineMain


class BeelineOnlinePage(BasePage):
    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP).fill("99999999999")
            self.page.locator(BeelineMain.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Закрыть мешающиеся куки")
    def close_coockies(self):
        self.page.locator(BeelineMain.COOKIES_CLOSE).click()

    @allure.title("Нажать на кнопку Подключиться хедер")
    def click_connect_button(self):
        self.page.locator(BeelineMain.CONNECT_BUTTON).click()

    @allure.title("Нажать на кнопку Подключиться футер")
    def click_connect_button_futer(self):
        self.page.locator(BeelineMain.CONNECT_BUTTON_FUTER).click()

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(BeelineMain.INPUT_STREET).fill("Тестовая")
            time.sleep(1)
            self.page.locator(BeelineMain.INPUT_HOUSE).fill("1")
            time.sleep(1)
            self.page.locator(BeelineMain.PHONE_INPUT_OTHER).fill("99999999999")
            time.sleep(1)
            self.page.locator(BeelineMain.INPUT_CONNECT).click()
            time.sleep(4)

    @allure.title("Проверить возможность подключения билайн по вашему адресу в Москве")
    def send_popup_from_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(BeelineMain.INPUT_ADDRES).fill("Город улица дом")
            time.sleep(1)
            self.page.locator(BeelineMain.PHONE_INPUT_FIRST).fill("99999999999")
            time.sleep(4)
            self.page.locator(BeelineMain.CHECK_ADDRESS).click()
            time.sleep(3)

    @allure.title("Проверить возможность подключения билайн по вашему адресу в Москве")
    def send_popup_from_connection_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(BeelineMain.INPUT_ADDRES_TWO).fill("Город улица дом")
            time.sleep(1)
            self.page.locator(BeelineMain.PHONE_INPUT_SECOND).fill("99999999999")
            time.sleep(4)
            self.page.locator(BeelineMain.CHECK_ADDRESS_TWO).click()
            time.sleep(3)

    @allure.title("Получить название тарифа из карточки")
    def get_tariff_name(self, card_index):
        tariff_name = self.page.locator(BeelineMain.TARIFF_NAMES).nth(card_index).text_content()
        return f"Тариф: \n                              {tariff_name}\n                              "

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(BeelineMain.TARIFF_CARDS).all()

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        self.page.locator(BeelineMain.TARIFF_BUTTON).nth(card_index).click()

    @allure.title("Проверить название тарифа в попапе")
    def verify_popup_tariff_name(self, expected_name):
        popup_tariff_name = self.page.locator(BeelineMain.POPUP_TARIFF_NAME)
        expect(popup_tariff_name).to_be_visible()
        expect(popup_tariff_name).to_have_text(expected_name)

    @allure.title("Проверить ссылку и убедиться, что страница существует")
    def check_link(self, locator, link_name):
        """
        Упрощённая проверка ссылки: видимость, href, клик, отсутствие 404
        :param locator: локатор ссылки
        :param link_name: название ссылки для отчета
        """
        with allure.step(f"Проверка ссылки {link_name}"):
            link = self.page.locator(locator)
            expect(link).to_be_visible()
            href = link.get_attribute('href')
            if not href:
                allure.attach(f"Ссылка {link_name} не имеет атрибута href", "warning")
                return
            link.scroll_into_view_if_needed()
            time.sleep(1)
            with self.page.context.expect_page() as new_page_info:
                link.click(modifiers=["Control"])
            new_page = new_page_info.value
            new_page.wait_for_load_state("networkidle", timeout=15000)
            expect(new_page).not_to_have_url("**/404")
            new_page.close()

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_sec(self):
        """Проверяет все ссылки в хедере и футере"""
        # Проверяем ссылки в хедере
        for name, locator in BeelineMain.HEADER_LINKS.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in BeelineMain.FOOTER_LINKS.items():
            self.check_link(locator, f"Footer: {name}")

        for name, locator in BeelineMain.OTHER_HEADERS.items():
            self.check_link(locator, f"Footer: {name}")

        for name, locator in BeelineMain.FOOTER_LINKS_SEC.items():
            self.check_link(locator, f"Footer: {name}")