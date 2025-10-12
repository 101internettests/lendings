import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain
from locators.mts.mts_home_online import FormApplicationCheckConnection, RegionChoice, MskMtsMainWeb, ApplicationPopupWithName
from locators.mts.mts_home_online_second import MTSHomeOnlineSecondMain, ApplicationPopupWithNameS, FormApplicationCheckConnectionSecond
from locators.mts.mts_home_online_second import ApplicationPopupCheckConnectionSecond, RegionChoiceSecond


class MtsHomeOnlineSecondPage(BasePage):
    @allure.title("Проверить, что попап Выгодное приложение появился")
    def check_popup_super_offer(self):
        # expect(self.page.locator(MTSHomeOnlineSecondMain.SUPER_OFFER_HEADER)).to_be_visible()
        expect(self.page.locator(MTSHomeOnlineSecondMain.SUPER_OFFER_TEXT)).to_be_visible(timeout=65000)

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            expect(self.page.locator(MTSHomeOnlineSecondMain.INPUT_OFFER_POPUP)).to_be_visible(timeout=65000)
            self.page.locator(MTSHomeOnlineSecondMain.ADDRESS_INPUT).fill("Тестоулица")
            self.page.locator(MTSHomeOnlineSecondMain.INPUT_OFFER_POPUP).fill("99999999999")
            self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)

    @allure.title("Нажать на кнопку Подключить в хедере")
    def click_connect_button(self):
        self.page.locator(MTSHomeOnlineSecondMain.CONNECT_BUTTON).click()

    @allure.title("Нажать на кнопку Проверить адрес из футера")
    def click_check_address_button_futer(self):
        self.page.locator(MTSHomeOnlineSecondMain.CHECK_ADDRESS_BUTTON_FUTER).click()

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.ADDRESS_INPUT_FIVE).fill("Тестоадрес")
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithNameS.PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title(
        "Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве в конце страницы")
    def send_popup_application_check_connection_near_futer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(FormApplicationCheckConnection.ADDRESS_THIRD).fill("Тестимя")
            time.sleep(3)
            self.page.locator(FormApplicationCheckConnectionSecond.PHONE_INPUT_SECOND).fill("99999999999")
            time.sleep(3)
            self.page.locator(FormApplicationCheckConnection.CHECK_ADDRESS_BUTTON_SECOND).click()
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.ADDRESS_INPUT_FIVE).fill("Тестоадрес")
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithNameS.PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Проверьте возможность подключения по вашему адресу")
    def send_popup_application_connection_your_address(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupCheckConnectionSecond.ADDRESS_INPUT_FOUR).fill("Тестимя")
            time.sleep(2)
            self.page.locator(ApplicationPopupCheckConnectionSecond.PHONE_INPUT_SECOND).fill("99999999999")
            time.sleep(2)
            self.page.locator(ApplicationPopupCheckConnectionSecond.CHECK_ADDRESS_BUTTON).click()
            time.sleep(4)

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
                with allure.step(f"Ссылка {link_name} не имеет атрибута href"):
                    pass
                return
            link.scroll_into_view_if_needed()
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
        for name, locator in ApplicationPopupCheckConnectionSecond.HEADER_LINKS.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in ApplicationPopupCheckConnectionSecond.FOOTER_LINKS.items():
            self.check_link(locator, f"Footer: {name}")

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button(self):
        region_button = self.page.locator(RegionChoice.REGION_CHOICE_BUTTON_FUTER)
        region_button.click()
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button_new(self):
        region_button = self.page.locator(RegionChoice.REGION_CHOICE_BUTTON_FUTER)
        region_button.click()
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button_new_two(self):
        region_button = self.page.locator(RegionChoice.HEADER_BUTTON_NEW)
        region_button.click()
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в футере")
    def click_region_choice_button_futer(self):
        region_button = self.page.locator(RegionChoiceSecond.REGION_CHOICE_BUTTON_FUTER)
        region_button.click()
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в футере")
    def click_region_choice_button_futer_new(self):
        region_button = self.page.locator(RegionChoiceSecond.NEW_HEADER_BUTTON)
        region_button.click()
        time.sleep(2)

    @allure.title("Отправить заявку в форму Не нашли свой город?")
    def send_form_dont_find_city(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(RegionChoice.FORM_CITY).fill("Тестгород")
            self.page.locator(RegionChoiceSecond.PHONE_INPUT).fill("99999999999")
            self.page.locator(RegionChoiceSecond.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(MTSHomeOnlineMain.STREET_BUTTON_FIVE).type("Тестовая улица", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON_FIVE).fill("1")
            self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP_SIX).fill("99999999999")
            time.sleep(1)
            self.page.locator(MTSHomeOnlineMain.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(MTSHomeOnlineMain.STREET_BUTTON).type("Тестовая улица", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON).fill("1")
            self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(MTSHomeOnlineMain.PHONE_INPUT_FIVE).fill("99999999999")
            time.sleep(1)
            self.page.locator(MTSHomeOnlineMain.CHECK_ADDRESS_BUTTON_FOUR).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_three(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(MTSHomeOnlineMain.STREET_BUTTON_THREE).type("Тестовая улица", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON_THREE).fill("1")
            self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP_SOME_PAGE).fill("99999999999")
            time.sleep(1)
            self.page.locator(MTSHomeOnlineMain.CHECK_ADDRESS_BUTTON_THREE).click()
            time.sleep(4)