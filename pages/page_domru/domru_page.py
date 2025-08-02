import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.domru.domru_locators import LocationPopup, PopUps, CardsPopup


class DomRuClass(BasePage):
    @allure.title("Ответить в всплывашке, что нахожусь в Москве")
    def close_popup_location(self):
        self.page.locator(LocationPopup.YES_BUTTON).click()

    @allure.title("Ответить в всплывашке, что нахожусь не в Москве")
    def choose_msk_location(self):
        self.page.locator(LocationPopup.NO_BUTTON).click()

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(LocationPopup.INPUT_OFFER_POPUP).fill("99999999999")
            self.page.locator(LocationPopup.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def close_thankyou_page(self):
        self.page.locator(LocationPopup.CLOSE_BUTTON).click()

    @allure.title("Отправить заявку в попап Подключите стабильный интернет в Москве")
    def send_popup_from_banner(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(PopUps.INPUT_NUM_POPUP).fill("99999999999")
            self.page.locator(PopUps.BUTTON_NEW_INTERNET).click()
            time.sleep(3)

    @allure.title("Отправить заявку в попап Бесплатный тест-драйв роутера на 14 дней")
    def send_popup_free_tes_drive(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(PopUps.INPUT_NUM_POPUP_THR).fill("99999999999")
            self.page.locator(PopUps.BUTTON_CONNECT).click()
            time.sleep(3)

    @allure.title("Отправить заявку в попап Тест-драйв скорости до 800 Мбит/с на 3 месяца")
    def send_popup_tes_drive_three_months(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(PopUps.INPUT_NUM_POPUP_FOU).fill("99999999999")
            self.page.locator(PopUps.BUTTON_CONNECT_SEC).click()
            time.sleep(3)

    @allure.title("Отправить заявку в попап Попробуйте скоростной безлимитный интернет")
    def send_popup_speed_inter(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(PopUps.INPUT_NUM_POPUP_FIV).fill("99999999999")
            self.page.locator(PopUps.BUTTON_CONNECT_THI).click()
            time.sleep(3)

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_check_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(PopUps.INPUT_ADDRESS).fill("Тестоадрес")
            self.page.locator(PopUps.INPUT_NUM_POPUP_SEC).fill("99999999999")
            self.page.locator(PopUps.BUTTON_CHECK_ADDRESS).click()
            time.sleep(4)

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(LocationPopup.TARIFF_CARDS).all()

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        self.page.locator(LocationPopup.TARIFF_CONNECT_BUTTONS).nth(card_index).click()

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(CardsPopup.INPUT_NAME).fill("Тестимя")
            self.page.locator(CardsPopup.INPUT_NUM).fill("99999999999")
            self.page.locator(CardsPopup.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(CardsPopup.INPUT_NAME).fill("Тестимя")
            self.page.locator(PopUps.INPUT_NUM_POPUP_FOU).fill("99999999999")
            self.page.locator(CardsPopup.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(CardsPopup.INPUT_NAME).fill("Тестимя")
            self.page.locator(PopUps.INPUT_NUM_POPUP_FOU).fill("99999999999")
            self.page.locator(CardsPopup.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Нажать на кнопку Подключить интернет первую")
    def open_popup_connection(self):
        self.page.locator(PopUps.BUTTON_CONNECT_INTERNET).click()

    @allure.title("Нажать на кнопку Подключить интернет вторую")
    def open_popup_connection_second(self):
        self.page.locator(PopUps.BUTTON_CONNECT_INTERNET_SECOND).click()

    @allure.title("Нажать на кнопку Подключить интернет третью")
    def open_popup_connection_third(self):
        self.page.locator(PopUps.BUTTON_CONNECT_INTERNET_THIRD).click()

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
    def check_all_links(self):
        """Проверяет все ссылки в хедере и футере"""
        # Проверяем ссылки в хедере
        for name, locator in LocationPopup.HEADER_LINKS.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in LocationPopup.FOOTER_LINKS.items():
            self.check_link(locator, f"Footer: {name}")

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_sec(self):
        """Проверяет все ссылки в хедере и футере"""
        # Проверяем ссылки в хедере
        for name, locator in LocationPopup.HEADER_LINKS.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in LocationPopup.FOOTER_LINKS_SEC.items():
            self.check_link(locator, f"Footer: {name}")

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def close_popup(self):
        self.page.locator(LocationPopup.CLOSE_POPUP).click()

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(LocationPopup.NAME_INPUT).fill("Тестимя")
            time.sleep(1)
            self.page.locator(PopUps.INPUT_NUM_POPUP_SIX).fill("99999999999")
            time.sleep(1)
            self.page.locator(LocationPopup.BUTTON_SEND).click()
            time.sleep(4)

    @allure.title("Нажать на лого на главной странице и проверить")
    def click_on_logo(self):
        self.page.locator(LocationPopup.MAIN_LOGO).click()