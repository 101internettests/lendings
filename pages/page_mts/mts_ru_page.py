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
            try:
                expect(self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP)).to_be_visible(timeout=65000)
            except Exception:
                raise AssertionError(
                    "Поле телефона в попапе 'Выгодное предложение' не появилось за ожидаемое время.\n"
                    "Возможно, попап не отрисовался или перекрыт другим элементом."
                )
            try:
                self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Выгодное предложение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Отправить' в попапе 'Выгодное предложение'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести имя в форме 'Заявка на подключение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(1)
            try:
                self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в форме 'Заявка на подключение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(1)
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в форме 'Заявка на подключение'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)