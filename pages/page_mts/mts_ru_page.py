import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain, ApplicationPopupWithName, ApplicationPopupCheckConnection, MtsRuLocators
from locators.mts.mts_home_online import FormApplicationCheckConnection, RegionChoice, MskMtsMainWeb, MtsThirdOnline


class MtsRuPage(BasePage):
    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            expect(self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP)).to_be_visible(timeout=65000)
            self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP).fill("99999999999")
            self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            time.sleep(1)
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            time.sleep(1)
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)