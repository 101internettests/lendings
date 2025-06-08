import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain, ApplicationPopupWithName, ApplicationPopupCheckConnection
from locators.mts.mts_home_online import FormApplicationCheckConnection, RegionChoice, MskMtsMainWeb


class MtsMSKHomeOnlinePage(BasePage):
    @allure.title("Нажать на баннер на главной стране")
    def click_on_banner(self):
        self.page.locator(MskMtsMainWeb.BANNER).click()

    @allure.title("Нажать на кнопку выбора региона в футере")
    def click_region_choice_button_futer(self):
        region_button = self.page.locator(MskMtsMainWeb.REGION_CHOICE_BUTTON)
        region_button.click()
        time.sleep(2)

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        # Ждем появления блока с тарифами до 1 минуты
        self.page.wait_for_selector(MTSHomeOnlineMain.TARIFF_CARDS, timeout=60000)
        # Получаем количество реально доступных кнопок подключения
        connect_buttons = self.page.locator(MTSHomeOnlineMain.TARIFF_CONNECT_BUTTONS).all()
        return connect_buttons

    @allure.title("Получить название тарифа из карточки")
    def get_tariff_name(self, card_index):
        # Ждем загрузки названий тарифов до 30 секунд
        self.page.wait_for_selector(MTSHomeOnlineMain.TARIFF_NAMES, timeout=30000)
        tariff_names = self.page.locator(MTSHomeOnlineMain.TARIFF_NAMES).all()
        if card_index < len(tariff_names):
            tariff_name = tariff_names[card_index].text_content()
            return f"Тариф: \n                              {tariff_name}\n                              "
        return None

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        # Находим все кнопки
        buttons = self.page.locator(MTSHomeOnlineMain.TARIFF_CONNECT_BUTTONS).all()
        if card_index < len(buttons):
            # Скроллим к кнопке и кликаем только если она существует
            buttons[card_index].scroll_into_view_if_needed()
            # Ждем завершения анимации скролла
            time.sleep(2)
            # Кликаем с увеличенным таймаутом
            buttons[card_index].click(timeout=30000)

    @allure.title("Проверить название тарифа в попапе")
    def verify_popup_tariff_name(self, expected_name):
        popup_tariff_name = self.page.locator(MTSHomeOnlineMain.POPUP_TARIFF_NAME)
        # Ждем появления попапа до 30 секунд
        expect(popup_tariff_name).to_be_visible(timeout=30000)
        expect(popup_tariff_name).to_have_text(expected_name)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Проверить успешность отправления заявки")
    def check_sucess(self):
        with allure.step("Проверить, что заявка отправилась"):
            expect(self.page.locator(MTSHomeOnlineMain.THANKYOU_TEXT)).to_be_visible()

    @allure.title("Закрыть страницу благодарности")
    def close_thankyou_page(self):
        self.page.locator(MTSHomeOnlineMain.CLOSE_BUTTON).click()

    @allure.title("Проверить ссылку и убедиться, что страница существует")
    def check_link(self, locator, link_name):
        """
        Проверяет ссылку и убеждается, что страница существует
        :param locator: локатор ссылки
        :param link_name: название ссылки для отчета
        """
        with allure.step(f"Проверка ссылки {link_name}"):
            link = self.page.locator(locator)
            expect(link).to_be_visible()
            link.click(modifiers=["Control"])
            new_page = self.page.context.wait_for_event("page", timeout=10000)
            new_page.wait_for_load_state("networkidle", timeout=10000)
            expect(new_page).not_to_have_url("**/404")
            new_page.close()

    @allure.title("Проверить все ссылки на странице")
    def check_all_links(self):
        """Проверяет все ссылки в хедере и футере"""
        # Проверяем ссылки в хедере
        for name, locator in MskMtsMainWeb.HEADER_LINKS.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in MTSHomeOnlineMain.FOOTER_LINKS.items():
            self.check_link(locator, f"Footer: {name}")