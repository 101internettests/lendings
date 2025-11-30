import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain, ApplicationPopupWithName
from locators.mts.mts_home_online import MskMtsMainWeb


class MtsMSKHomeOnlinePage(BasePage):
    @allure.title("Нажать на баннер на главной стране")
    def click_on_banner(self):
        try:
            self.page.locator(MskMtsMainWeb.BANNER).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать на баннер на главной странице.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
            )

    @allure.title("Нажать на кнопку выбора региона в футере")
    def click_region_choice_button_futer(self):
        region_button = self.page.locator(MskMtsMainWeb.REGION_CHOICE_BUTTON)
        try:
            region_button.click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку выбора региона в футере.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        # Ждем появления блока с тарифами до 1 минуты
        try:
            self.page.wait_for_selector(MTSHomeOnlineMain.TARIFF_CARDS, timeout=60000)
            connect_buttons = self.page.locator(MTSHomeOnlineMain.TARIFF_CONNECT_BUTTONS).all()
            return connect_buttons
        except Exception:
            raise AssertionError(
                "Не удалось получить список тарифных карточек.\n"
                "Возможно, карточки не отрисовались или изменился селектор."
            )

    @allure.title("Получить название тарифа из карточки")
    def get_tariff_name(self, card_index):
        # Ждем загрузки названий тарифов до 30 секунд
        try:
            self.page.wait_for_selector(MTSHomeOnlineMain.TARIFF_NAMES, timeout=30000)
            tariff_names = self.page.locator(MTSHomeOnlineMain.TARIFF_NAMES).all()
            if card_index < len(tariff_names):
                tariff_name = (tariff_names[card_index].text_content() or "").strip()
                if not tariff_name:
                    raise AssertionError("Название тарифа пустое.")
                return f"Тариф: \n                              {tariff_name}\n                              "
            raise AssertionError("Указанный индекс карточки тарифа отсутствует на странице.")
        except AssertionError:
            raise
        except Exception:
            raise AssertionError(
                f"Не удалось получить название тарифа для карточки #{card_index}.\n"
                "Возможно, элемент недоступен, скрыт или изменился селектор."
            )

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        # Находим все кнопки
        try:
            buttons = self.page.locator(MTSHomeOnlineMain.TARIFF_CONNECT_BUTTONS).all()
            if card_index < len(buttons):
                buttons[card_index].scroll_into_view_if_needed()
                time.sleep(2)
                buttons[card_index].click(timeout=30000)
            else:
                raise AssertionError("Кнопка 'Подключить' с указанным индексом отсутствует.")
        except AssertionError:
            raise
        except Exception:
            raise AssertionError(
                f"Не удалось нажать кнопку 'Подключить' на карточке тарифа #{card_index}.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
            )

    @allure.title("Проверить название тарифа в попапе")
    def verify_popup_tariff_name(self, expected_name):
        popup_tariff_name = self.page.locator(MTSHomeOnlineMain.POPUP_TARIFF_NAME)
        # Ждем появления попапа до 30 секунд
        try:
            expect(popup_tariff_name).to_be_visible(timeout=30000)
        except Exception:
            raise AssertionError(
                "Название тарифа в попапе не отображается.\n"
                "Возможно, попап не открылся или изменился селектор."
            )
        try:
            expect(popup_tariff_name).to_have_text(expected_name)
        except Exception:
            raise AssertionError(
                f"Название тарифа в попапе не соответствует ожидаемому '{expected_name}'.\n"
                "Возможно, данные тарифа изменились."
            )

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupWithName.ADDRESS_INPUT).fill("Тестоадрес")
            except Exception:
                raise AssertionError("Не удалось ввести адрес в форме тарифа.")
            try:
                self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError("Не удалось ввести имя в форме тарифа.")
            try:
                self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон в форме тарифа.")
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку отправки в форме тарифа.")
            time.sleep(4)

    @allure.title("Проверить успешность отправления заявки")
    def check_sucess(self):
        with allure.step("Проверить, что заявка отправилась"):
            try:
                expect(self.page.locator(MTSHomeOnlineMain.THANKYOU_TEXT)).to_be_visible()
            except Exception:
                raise AssertionError(
                    "Страница благодарности не появилась после отправки заявки."
                )

    @allure.title("Закрыть страницу благодарности")
    def close_thankyou_page(self):
        try:
            self.page.locator(MTSHomeOnlineMain.CLOSE_BUTTON).click()
        except Exception:
            raise AssertionError(
                "Не удалось закрыть страницу благодарности.\n"
                "Возможно, кнопка недоступна или изменился селектор."
            )

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
        for name, locator in MskMtsMainWeb.HEADER_LINKS.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in MTSHomeOnlineMain.FOOTER_LINKS.items():
            self.check_link(locator, f"Footer: {name}")