import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.domru.domru_locators import LocationPopup, PopUps, CardsPopup


class DomRuClass(BasePage):
    @allure.title("Проверить, что появилась всплывашка Вы находитесь в городе")
    def check_location_popup(self):
        try:
            self.page.locator(LocationPopup.CHECK_LOCATION_POPUP).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось взаимодействовать с всплывающим окном 'Вы находитесь в городе'.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Ответить в всплывашке, что нахожусь в Москве")
    def close_popup_location(self):
        # Важно: этот попап может появляться не всегда. Метод должен быть безопасен для вызова "на всякий случай".
        header_visible = self.is_visible(getattr(LocationPopup, "POPUP_HEADER", LocationPopup.CHECK_LOCATION_POPUP), timeout_ms=1500)
        yes_visible = self.is_visible(LocationPopup.YES_BUTTON, timeout_ms=1500)
        if not (header_visible or yes_visible):
            return

        if not self.click_if_visible(LocationPopup.YES_BUTTON, timeout_ms=1500, click_timeout_ms=4000, force=True):
            # Попап видим, но закрыть не смогли — это уже ошибка.
            raise AssertionError(
                "Попап определения города видим, но не удалось нажать кнопку 'Да'.\n"
                "Возможно, элемент перекрыт, disabled или изменился селектор."
            )

        # Дожидаемся, что попап действительно закрылся (иначе следующие клики часто перехватываются оверлеем)
        self.wait_hidden(getattr(LocationPopup, "POPUP_HEADER", LocationPopup.CHECK_LOCATION_POPUP), timeout_ms=5000)

    @allure.title("Ответить в всплывашке, что нахожусь не в Москве")
    def choose_msk_location(self):
        try:
            self.page.locator(LocationPopup.NO_BUTTON).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать кнопку 'Нет' во всплывающем окне определения города.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Ответить в всплывашке, что нахожусь не в Москве")
    def choose_msk_location_new(self):
        try:
            self.page.locator(LocationPopup.NEW_BUTTON_NO).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать альтернативную кнопку 'Нет' во всплывающем окне.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Ответить в всплывашке, что нахожусь не в Москве третий")
    def choose_msk_location_new_third(self):
        try:
            self.page.locator(LocationPopup.NEW_BUTTON_NO_SECOND).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать третий вариант кнопки 'Нет' во всплывающем окне.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(LocationPopup.INPUT_OFFER_POPUP).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе предложения.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            try:
                self.page.locator(LocationPopup.SEND_BUTTON_OFFER_POPUP).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Отправить' в попапе предложения.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def close_thankyou_page(self):
        try:
            self.page.locator(LocationPopup.CLOSE_BUTTON).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось закрыть страницу благодарности (кнопка внизу справа).\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Отправить заявку в попап Подключите стабильный интернет в Москве")
    def send_popup_from_banner(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(PopUps.INPUT_NUM_POPUP).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Подключите стабильный интернет'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            try:
                self.page.locator(PopUps.BUTTON_NEW_INTERNET).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе 'Подключите стабильный интернет'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(3)

    @allure.title("Отправить заявку в попап Бесплатный тест-драйв роутера на 14 дней")
    def send_popup_free_tes_drive(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(PopUps.INPUT_NUM_POPUP_THR).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Бесплатный тест-драйв роутера'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            try:
                self.page.locator(PopUps.BUTTON_CONNECT).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе 'Бесплатный тест-драйв роутера'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(3)

    @allure.title("Отправить заявку в попап Тест-драйв скорости до 800 Мбит/с на 3 месяца")
    def send_popup_tes_drive_three_months(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(PopUps.INPUT_NUM_POPUP_FOU).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Тест-драйв скорости до 800 Мбит/с'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            try:
                self.page.locator(PopUps.BUTTON_CONNECT_SEC).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе 'Тест-драйв скорости до 800 Мбит/с'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(3)

    @allure.title("Отправить заявку в попап Попробуйте скоростной безлимитный интернет")
    def send_popup_speed_inter(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(PopUps.INPUT_NUM_POPUP_FIV).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Попробуйте скоростной безлимитный интернет'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            try:
                self.page.locator(PopUps.BUTTON_CONNECT_THI).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе 'Попробуйте скоростной безлимитный интернет'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(3)

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_check_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(PopUps.INPUT_ADDRESS).fill("Тестоадрес")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести адрес в форму проверки подключения.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            try:
                self.page.locator(PopUps.INPUT_NUM_POPUP_SEC).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форму проверки подключения.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            try:
                self.page.locator(PopUps.BUTTON_CHECK_ADDRESS).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' в форме проверки подключения.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        try:
            return self.page.locator(LocationPopup.TARIFF_CARDS).all()
        except Exception:
            raise AssertionError(
                "Не удалось получить список тарифных карточек.\n"
                "Возможно, карточки не отрисовались или изменился селектор."
            )

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        try:
            self.page.locator(LocationPopup.TARIFF_CONNECT_BUTTONS).nth(card_index).click()
        except Exception:
            raise AssertionError(
                f"Не удалось нажать кнопку 'Подключить' на карточке тарифа #{card_index}.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
            )

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(CardsPopup.INPUT_NAME).fill("Тестимя")
            except Exception:
                raise AssertionError("Не удалось ввести имя в форме тарифа.")
            try:
                self.page.locator(CardsPopup.INPUT_NUM).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон в форме тарифа.")
            try:
                self.page.locator(CardsPopup.SEND_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку отправки в форме тарифа.")
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(CardsPopup.INPUT_NAME).fill("Тестимя")
            except Exception:
                raise AssertionError("Не удалось ввести имя в форме тарифа.")
            try:
                self.page.locator(PopUps.INPUT_NUM_POPUP_FOU).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон в форме тарифа.")
            try:
                self.page.locator(CardsPopup.SEND_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку отправки в форме тарифа.")
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(CardsPopup.INPUT_NAME).fill("Тестимя")
            except Exception:
                raise AssertionError("Не удалось ввести имя в форме тарифа.")
            try:
                self.page.locator(PopUps.INPUT_NUM_POPUP_FOU).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон в форме тарифа.")
            try:
                self.page.locator(CardsPopup.SEND_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку отправки в форме тарифа.")
            time.sleep(4)

    @allure.title("Нажать на кнопку Подключить интернет первую")
    def open_popup_connection(self):
        try:
            self.page.locator(PopUps.BUTTON_CONNECT_INTERNET).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать первую кнопку 'Подключить интернет'.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Нажать на кнопку Подключить интернет вторую")
    def open_popup_connection_second(self):
        try:
            self.page.locator(PopUps.BUTTON_CONNECT_INTERNET_SECOND).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать вторую кнопку 'Подключить интернет'.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Нажать на кнопку Подключить интернет третью")
    def open_popup_connection_third(self):
        try:
            self.page.locator(PopUps.BUTTON_CONNECT_INTERNET_THIRD).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать третью кнопку 'Подключить интернет'.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
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
    def check_all_links(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in LocationPopup.HEADER_LINKS.items():
                self.check_link(locator, f"Header: {name}")

            # Проверяем ссылки в футере
            for name, locator in LocationPopup.FOOTER_LINKS.items():
                self.check_link(locator, f"Footer: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Проверить все ссылки на странице")
    def check_all_links_sec(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in LocationPopup.HEADER_LINKS.items():
                self.check_link(locator, f"Header: {name}")

            # Проверяем ссылки в футере
            for name, locator in LocationPopup.FOOTER_LINKS_SEC.items():
                self.check_link(locator, f"Footer: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def close_popup(self):
        try:
            self.page.locator(LocationPopup.CLOSE_POPUP).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось закрыть попап (кнопка закрытия).\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(LocationPopup.NAME_INPUT).fill("Тестимя")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести имя в попапе 'Заявка на подключение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(PopUps.INPUT_NUM_POPUP_SIX).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Заявка на подключение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(LocationPopup.BUTTON_SEND).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе 'Заявка на подключение'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Нажать на лого на главной странице и проверить")
    def click_on_logo(self):
        try:
            self.page.locator(LocationPopup.MAIN_LOGO).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось кликнуть по логотипу на главной странице.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Нажать на лого на главной странице и проверить")
    def click_on_logo_beeline(self):
        try:
            self.page.locator(LocationPopup.MAIN_LOGO_BEELINE).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось кликнуть по логотипу Билайн на главной странице.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )