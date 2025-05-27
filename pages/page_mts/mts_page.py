import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain


class MtsHomeOnlinePage(BasePage):
    @allure.title("Проверить, что попап Выгодное приложение появился")
    def check_popup_super_offer(self):
        expect(self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_HEADER)).to_be_visible()
        expect(self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_TEXT)).to_be_visible()

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP).fill("99999999999")
            self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)
        with allure.step("Проверить, что заявка отправилась"):
            expect(self.page.locator(MTSHomeOnlineMain.THANKYOU_TEXT)).to_be_visible()

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def close_thankyou_page(self):
        self.page.locator(MTSHomeOnlineMain.CLOSE_BUTTON).click()

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def click_on_red_button(self):
        self.page.locator(MTSHomeOnlineMain.RED_BUTTON).click()