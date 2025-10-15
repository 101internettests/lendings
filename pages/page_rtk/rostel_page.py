import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.rtk.rostel_locators import Rostelecom


class RostelecomPage(BasePage):
    @allure.title("Нажать на плавающую фиолетовую кнопку с телефоном в правом нижнем углу")
    def click_on_purple_button(self):
        self.page.locator(Rostelecom.CONNECT_PURPLE_BUTTON).click()

    @allure.title("Закрыть всплыващий попап")
    def close_popup(self):
        self.page.locator(Rostelecom.CLOSE_POPUP).click()

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            expect(self.page.locator(Rostelecom.PHONE_BUTTON)).to_be_visible(timeout=65000)
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

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_online(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT).fill("1")
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_FOUR).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.SEND_BUTTON_CONNECT).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап скнопки Подключиться")
    def send_popup_application_connection_home_new_four(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT_FOUR).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT_FOUR).fill("1")
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с кнопки Подключиться для ТВ")
    def send_popup_application_connection_home_new_tv(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT_FOUR).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT_FOUR).fill("1")
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_FOUR).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап скнопки Подключиться")
    def send_popup_application_connection_home_new_five(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.INPUT_STREET_FIVE).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.INPUT_HOUSE_FIVE).fill("1")
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап скнопки Подключиться")
    def send_popup_application_connection_rtk(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.INPUT_STREET_FIVE).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.INPUT_HOUSE_FIVE).fill("1")
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_SIX).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)

    @allure.title("Нажать на кнопку Подключиться с баннера")
    def click_connect_banner_button(self):
        self.page.locator(Rostelecom.CONNECTION_BUTTON).click()

    @allure.title("Нажать на кнопку Подключиться с середины страницы")
    def click_connect_banner_button_middle(self):
        self.page.locator(Rostelecom.CONNECTION_BUTTON_MIDDLE).click()

    @allure.title("Нажать на кнопку Не определились с тарифом?")
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

    @allure.title("Проверить возможность подключения около хедера")
    def send_popup_application_connection_online_rtk(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT_FIRST).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT_FIRST).fill("1")
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_FIRST).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.BUTTON_CHECK_CONNECTION_RTK).click()
            time.sleep(4)

    @allure.title("Проверить возможность подключения около хедера")
    def send_popup_application_connection_online_rtk_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT_SECOND).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT_SECOND).fill("1")
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_SECOND).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.BUTTON_CHECK_CONNECTION_RTK_SECOND).click()
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

    @allure.title("попап не определились с тарифом")
    def send_popup_application_popup_dont_tariff(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.NAME_INPUT_FIRST).fill("Тест")
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_SECOND).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.CHECK_THE_ADDRESS_BUTTON_SECOND).click()
            time.sleep(4)

    @allure.title("Проверить возможность подключения в форме подключить")
    def send_popup_application_connection_futer_dom(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT_SECOND).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT_SECOND).fill("1")
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_THREE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.SEND_BUTTON_CONNECT).click()
            time.sleep(4)

    @allure.title("Проверить возможность подключения в форме подключить")
    def send_popup_application_connection_futer_tv(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT_SECOND).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT_SECOND).fill("1")
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_SECOND).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.SEND_BUTTON_CONNECT).click()
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

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request_online(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT_FOUR).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT).type("1", delay=100)
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.NAME_INPUT).fill("Тест")
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.SEND_BUTTON_SECOND).click()
            time.sleep(4)

    @allure.title("Отправить заявку на подключение с карточек дом")
    def send_tariff_connection_request_dom(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT).type("Тестовая улица", delay=100)
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

    @allure.title("Отправить заявку на подключение с карточек дом")
    def send_tariff_connection_request_tv(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(Rostelecom.STREET_INPUT).type("Тестовая улица", delay=100)
            self.page.locator(Rostelecom.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(Rostelecom.HOUSE_INPUT).type("1", delay=100)
            self.page.locator(Rostelecom.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(Rostelecom.NAME_INPUT).fill("Тест")
            time.sleep(1)
            self.page.locator(Rostelecom.PHONE_BUTTON_THREE).fill("99999999999")
            time.sleep(1)
            self.page.locator(Rostelecom.SEND_BUTTON_SECOND).click()
            time.sleep(4)

    @allure.title("Получить название тарифа из карточки")
    def get_tariff_name(self, card_index):
        tariff_name = self.page.locator(Rostelecom.TARIFF_NAMES).nth(card_index).text_content()
        return f"Тариф: \n                              {tariff_name}\n                              "

    @allure.title("Получить название тарифа из карточки")
    def get_tariff_name_dom(self, card_index):
        tariff_name = self.page.locator(Rostelecom.TARIFF_NAMES_DOM).nth(card_index).text_content()
        return f"Тариф: \n                              {tariff_name}\n                              "

    @allure.title("Проверить название тарифа в попапе")
    def verify_popup_tariff_name(self, expected_name):
        popup_tariff_name = self.page.locator(Rostelecom.POPUP_TARIFF_NAME)
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
        try:
            # Проверяем ссылки в хедере
            for name, locator in Rostelecom.HEADER_LINKS.items():
                self.check_link(locator, f"Header: {name}")

            # Проверяем ссылки в футере
            for name, locator in Rostelecom.FOOTER_LINKS.items():
                self.check_link(locator, f"Footer: {name}")
            for name, locator in Rostelecom.FOOTER_LINKS_SECOND.items():
                self.check_link(locator, f"Footer: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_online(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in Rostelecom.HEADER_LINKS_SECOND.items():
                self.check_link(locator, f"Header: {name}")

            # Проверяем ссылки в футере
            for name, locator in Rostelecom.FOOTER_LINKS_THIRD.items():
                self.check_link(locator, f"Footer: {name}")
            for name, locator in Rostelecom.FOOTER_LINKS_FOUR.items():
                self.check_link(locator, f"Footer: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_rtk(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in Rostelecom.HEADER_LINKS_THIRD.items():
                self.check_link(locator, f"Header: {name}")

            # Проверяем ссылки в футере
            for name, locator in Rostelecom.FOOTER_LINKS_RTK.items():
                self.check_link(locator, f"Footer: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_rtk_home(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in Rostelecom.HEADER_LINKS_FOUR.items():
                self.check_link(locator, f"Header: {name}")

            # Проверяем ссылки в футере
            for name, locator in Rostelecom.FOOTER_LINKS_RTK.items():
                self.check_link(locator, f"Footer: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button(self):
        region_button = self.page.locator(Rostelecom.REGION_CHOICE_BUTTON_FUTER)
        region_button.click()
        time.sleep(2)