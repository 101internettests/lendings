import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain
from locators.beeline.beeline_locators import BeelineMain, OnlineBeeline, OnlineBeelineNew
from locators.tele_two.tele_two_locators import TeleTwoMain


class BeelineOnlinePage(BasePage):
    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон в попапе предложения. Технические детали: {}".format(e))
            try:
                self.page.locator(BeelineMain.SEND_BUTTON).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку отправки в попапе предложения. Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer_dom(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP_SOME_PAGE).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон в попапе предложения (другая страница). Технические детали: {}".format(e))
            try:
                self.page.locator(BeelineMain.SEND_BUTTON).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку отправки в попапе предложения (другая страница). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.STREET_BUTTON).type("Тестовая улица", delay=100)
                self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError("Не удалось ввести/выбрать улицу в попапе. Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON).fill("1")
                self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError("Не удалось указать дом в попапе. Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP_SOME_PAGE).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон в попапе. Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.SEND_BUTTON).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку отправки в попапе. Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить заявку в попап и проверить успешность где телефон")
    def send_popup_super_offer_new_phone(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.STREET_BUTTON).type("Тестовая улица", delay=100)
                self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError("Не удалось ввести/выбрать улицу (вариант с телефоном). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON).fill("1")
                self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError("Не удалось указать дом (вариант с телефоном). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP_SIX).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (вариант с телефоном). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.SEND_BUTTON).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку отправки (вариант с телефоном). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить заявку в попап и проверить успешность где кнопка проверить адрес ПЕРВАЯ")
    def send_popup_super_offer_new_address_first(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.STREET_BUTTON_FIRST).type("Тестовая улица", delay=100)
                self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError("Не удалось ввести/выбрать улицу (кнопка 'Проверить адрес' первая). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON_FIRST).fill("1")
                self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError("Не удалось указать дом (кнопка 'Проверить адрес' первая). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (кнопка 'Проверить адрес' первая). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.CHECK_ADDRESS_BUTTON_SECOND).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку 'Проверить адрес' (первая). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить заявку в попап и проверить успешность где кнопка проверить адрес")
    def send_popup_super_offer_new_address(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.STREET_BUTTON).type("Тестовая улица", delay=100)
                self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError("Не удалось ввести/выбрать улицу (кнопка 'Проверить адрес'). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON).fill("1")
                self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError("Не удалось указать дом (кнопка 'Проверить адрес'). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP_SOME_PAGE).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (кнопка 'Проверить адрес'). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.CHECK_ADDRESS_BUTTON_FOUR).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку 'Проверить адрес' (вариант 4). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer_new_moscow(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.STREET_BUTTON_FIVE).type("Тестовая улица", delay=100)
                self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError("Не удалось ввести/выбрать улицу (Москва). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON_FIVE).fill("1")
                self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError("Не удалось указать дом (Москва). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (Москва). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.SEND_BUTTON).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку отправки (Москва). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer_new_ghome(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.STREET_BUTTON_FIVE).type("Тестовая улица", delay=100)
                self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError("Не удалось ввести/выбрать улицу (G-Home). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON_FIVE).fill("1")
                self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError("Не удалось указать дом (G-Home). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP_SEVEN).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (G-Home). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_TWO).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку отправки (G-Home). Технические детали: {}".format(e))
            time.sleep(4)

    # @allure.title("Отправить заявку в попап и проверить успешность")
    # def send_popup_super_offer_new_moscow_dom(self):
    #     with allure.step("Заполнить попап и отправить заявку"):
    #         self.page.locator(MTSHomeOnlineMain.STREET_BUTTON_FIVE).type("Тестовая улица", delay=100)
    #         self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
    #         time.sleep(1)
    #         self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON_FIVE).fill("1")
    #         self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
    #         time.sleep(1)
    #         self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP).fill("99999999999")
    #         time.sleep(1)
    #         self.page.locator(MTSHomeOnlineMain.SEND_BUTTON).click()
    #         time.sleep(4)

    @allure.title("Закрыть мешающиеся куки")
    def close_coockies(self):
        try:
            self.page.locator(BeelineMain.COOKIES_CLOSE).click()
        except Exception as e:
            raise AssertionError("Не удалось закрыть баннер cookies. Технические детали: {}".format(e))

    @allure.title("Нажать на кнопку Подключиться хедер")
    def click_connect_button(self):
        try:
            self.page.locator(BeelineMain.CONNECT_BUTTON).click()
        except Exception as e:
            raise AssertionError("Не удалось нажать кнопку 'Подключиться' в хедере. Технические детали: {}".format(e))

    @allure.title("Нажать на кнопку Подключиться футер")
    def click_connect_button_futer(self):
        try:
            self.page.locator(BeelineMain.CONNECT_BUTTON_FUTER).click()
        except Exception as e:
            raise AssertionError("Не удалось нажать кнопку 'Подключиться' в футере. Технические детали: {}".format(e))

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(BeelineMain.INPUT_STREET).fill("Тестовая")
            except Exception as e:
                raise AssertionError("Не удалось ввести улицу в попапе 'Заявка на подключение'. Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.INPUT_HOUSE).fill("1")
            except Exception as e:
                raise AssertionError("Не удалось ввести дом в попапе 'Заявка на подключение'. Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_OTHER).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон в попапе 'Заявка на подключение'. Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.INPUT_CONNECT).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку отправки в попапе 'Заявка на подключение'. Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_dom(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(BeelineMain.INPUT_STREET).fill("Тестовая")
            except Exception as e:
                raise AssertionError("Не удалось ввести улицу (домашняя страница). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.INPUT_HOUSE).fill("1")
            except Exception as e:
                raise AssertionError("Не удалось ввести дом (домашняя страница). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (домашняя страница). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.INPUT_CONNECT).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку отправки (домашняя страница). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Проверить возможность подключения билайн по вашему адресу в Москве")
    def send_popup_from_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(BeelineMain.INPUT_ADDRES).fill("Город улица дом")
            except Exception as e:
                raise AssertionError("Не удалось ввести адрес. Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_FIRST).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон. Технические детали: {}".format(e))
            time.sleep(4)
            try:
                self.page.locator(BeelineMain.CHECK_ADDRESS).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку 'Проверить адрес'. Технические детали: {}".format(e))
            time.sleep(3)

    @allure.title("Проверить возможность подключения билайн по вашему адресу в Москве")
    def send_popup_from_connection_online(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(BeelineMain.INPUT_ADDRES).fill("Город улица дом")
            except Exception as e:
                raise AssertionError("Не удалось ввести адрес (онлайн). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_OTHER).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (онлайн). Технические детали: {}".format(e))
            time.sleep(4)
            try:
                self.page.locator(BeelineMain.INPUT_CONNECT).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку отправки (онлайн). Технические детали: {}".format(e))
            time.sleep(3)

    @allure.title("Проверить возможность подключения билайн по вашему адресу в Москве")
    def send_popup_from_connection_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(BeelineMain.INPUT_ADDRES_TWO).fill("Город улица дом")
            except Exception as e:
                raise AssertionError("Не удалось ввести адрес (второй). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (второй). Технические детали: {}".format(e))
            time.sleep(4)
            try:
                self.page.locator(BeelineMain.CHECK_ADDRESS_TWO).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку 'Проверить адрес' (второй). Технические детали: {}".format(e))
            time.sleep(3)

    @allure.title("Получить название тарифа из карточки")
    def get_tariff_name(self, card_index):
        tariff_name = self.page.locator(BeelineMain.TARIFF_NAMES).nth(card_index).text_content()
        return f"Тариф: \n                              {tariff_name}\n                              "

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(BeelineMain.TARIFF_CARDS).all()

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards_new(self):
        return self.page.locator(BeelineMain.TARIFF_CARDS_SECOND).all()

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        self.page.locator(BeelineMain.TARIFF_BUTTON).nth(card_index).click()

    @allure.title("Проверить название тарифа в попапе")
    def verify_popup_tariff_name(self, expected_name):
        popup_tariff_name = self.page.locator(BeelineMain.POPUP_TARIFF_NAME)
        try:
            expect(popup_tariff_name).to_be_visible()
        except Exception as e:
            raise AssertionError("Название тарифа в попапе не отображается. Технические детали: {}".format(e))
        try:
            expect(popup_tariff_name).to_have_text(expected_name)
        except Exception as e:
            raise AssertionError(f"Название тарифа в попапе не соответствует '{expected_name}'. Технические детали: {e}")

    @allure.title("Проверить название тарифа в попапе")
    def verify_popup_tariff_name_new(self, expected_name):
        popup_tariff_name = self.page.locator(BeelineMain.POPUP_NAME)
        try:
            expect(popup_tariff_name).to_be_visible()
        except Exception as e:
            raise AssertionError("Название тарифа (новый селектор) не отображается. Технические детали: {}".format(e))
        try:
            expect(popup_tariff_name).to_have_text(expected_name)
        except Exception as e:
            raise AssertionError(f"Название тарифа (новый селектор) не соответствует '{expected_name}'. Технические детали: {e}")

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
    def check_all_links_sec(self):
        """Проверяет все ссылки в хедере и футере"""
        # Проверяем ссылки в хедере
        for name, locator in BeelineMain.HEADER_LINKS.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in BeelineMain.FOOTER_LINKS.items():
            self.check_link(locator, f"Footer: {name}")

        for name, locator in BeelineMain.OTHER_HEADERS.items():
            self.check_link(locator, f"Footer: {name}")

        for name, locator in BeelineMain.FOOTER_LINKS_SEC.items():
            self.check_link(locator, f"Footer: {name}")

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_msk(self):
        """Проверяет все ссылки в хедере и футере"""
        # Проверяем ссылки в хедере
        for name, locator in BeelineMain.HEADER_LINKS_SECOND.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in BeelineMain.FOOTER_LINKS_SECOND.items():
            self.check_link(locator, f"Footer: {name}")

        for name, locator in BeelineMain.OTHER_HEADERS.items():
            self.check_link(locator, f"Footer: {name}")

        for name, locator in BeelineMain.FOOTER_LINKS_SEC.items():
            self.check_link(locator, f"Footer: {name}")

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_msk_dom(self):
        """Проверяет все ссылки в хедере и футере"""
        # Проверяем ссылки в хедере
        for name, locator in BeelineMain.HEADER_LINKS_SECOND.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in BeelineMain.FOOTER_LINKS_SECOND.items():
            self.check_link(locator, f"Footer: {name}")

        for name, locator in BeelineMain.FOOTER_LINKS_SEC.items():
            self.check_link(locator, f"Footer: {name}")

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_online(self):
        """Проверяет все ссылки в хедере и футере"""
        # Проверяем ссылки в хедере
        for name, locator in BeelineMain.HEADER_LINKS_FOUR.items():
            self.check_link(locator, f"Header: {name}")

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_online_second(self):
        # Проверяем ссылки в футере
        for name, locator in BeelineMain.FOOTER_LINKS_FOUR.items():
            self.check_link(locator, f"Footer: {name}")

        for name, locator in BeelineMain.FOOTER_LINKS_SEC.items():
            self.check_link(locator, f"Footer: {name}")

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_online_beeline(self):
        """Проверяет все ссылки в хедере и футере"""
        # Проверяем ссылки в хедере
        for name, locator in BeelineMain.HEADER_LINKS_THIRD.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in BeelineMain.FOOTER_LINKS_THIRD.items():
            self.check_link(locator, f"Footer: {name}")

        for name, locator in BeelineMain.FOOTER_LINKS_SEC.items():
            self.check_link(locator, f"Footer: {name}")

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_online_pro(self):
        """Проверяет все ссылки в хедере и футере"""
        # Проверяем ссылки в хедере
        for name, locator in BeelineMain.HEADER_LINKS_PRO.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in BeelineMain.FOOTER_LINKS_THIRD.items():
            self.check_link(locator, f"Footer: {name}")

        for name, locator in BeelineMain.FOOTER_LINKS_SEC.items():
            self.check_link(locator, f"Footer: {name}")

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_online_tele(self):
        """Проверяет все ссылки в хедере и футере"""
        # Проверяем ссылки в хедере
        for name, locator in BeelineMain.HEADER_LINKS_TELE.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in BeelineMain.FUTER_LINKS_TELE.items():
            self.check_link(locator, f"Footer: {name}")

        # for name, locator in BeelineMain.FOOTER_LINKS_SEC.items():
        #     self.check_link(locator, f"Footer: {name}")

    @allure.title("Проверить видимость ссылок ТТК во футере")
    def check_all_links_ttk(self):
        """Проверяет, что все локаторы ссылок ТТК во футере видимы"""
        for name, locator in BeelineMain.FOOTER_LINKS_TTK.items():
            with allure.step(f"Проверить видимость элемента: {name}"):
                expect(self.page.locator(locator)).to_be_visible()

class OnlineBeelinePage(BasePage):
    @allure.title("Проверить, что попап появился и нажать на  кнопку выбора города")
    def popup_choose_city_accept(self):
        with allure.step("Проверить попап и нажать на кнопку Выбрать город"):
            try:
                expect(self.page.locator(OnlineBeeline.CHOOSE_YOUR_CITY_HEADER)).to_be_visible()
            except Exception as e:
                raise AssertionError("Попап выбора города не появился. Технические детали: {}".format(e))
            try:
                self.page.locator(OnlineBeeline.CHOOSE_YOUR_CITY_BUTTON).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку 'Выбрать город'. Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Закрыть попап Указать город")
    def popup_choose_city(self):
        try:
            self.page.locator(OnlineBeeline.CLOSE_CITY_POPUP).click()
        except Exception as e:
            raise AssertionError("Не удалось закрыть попап 'Указать город'. Технические детали: {}".format(e))

    @allure.title("Отправить заявку в форму подключить тарифы билайн в Москве")
    def send_popup_from_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(OnlineBeeline.FILL_THE_ADDRESS).fill("Город улица дом")
            except Exception as e:
                raise AssertionError("Не удалось ввести адрес (Онлайн Билайн). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_FIRST).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (Онлайн Билайн). Технические детали: {}".format(e))
            time.sleep(4)
            try:
                self.page.locator(OnlineBeeline.BUTTON_FIND_TARIFFS).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку 'Найти тарифы'. Технические детали: {}".format(e))
            time.sleep(3)

    @allure.title("Отправить  заявку вформу проверьте адрес подключения")
    def send_popup_from_connection_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(OnlineBeeline.FILL_THE_ADDRESS_SECOND).fill("Город улица дом")
            except Exception as e:
                raise AssertionError("Не удалось ввести адрес (Онлайн Билайн, второй). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (Онлайн Билайн, второй). Технические детали: {}".format(e))
            time.sleep(4)
            try:
                self.page.locator(OnlineBeeline.BUTTON_FIND_TARIFFS_SECOND).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку 'Найти тарифы' (второй). Технические детали: {}".format(e))
            time.sleep(3)

    @allure.title("Отправить  заявку вформу проверьте адрес подключения")
    def send_popup_from_connection_home(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(BeelineMain.INPUT_ADDRES_TWO).fill("Город улица дом")
            except Exception as e:
                raise AssertionError("Не удалось ввести адрес (домашняя страница, второй). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (домашняя страница, второй). Технические детали: {}".format(e))
            time.sleep(4)
            try:
                self.page.locator(BeelineMain.CHECK_ADDRESS_TWO).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку 'Проверить адрес' (домашняя страница, второй). Технические детали: {}".format(e))
            time.sleep(3)

    @allure.title("Отправить  заявку в форму проверьте адрес подключения")
    def send_popup_from_connection_home_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(BeelineMain.INPUT_STREET_SECOND).type("Тестовая улица", delay=100)
                self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError("Не удалось ввести/выбрать улицу (домашняя новая форма). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.INPUT_HOUSE_SECOND).fill("1")
                self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError("Не удалось указать дом (домашняя новая форма). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (домашняя новая форма). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.CHECK_ADDRESS_TWO).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку 'Проверить адрес' (домашняя новая форма). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить  заявку в форму проверьте адрес подключения")
    def send_popup_from_connection_home_new_MORE(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(BeelineMain.INPUT_STREET_SECOND).type("Тестовая улица", delay=100)
                self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError("Не удалось ввести/выбрать улицу (домашняя новая форма MORE). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.INPUT_HOUSE_SECOND).fill("1")
                self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError("Не удалось указать дом (домашняя новая форма MORE). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (домашняя новая форма MORE). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.CHECK_ADDRESS_TWO).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку 'Проверить адрес' (домашняя новая форма MORE). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Нажать на кнопку Подключиться футер")
    def click_connect_button_futer(self):
        self.page.locator(OnlineBeeline.CONNECT_BUTTON_FUTER).click()

    @allure.title("Отправить заявку в попап скнопки Подключиться")
    def send_popup_application_connection_dom(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(BeelineMain.INPUT_ADDRES).fill("Город улица дом")
            time.sleep(1)
            self.page.locator(BeelineMain.PHONE_INPUT_OTHER).fill("99999999999")
            time.sleep(1)
            self.page.locator(BeelineMain.INPUT_CONNECT).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап скнопки Подключиться")
    def send_popup_application_connection_home(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(BeelineMain.INPUT_ADDRES).fill("Город улица дом")
            time.sleep(1)
            self.page.locator(BeelineMain.PHONE_INPUT_FIRST).fill("99999999999")
            time.sleep(1)
            self.page.locator(BeelineMain.CHECK_ADDRESS).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап скнопки Подключиться")
    def send_popup_application_connection_home_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(BeelineMain.INPUT_STREET).type("Тестовая улица", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(BeelineMain.INPUT_HOUSE).fill("1")
            self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(BeelineMain.PHONE_INPUT_FIRST).fill("99999999999")
            time.sleep(1)
            self.page.locator(BeelineMain.CHECK_ADDRESS).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап скнопки Подключиться")
    def send_popup_application_connection_home_new_five(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(BeelineMain.INPUT_STREET_FIVE).type("Тестовая улица", delay=100)
            self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            time.sleep(1)
            self.page.locator(BeelineMain.INPUT_HOUSE_FIVE).fill("1")
            self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            time.sleep(1)
            self.page.locator(BeelineMain.PHONE_INPUT_FIVE).fill("99999999999")
            time.sleep(1)
            self.page.locator(BeelineMain.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Нажать на кнопку быстрое подключение")
    def click_button_fast_connection(self):
        try:
            self.page.locator(OnlineBeeline.BUTTON_FAST_CONNECTION).click()
        except Exception as e:
            raise AssertionError("Не удалось нажать кнопку 'Быстрое подключение'. Технические детали: {}".format(e))

    @allure.title("Нажать на кнопку Не нашли свой город")
    def click_button_dont_find_city(self):
        try:
            self.page.locator(OnlineBeeline.BUTTON_DONT_CITY).click()
        except Exception as e:
            raise AssertionError("Не удалось нажать кнопку 'Не нашли свой город'. Технические детали: {}".format(e))
        time.sleep(2)


class BeelineInternetOnlinePage(BasePage):
    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer_internet(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_OTHER).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (интернет). Технические детали: {}".format(e))
            try:
                self.page.locator(BeelineMain.SEND_BUTTON).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку отправки (интернет). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_internet(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(OnlineBeeline.CITY_INPUT).fill("Тест")
            except Exception as e:
                raise AssertionError("Не удалось ввести город (интернет). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(OnlineBeeline.STREET_HOME_INPUT).fill("1")
            except Exception as e:
                raise AssertionError("Не удалось ввести улицу/дом (интернет). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (интернет). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.INPUT_CONNECT).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку отправки (интернет). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Кликнуть на  кнопку Подключить на баннере")
    def click_button_dont_find_city(self):
        try:
            self.page.locator(OnlineBeeline.CONNECT_BANNER).click()
        except Exception as e:
            raise AssertionError("Не удалось нажать кнопку 'Подключить' на баннере. Технические детали: {}".format(e))
        time.sleep(2)

    @allure.title("Кликнуть на  кнопку Получить консультацию")
    def click_button_get_consultation(self):
        try:
            self.page.locator(OnlineBeeline.GET_CONSULTATION).click()
        except Exception as e:
            raise AssertionError("Не удалось нажать кнопку 'Получить консультацию'. Технические детали: {}".format(e))
        time.sleep(2)

    @allure.title("Закрыть попап Выгодное предложение")
    def close_popup_super_offer(self):
        try:
            self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_CLOSE_SECOND).click()
        except Exception as e:
            raise AssertionError("Не удалось закрыть попап 'Выгодное предложение' (второй). Технические детали: {}".format(e))

    @allure.title("Закрыть попап Выгодное предложение")
    def close_popup_super_offer_home(self):
        try:
            self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_CLOSE_HOME).click()
        except Exception as e:
            raise AssertionError("Не удалось закрыть попап 'Выгодное предложение' (home). Технические детали: {}".format(e))

    @allure.title("Нажать на кнопку Подключиться хедер")
    def click_connect_button_header(self):
        try:
            self.page.locator(OnlineBeeline.CONNECT_BUTTON_FUTER_FR).click()
        except Exception as e:
            raise AssertionError("Не удалось нажать кнопку 'Подключиться' (хедер). Технические детали: {}".format(e))

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_pro(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(OnlineBeeline.CITY_INPUT).fill("Тест")
            except Exception as e:
                raise AssertionError("Не удалось ввести город (PRO). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(OnlineBeeline.STREET_HOME_INPUT).fill("1")
            except Exception as e:
                raise AssertionError("Не удалось ввести улицу/дом (PRO). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_OTHER).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (PRO). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.INPUT_CONNECT).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку отправки (PRO). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_pro_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.STREET_BUTTON_THREE).type("Тестовая улица", delay=100)
                self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError("Не удалось ввести/выбрать улицу (PRO новый). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON_THREE).fill("1")
                self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError("Не удалось указать дом (PRO новый). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_OTHER).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (PRO новый). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.CHECK_ADDRESS_THREE).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку проверки адреса (PRO новый). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_pro_new_phone(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.STREET_BUTTON_THREE).type("Тестовая улица", delay=100)
                self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError("Не удалось ввести/выбрать улицу (PRO новый, телефон). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON_THREE).fill("1")
                self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError("Не удалось указать дом (PRO новый, телефон). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_FIVE).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (PRO новый, телефон). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.CHECK_ADDRESS_FOUR).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку проверки адреса (PRO новый, телефон). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Отправить заявку по кнопке Проверить адрес НОВЫЙ")
    def send_popup_application_connection_check_address(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.STREET_BUTTON_SECOND).type("Тестовая улица", delay=100)
                self.page.locator(MTSHomeOnlineMain.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError("Не удалось ввести/выбрать улицу (новая кнопка 'Проверить адрес'). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(MTSHomeOnlineMain.HOUSE_BUTTON_SECOND).fill("1")
                self.page.locator(MTSHomeOnlineMain.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError("Не удалось указать дом (новая кнопка 'Проверить адрес'). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.PHONE_INPUT_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError("Не удалось ввести телефон (новая кнопка 'Проверить адрес'). Технические детали: {}".format(e))
            time.sleep(1)
            try:
                self.page.locator(BeelineMain.CHECK_ADDRESS_TWO).click()
            except Exception as e:
                raise AssertionError("Не удалось нажать кнопку 'Проверить адрес' (новая кнопка). Технические детали: {}".format(e))
            time.sleep(4)

    @allure.title("Нажать кнопку подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        self.page.locator(OnlineBeeline.TARIFF_BUTTON).nth(card_index).click()

    @allure.title("Нажать кнопку подключить на тарифной карточке")
    def click_tariff_connect_button_new(self, card_index):
        self.page.locator(OnlineBeeline.TARIFF_BUTTON).nth(card_index).click()

    @allure.title("Нажать на кнопку Подключиться футер")
    def click_connect_button_pro(self):
        self.page.locator(OnlineBeeline.CONNECT_BUTTON_FUTER_TH).click()

    @allure.title("Новая форма для отправления заявок")
    def send_popup_application_connection_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(OnlineBeelineNew.STREET_INPUT_SECOND).type("Тестовая улица", delay=100)
            self.page.locator(OnlineBeelineNew.FIRST_CHOICE).click()
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.HOUSE_INPUT_SECOND).fill("1")
            self.page.locator(OnlineBeelineNew.FIRST_CHOICE).click()
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.PHONE_BUTTON_SECOND).fill("99999999999")
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.SEND_BUTTON_CONNECT).click()
            time.sleep(4)

    @allure.title("Новая форма для отправления заявок")
    def send_popup_application_connection_more(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(OnlineBeelineNew.STREET_INPUT_SECOND).type("Тестовая улица", delay=100)
            self.page.locator(OnlineBeelineNew.FIRST_CHOICE).click()
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.HOUSE_INPUT_SECOND).fill("1")
            self.page.locator(OnlineBeelineNew.FIRST_CHOICE).click()
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.PHONE_BUTTON_THREE).fill("99999999999")
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.SEND_BUTTON_CONNECT_ONE).click()
            time.sleep(4)

    @allure.title("Проверить возможность подключения билайн по вашему адресу в Москве")
    def send_popup_from_connection_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(OnlineBeelineNew.STREET_INPUT).type("Тестовая улица", delay=100)
            self.page.locator(OnlineBeelineNew.FIRST_CHOICE).click()
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.HOUSE_INPUT).fill("1")
            self.page.locator(OnlineBeelineNew.FIRST_CHOICE).click()
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.PHONE_BUTTON).fill("99999999999")
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.SEND_BUTTON_CONNECT_FIRST).click()
            time.sleep(4)

    @allure.title("Проверить возможность подключения билайн по вашему адресу в Москве")
    def send_popup_from_connection_new_address_se(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(OnlineBeelineNew.STREET_INPUT).type("Тестовая улица", delay=100)
            self.page.locator(OnlineBeelineNew.FIRST_CHOICE).click()
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.HOUSE_INPUT).fill("1")
            self.page.locator(OnlineBeelineNew.FIRST_CHOICE).click()
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.PHONE_BUTTON_SECOND).fill("99999999999")
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.SEND_BUTTON_CONNECT).click()
            time.sleep(4)

    @allure.title("Проверьте возможность подключения по вашему адресуе")
    def send_popup_from_connection_new_address(self):
            self.page.locator(OnlineBeelineNew.ADRESS_INPUT).type("Тестовая улица", delay=100)
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.PHONE_BUTTON).fill("99999999999")
            time.sleep(1)
            self.page.locator(OnlineBeelineNew.SEND_BUTTON_CONNECT_FIRST).click()
            time.sleep(4)