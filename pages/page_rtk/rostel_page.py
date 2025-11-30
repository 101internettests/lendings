import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.rtk.rostel_locators import Rostelecom


class RostelecomPage(BasePage):
    @allure.title("Нажать на плавающую фиолетовую кнопку с телефоном в правом нижнем углу")
    def click_on_purple_button(self):
        try:
            self.page.locator(Rostelecom.CONNECT_PURPLE_BUTTON).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать на фиолетовую плавающую кнопку (телефон) в правом нижнем углу.\n"
                "Возможно, элемент перекрыт попапом, скрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Закрыть всплыващий попап")
    def close_popup(self):
        try:
            self.page.locator(Rostelecom.CLOSE_POPUP).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось закрыть всплывающий попап.\n"
                "Возможно, кнопка закрытия недоступна, перекрыта или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                expect(self.page.locator(Rostelecom.PHONE_BUTTON)).to_be_visible(timeout=65000)
            except Exception as e:
                raise AssertionError(
                    "Поле телефона в попапе не появилось за ожидаемое время.\n"
                    "Возможно, попап не отрисовался или перекрыт другим элементом."
                    f"\nТехнические детали: {e}"
                )
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_OFFER_POPUP).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Отправить' в попапе.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в форме 'Заявка на подключение'.\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT).fill("1")
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в форме 'Заявка на подключение'.\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_THREE).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форме 'Заявка на подключение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_CONNECT).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось отправить форму 'Заявка на подключение'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_online(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в форме 'Заявка на подключение' (онлайн).\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT).fill("1")
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в форме 'Заявка на подключение' (онлайн).\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_FOUR).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форме 'Заявка на подключение' (онлайн).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_CONNECT).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось отправить форму 'Заявка на подключение' (онлайн).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап скнопки Подключиться")
    def send_popup_application_connection_home_new_four(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT_FOUR).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в попапе 'Подключиться'.\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT_FOUR).fill("1")
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в попапе 'Подключиться'.\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Подключиться'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_OFFER_POPUP).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе 'Подключиться'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап с кнопки Подключиться для ТВ")
    def send_popup_application_connection_home_new_tv(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT_FOUR).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в попапе 'Подключиться для ТВ'.\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT_FOUR).fill("1")
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в попапе 'Подключиться для ТВ'.\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_FOUR).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Подключиться для ТВ'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_OFFER_POPUP).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе 'Подключиться для ТВ'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап скнопки Подключиться")
    def send_popup_application_connection_home_new_five(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.INPUT_STREET_FIVE).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в попапе 'Подключиться' (вариант 5).\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.INPUT_HOUSE_FIVE).fill("1")
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в попапе 'Подключиться' (вариант 5).\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Подключиться' (вариант 5).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_OFFER_POPUP).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе 'Подключиться' (вариант 5).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап скнопки Подключиться")
    def send_popup_application_connection_rtk(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.INPUT_STREET_FIVE).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в попапе 'Подключиться' (RTK).\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.INPUT_HOUSE_FIVE).fill("1")
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в попапе 'Подключиться' (RTK).\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_SIX).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Подключиться' (RTK).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_OFFER_POPUP).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе 'Подключиться' (RTK).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Нажать на кнопку Подключиться с баннера")
    def click_connect_banner_button(self):
        try:
            self.page.locator(Rostelecom.CONNECTION_BUTTON).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подключиться' на баннере.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Нажать на кнопку Подключиться с середины страницы")
    def click_connect_banner_button_middle(self):
        try:
            self.page.locator(Rostelecom.CONNECTION_BUTTON_MIDDLE).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подключиться' в середине страницы.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Нажать на кнопку Не определились с тарифом?")
    def click_connect_banner_button_middle(self):
        try:
            self.page.locator(Rostelecom.CONNECTION_BUTTON_MIDDLE).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать кнопку 'Не определились с тарифом?'.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Проверить возможность подключения около хедера")
    def send_popup_application_connection_header(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT_FIRST).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в форме проверки адреса (хедер).\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT_FIRST).fill("1")
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в форме проверки адреса (хедер).\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_FIRST).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форме проверки адреса (хедер).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.CHECK_THE_ADDRESS_BUTTON).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку проверки адреса (хедер).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Проверить возможность подключения около хедера")
    def send_popup_application_connection_online_rtk(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT_FIRST).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в форме проверки адреса (RTK хедер).\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT_FIRST).fill("1")
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в форме проверки адреса (RTK хедер).\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_FIRST).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форме проверки адреса (RTK хедер).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.BUTTON_CHECK_CONNECTION_RTK).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку проверки адреса (RTK хедер).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Проверить возможность подключения около хедера")
    def send_popup_application_connection_online_rtk_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT_SECOND).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в форме проверки адреса (RTK хедер, вариант 2).\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT_SECOND).fill("1")
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в форме проверки адреса (RTK хедер, вариант 2).\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форме проверки адреса (RTK хедер, вариант 2).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.BUTTON_CHECK_CONNECTION_RTK_SECOND).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку проверки адреса (RTK хедер, вариант 2).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Проверить возможность подключения около футера")
    def send_popup_application_connection_futer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT_SECOND).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в форме проверки адреса (футер).\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT_SECOND).fill("1")
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в форме проверки адреса (футер).\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форме проверки адреса (футер).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.CHECK_THE_ADDRESS_BUTTON_SECOND).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку проверки адреса (футер).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("попап не определились с тарифом")
    def send_popup_application_popup_dont_tariff(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.NAME_INPUT_FIRST).fill("Тест")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести имя в попапе 'Не определились с тарифом?'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Не определились с тарифом?'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.CHECK_THE_ADDRESS_BUTTON_SECOND).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось отправить форму 'Не определились с тарифом?'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Проверить возможность подключения в форме подключить")
    def send_popup_application_connection_futer_dom(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT_SECOND).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в форме 'Подключить' (блок у футера, Дом).\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT_SECOND).fill("1")
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в форме 'Подключить' (блок у футера, Дом).\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_THREE).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форме 'Подключить' (блок у футера, Дом).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_CONNECT).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось отправить форму 'Подłączить' (блок у футера, Дом).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Проверить возможность подключения в форме подключить")
    def send_popup_application_connection_futer_tv(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT_SECOND).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в форме 'Подключить' (блок у футера, ТВ).\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT_SECOND).fill("1")
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в форме 'Подключить' (блок у футера, ТВ).\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_SECOND).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форме 'Подключить' (блок у футера, ТВ).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_CONNECT).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось отправить форму 'Подключить' (блок у футера, ТВ).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(Rostelecom.TARIFF_CARDS).all()

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        try:
            self.page.locator(Rostelecom.TARIFF_CONNECT_BUTTONS).nth(card_index).click()
        except Exception as e:
            raise AssertionError(
                f"Не удалось нажать кнопку 'Подключить' на карточке тарифа #{card_index}.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
            )

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT_FOUR).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в форме подключения тарифа.\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT).type("1", delay=100)
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в форме подключения тарифа.\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.NAME_INPUT).fill("Тест")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести имя в форме подключения тарифа.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_FOUR).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форме подключения тарифа.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_SECOND).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось отправить форму подключения тарифа.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request_online(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT_FOUR).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в форме подключения тарифа (онлайн).\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT).type("1", delay=100)
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в форме подключения тарифа (онлайн).\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.NAME_INPUT).fill("Тест")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести имя в форме подключения тарифа (онлайн).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форме подключения тарифа (онлайн).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_SECOND).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось отправить форму подключения тарифа (онлайн).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Отправить заявку на подключение с карточек дом")
    def send_tariff_connection_request_dom(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в форме подключения тарифа (карточки Дом).\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT).type("1", delay=100)
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в форме подключения тарифа (карточки Дом).\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.NAME_INPUT).fill("Тест")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести имя в форме подключения тарифа (карточки Дом).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_FOUR).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форме подключения тарифа (карточки Дом).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_SECOND).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось отправить форму подключения тарифа (карточки Дом).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Отправить заявку на подключение с карточек дом")
    def send_tariff_connection_request_tv(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(Rostelecom.STREET_INPUT).type("Тестовая улица", delay=100)
                self.page.locator(Rostelecom.FIRST_STREET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести/выбрать улицу в форме подключения тарифа (карточки ТВ).\n"
                    "Возможно, подсказки не подгрузились или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.HOUSE_INPUT).type("1", delay=100)
                self.page.locator(Rostelecom.FIRST_HOUSE).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось указать номер дома в форме подключения тарифа (карточки ТВ).\n"
                    "Возможно, подсказка дома недоступна или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.NAME_INPUT).fill("Тест")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести имя в форме подключения тарифа (карточки ТВ).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.PHONE_BUTTON_THREE).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форме подключения тарифа (карточки ТВ).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(Rostelecom.SEND_BUTTON_SECOND).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось отправить форму подключения тарифа (карточки ТВ).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
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
        try:
            expect(popup_tariff_name).to_be_visible()
        except Exception as e:
            raise AssertionError(
                "Название тарифа в попапе не отображается.\n"
                "Возможно, попап не открылся или элемент скрыт."
                f"\nТехнические детали: {e}"
            )
        try:
            expect(popup_tariff_name).to_have_text(expected_name)
        except Exception as e:
            raise AssertionError(
                f"Название тарифа в попапе не соответствует ожидаемому: '{expected_name}'.\n"
                "Возможно, отображается другой тариф или изменилась разметка."
                f"\nТехнические детали: {e}"
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
        try:
            region_button.click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать на кнопку выбора региона в хедере.\n"
                "Возможно, элемент перекрыт попапом, скрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )
        time.sleep(2)