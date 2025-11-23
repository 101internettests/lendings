import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.tele_two.tele_two_locators import TeleTwoMain


class TeleTwoPage(BasePage):
    @allure.title("Нажать на кнопку Подключиться хедер")
    def click_connect_button_header(self):
        try:
            self.page.locator(TeleTwoMain.CONNECT_HEADER_BUTTON).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подключиться' в хедере.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(TeleTwoMain.NAME_INPUT).fill("Тест")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести имя в попапе 'Заявка на подключение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(TeleTwoMain.PHONE_INPUT).fill("9999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Заявка на подключение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(TeleTwoMain.SEND_BUTTON).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Отправить' в попапе 'Заявка на подключение'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)

    @allure.title("Нажать на кнопку Подключить на баннере")
    def click_connect_button_banner(self):
        try:
            self.page.locator(TeleTwoMain.BANNER_BUTTON).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подключить' на баннере.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(TeleTwoMain.TARIFF_CARDS).all()

    @allure.title("Получить список всех тарифных карточек домашний")
    def get_tariff_cards_home(self):
        return self.page.locator(TeleTwoMain.TARIFF_MOB).all()

    @allure.title("Нажать кнопку подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        try:
            self.page.locator(TeleTwoMain.TARIFF_BUTTON).nth(card_index).click()
        except Exception as e:
            raise AssertionError(
                f"Не удалось нажать кнопку 'Подключить' на карточке тарифа #{card_index}.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_cards(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(TeleTwoMain.NAME_INPUT_TWO).fill("Тест")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести имя в попапе (карточки тарифа).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(TeleTwoMain.PHONE_INPUT_THREE).fill("9999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе (карточки тарифа).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(TeleTwoMain.SEND_BUTTON_TWO).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Отправить' в попапе (карточки тарифа).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_cards_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(TeleTwoMain.NAME_INPUT).fill("Тест")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести имя в попапе 'Заявка на подключение' (новая версия).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(TeleTwoMain.PHONE_INPUT).fill("9999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Заявка на подключение' (новая версия).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(TeleTwoMain.SEND_BUTTON).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Отправить' в попапе 'Заявка на подключение' (новая версия).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу")
    def send_popup_from_your_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(TeleTwoMain.CITY_INPUT).fill("Тестгород")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести город в форму 'Проверьте возможность подключения'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(TeleTwoMain.STREET_INPUT).fill("Тестовая 1")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести улицу в форму 'Проверьте возможность подключения'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(TeleTwoMain.PHONE_INPUT_FIRST).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форму 'Проверьте возможность подключения'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)
            try:
                self.page.locator(TeleTwoMain.CHECK_THE_ADDRESS).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' в форме 'Проверьте возможность подключения'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(3)

    @allure.title("Нажать на кнопку Подключиться футер")
    def click_connect_button_futer(self):
        try:
            self.page.locator(TeleTwoMain.CONNECT_FUTER_BUTTON).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подключиться' в футере.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Нажать на кнопку Не нашли свой город")
    def click_button_dont_find_city(self):
        try:
            self.page.locator(TeleTwoMain.BUTTON_DONT_CITY).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать кнопку 'Не нашли свой город'.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )
        time.sleep(2)
