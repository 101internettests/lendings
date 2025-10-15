import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mega.mega_premium_locators import ThankYouPage, CheckConnectApplicationForms, ClarifyPopUp, MainPageLocs
from locators.mega.mega_premium_locators import ApplicationConnection


class MegaPremiumOnline(BasePage):
    @allure.title("Закрыть страницу благодарности")
    def close_thankyou_page(self):
        self.page.locator(ThankYouPage.CRUSIFIX_CLOSE).click()

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу первый")
    def send_popup_application_check_connection_first(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(CheckConnectApplicationForms.FIRST_CITY).fill("Тестгород")
            time.sleep(2)
            self.page.locator(CheckConnectApplicationForms.FIRST_ADDRESS).fill("Тестулица")
            time.sleep(2)
            self.page.locator(CheckConnectApplicationForms.FIRST_PHONE_INPUT).fill("99999999999")
            time.sleep(1)
            self.page.locator(CheckConnectApplicationForms.FIRST_CHECK_ADDRESS_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу второй")
    def send_popup_application_check_connection_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(CheckConnectApplicationForms.SECOND_CITY).fill("Тестгород")
            time.sleep(2)
            self.page.locator(CheckConnectApplicationForms.SECOND_ADDRESS).fill("Тестулица")
            time.sleep(2)
            self.page.locator(CheckConnectApplicationForms.SECOND_PHONE_INPUT).fill("99999999999")
            time.sleep(1)
            self.page.locator(CheckConnectApplicationForms.SECOND_CHECK_ADDRESS_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в форму Не определились с тарифом?")
    def send_popup_application_tariff_form(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(CheckConnectApplicationForms.TARIFF_CITY).fill("Тестгород")
            time.sleep(2)
            self.page.locator(CheckConnectApplicationForms.TARIFF_ADDRESS).fill("Тестулица")
            time.sleep(2)
            self.page.locator(CheckConnectApplicationForms.TARIFF_PHONE_INPUT).fill("99999999999")
            time.sleep(1)
            self.page.locator(CheckConnectApplicationForms.TARIFF_CHECK_ADDRESS_BUTTON).click()

    @allure.title("Кликнуть по кнопке Уточнить")
    def click_clarify_button(self):
        self.page.locator(ClarifyPopUp.CLARIFY_BUTTON).click()

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(MainPageLocs.TARIFFS_CARDS).all()

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        self.page.locator(MainPageLocs.TARIFF_CONNECT_BUTTONS).nth(card_index).click()

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
    def check_header_links(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in MainPageLocs.HEADER_LINKS.items():
                self.check_link(locator, f"Header: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Проверить все ссылки на странице")
    def check_footer_links(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in MainPageLocs.POPUP_LINKS.items():
                self.check_link(locator, f"Header: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Проверить все ссылки на странице")
    def check_popup_links(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in MainPageLocs.POPUP_LINKS.items():
                self.check_link(locator, f"Header: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Проверить все ссылки на странице")
    def check_popup_links_moskva(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in MainPageLocs.MEGA_HEADER.items():
                self.check_link(locator, f"Header: {name}")

            for name, locator in MainPageLocs.MEGA_FUTER.items():
                self.check_link(locator, f"Header: {name}")

            for name, locator in MainPageLocs.POPUP_LINKS.items():
                self.check_link(locator, f"Header: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Нажать на кнопку Не смогли найти город")
    def click_button_dont_find_city(self):
        self.page.locator(MainPageLocs.BUTTON_DONT_FIND_BUTTON).click()
        time.sleep(2)

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            expect(self.page.locator(CheckConnectApplicationForms.SECOND_PHONE_INPUT)).to_be_visible(timeout=65000)
            self.page.locator(CheckConnectApplicationForms.SECOND_PHONE_INPUT).fill("99999999999")
            self.page.locator(CheckConnectApplicationForms.POPUP_SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationConnection.NAME_INPUT).fill("Тестимя")
            time.sleep(1)
            self.page.locator(CheckConnectApplicationForms.TARIFF_PHONE_INPUT).fill("99999999999")
            time.sleep(1)
            self.page.locator(ApplicationConnection.POPUP_SEND_BUTTON).click()
            time.sleep(4)


class MegaHomeInternet(BasePage):

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу первый")
    def send_popup_application_check_connection_first(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(CheckConnectApplicationForms.HOME_MEGA_CITY).fill("Тестулица")
            time.sleep(2)
            self.page.locator(CheckConnectApplicationForms.FIRST_PHONE_INPUT).fill("99999999999")
            time.sleep(1)
            self.page.locator(CheckConnectApplicationForms.FIRST_CHECK_ADDRESS_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationConnection.NAME_INPUT).fill("Тестимя")
            time.sleep(1)
            self.page.locator(CheckConnectApplicationForms.TARIFF_PHONE_INPUT).fill("99999999999")
            time.sleep(1)
            self.page.locator(ApplicationConnection.POPUP_SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(MainPageLocs.TARIFFS_CARDS_TWO).all()

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        self.page.locator(MainPageLocs.TARIFF_CONNECT_BUTTONS_TWO).nth(card_index).click()

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationConnection.NAME_INPUT).fill("Тестимя")
            self.page.locator(CheckConnectApplicationForms.TARIFF_PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationConnection.POPUP_SEND_BUTTON).click()
            time.sleep(4)
