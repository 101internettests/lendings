import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain, ApplicationPopupWithName, ApplicationPopupCheckConnection
from locators.mts.mts_home_online import FormApplicationCheckConnection, RegionChoice, MskMtsMainWeb
from locators.mts.internet_mts_home import InternetMTSHomeOnlineMain


class MtsInternetHomeOnlinePage(BasePage):
    @allure.title("Проверить, что попап Выгодное приложение появился")
    def check_popup_super_offer(self):
        # expect(self.page.locator(InternetMTSHomeOnlineMain.SUPER_OFFER_HEADER)).to_be_visible()
        expect(self.page.locator(InternetMTSHomeOnlineMain.SUPER_OFFER_TEXT)).to_be_visible()

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP_SOME_PAGE).fill("99999999999")
            self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)

    @allure.title("Нажать и закрыть куки")
    def click_on_accept(self):
        self.page.locator(InternetMTSHomeOnlineMain.ACCEPT_COOKIES).click()

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT_OTHER).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Проверьте возможность подключения по вашему адресу")
    def send_popup_application_connection_your_address(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupCheckConnection.ADDRESS_INPUT_SECOND).fill("Тестоулица111111")
            self.page.locator(ApplicationPopupCheckConnection.PHONE_INPUT_SECOND).fill("99999999999")
            self.page.locator(ApplicationPopupCheckConnection.CHECK_ADDRESS_BUTTON_SECOND).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Проверьте возможность подключения по вашему адресу")
    def send_popup_application_connection_your_address_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupCheckConnection.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupCheckConnection.PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Нажать на баннер на главной стране")
    def click_on_banner(self):
        self.page.locator(InternetMTSHomeOnlineMain.BANNER).click()

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT_OTHER).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_internet_online(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
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
        for name, locator in InternetMTSHomeOnlineMain.HEADER_LINKS.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in InternetMTSHomeOnlineMain.FOOTER_LINKS.items():
            self.check_link(locator, f"Footer: {name}")

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button(self):
        region_button = self.page.locator(RegionChoice.REGION_CHOICE_BUTTON_FUTER)
        region_button.click()
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button_new(self):
        region_button = self.page.locator(RegionChoice.NEW_REGION_CHOICE_BUTTON)
        region_button.click()
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в футере")
    def click_region_choice_button_futer(self):
        region_button = self.page.locator(RegionChoice.REGION_CHOICE_BUTTON_THREE)
        region_button.click()
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button_header_new(self):
        region_button = self.page.locator(RegionChoice.NEW_REGION_CHOICE_BUTTON_HEADER)
        region_button.click()
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в футере")
    def click_region_choice_button_futer_new(self):
        region_button = self.page.locator(RegionChoice.NEW_REGION_CHOICE_BUTTON_FUTER)
        region_button.click()
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в футере МТС")
    def click_region_choice_button_futer_msk_new(self):
        region_button = self.page.locator(RegionChoice.FUTER_MTS_NEW)
        region_button.click()
        time.sleep(2)