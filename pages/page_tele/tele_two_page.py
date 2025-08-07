import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.tele_two.tele_two_locators import TeleTwoMain


class TeleTwoPage(BasePage):
    @allure.title("Нажать на кнопку Подключиться хедер")
    def click_connect_button_header(self):
        self.page.locator(TeleTwoMain.CONNECT_HEADER_BUTTON).click()

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(TeleTwoMain.NAME_INPUT).fill("Тест")
            time.sleep(2)
            self.page.locator(TeleTwoMain.PHONE_INPUT).fill("9999999999")
            time.sleep(2)
            self.page.locator(TeleTwoMain.SEND_BUTTON).click()
            time.sleep(2)

    @allure.title("Нажать на кнопку Подключить на баннере")
    def click_connect_button_banner(self):
        self.page.locator(TeleTwoMain.BANNER_BUTTON).click()

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(TeleTwoMain.TARIFF_CARDS).all()

    @allure.title("Получить список всех тарифных карточек домашний")
    def get_tariff_cards_home(self):
        return self.page.locator(TeleTwoMain.TARIFF_MOB).all()

    @allure.title("Нажать кнопку подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        self.page.locator(TeleTwoMain.TARIFF_BUTTON).nth(card_index).click()

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_cards(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(TeleTwoMain.NAME_INPUT_TWO).fill("Тест")
            time.sleep(2)
            self.page.locator(TeleTwoMain.PHONE_INPUT_THREE).fill("9999999999")
            time.sleep(2)
            self.page.locator(TeleTwoMain.SEND_BUTTON_TWO).click()
            time.sleep(2)

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу")
    def send_popup_from_your_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(TeleTwoMain.CITY_INPUT).fill("Тестгород")
            time.sleep(1)
            self.page.locator(TeleTwoMain.STREET_INPUT).fill("Тестовая 1")
            time.sleep(1)
            self.page.locator(TeleTwoMain.PHONE_INPUT_FIRST).fill("99999999999")
            time.sleep(4)
            self.page.locator(TeleTwoMain.CHECK_THE_ADDRESS).click()
            time.sleep(3)

    @allure.title("Нажать на кнопку Подключиться футер")
    def click_connect_button_futer(self):
        self.page.locator(TeleTwoMain.CONNECT_FUTER_BUTTON).click()

    @allure.title("Нажать на кнопку Не нашли свой город")
    def click_button_dont_find_city(self):
        self.page.locator(TeleTwoMain.BUTTON_DONT_CITY).click()
        time.sleep(2)
