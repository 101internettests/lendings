import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.rtk.rostel_locators import Rostelecom


class RostelecomPage(BasePage):
    @allure.title("Нажать на плавающую фиолетовую кнопку с телефоном в правом нижнем углу")
    def click_on_purple_button(self):
        self.page.locator(Rostelecom.CONNECT_PURPLE_BUTTON).click()

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.PHONE_BUTTON).fill("99999999999")
            self.page.locator(Rostelecom.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT).fill("1")
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_THREE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.SEND_BUTTON_CONNECT).click()
            time.sleep(4)

    @allure.title("Нажать на кнопку Подключиться с баннера")
    def click_connect_banner_button(self):
        self.page.locator(Rostelecom.CONNECTION_BUTTON).click()

    @allure.title("Нажать на кнопку Подключиться с середины страницы")
    def click_connect_banner_button_middle(self):
        self.page.locator(Rostelecom.CONNECTION_BUTTON_MIDDLE).click()

    @allure.title("Проверить возможность подключения около хедера")
    def send_popup_application_connection_header(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT_FIRST).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT_FIRST).fill("1")
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_FIRST).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.CHECK_THE_ADDRESS_BUTTON).click()
            time.sleep(4)

    @allure.title("Проверить возможность подключения около футера")
    def send_popup_application_connection_futer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT_SECOND).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT_SECOND).fill("1")
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_SECOND).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.CHECK_THE_ADDRESS_BUTTON_SECOND).click()
            time.sleep(4)

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(Rostelecom.TARIFF_CARDS).all()

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        self.page.locator(Rostelecom.TARIFF_CONNECT_BUTTONS).nth(card_index).click()

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT_FOUR).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT).type("1", delay=100)
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.NAME_INPUT).fill("Тест")
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_FOUR).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.SEND_BUTTON_SECOND).click()
            time.sleep(4)

    @allure.title("Получить название тарифа из карточки")
    def get_tariff_name(self, card_index):
        tariff_name = self.page.locator(Rostelecom.TARIFF_NAMES).nth(card_index).text_content()
        return f"Тариф: \n                              {tariff_name}\n                              "

    @allure.title("Проверить название тарифа в попапе")
    def verify_popup_tariff_name(self, expected_name):
        popup_tariff_name = self.page.locator(Rostelecom.POPUP_TARIFF_NAME)
        expect(popup_tariff_name).to_be_visible()
        expect(popup_tariff_name).to_have_text(expected_name)