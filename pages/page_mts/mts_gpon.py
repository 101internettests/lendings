import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain, ApplicationPopupWithName, ApplicationPopupCheckConnection
from locators.mts.mts_home_online import FormApplicationCheckConnection, RegionChoice, MskMtsMainWeb


class MtsGponHomeOnlinePage(BasePage):
    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def close_thankyou_page(self):
        try:
            self.page.locator(MTSHomeOnlineMain.CLOSE_BUTTON_SECOND).click()
        except Exception:
            raise AssertionError(
                "Не удалось закрыть страницу благодарности (кнопка 'Закрыть').\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
            )

    @allure.title("Проверить, что попап Выгодное приложение появился")
    def check_popup_super_offer(self):
        try:
            expect(self.page.locator(MskMtsMainWeb.SUPER_OFFER_HEADER)).to_be_visible(timeout=65000)
            expect(self.page.locator(MskMtsMainWeb.SUPER_OFFER_TEXT)).to_be_visible(timeout=65000)
        except Exception:
            raise AssertionError(
                "Попап 'Выгодное предложение' не появился за ожидаемое время.\n"
                "Возможно, попап не отрисовался или перекрыт другим элементом."
            )

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                expect(self.page.locator(MskMtsMainWeb.INPUT_OFFER_POPUP)).to_be_visible(timeout=65000)
            except Exception:
                raise AssertionError(
                    "Поле телефона в попапе 'Выгодное предложение' не появилось вовремя."
                )
            try:
                self.page.locator(MskMtsMainWeb.ADDRESS_FIVE).fill("Тестадрес")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести адрес в попапе 'Выгодное предложение'."
                )
            try:
                self.page.locator(MskMtsMainWeb.INPUT_OFFER_POPUP).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Выгодное предложение'."
                )
            try:
                self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Отправить' в попапе 'Выгодное предложение'."
                )
            time.sleep(4)

    @allure.title("Нажать на кнопку Подключить")
    def click_connect_button(self):
        try:
            self.page.locator(MskMtsMainWeb.CONNECT_BUTTON).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подключить'.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupWithName.ADDRESS_INPUT).fill("Тестадрес")
            except Exception:
                raise AssertionError("Не удалось ввести адрес в попапе 'Заявка на подключение'.")
            try:
                self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError("Не удалось ввести имя в попапе 'Заявка на подключение'.")
            try:
                self.page.locator(MskMtsMainWeb.PHONE_INPUT_OTHER).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон в попапе 'Заявка на подключение'.")
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку отправки в попапе 'Заявка на подключение'.")
            time.sleep(4)

    @allure.title("Нажать на кнопку Проверить адрес")
    def click_check_address_button(self):
        try:
            self.page.locator(MskMtsMainWeb.CHECK_ADDRESS_BUTTON).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Проверить адрес'.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Нажать на кнопку Проверить адрес из футера")
    def click_check_address_button_futer(self):
        try:
            self.page.locator(MskMtsMainWeb.CHECK_ADDRESS_BUTTON_FUTER).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Проверить адрес' в футере.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title(
        "Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве в конце страницы")
    def send_popup_application_check_connection_near_futer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(FormApplicationCheckConnection.ADDRESS_SECOND).fill("Тестимя")
            except Exception:
                raise AssertionError("Не удалось ввести адрес в форму у футера.")
            time.sleep(3)
            try:
                self.page.locator(ApplicationPopupCheckConnection.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон в форму у футера.")
            time.sleep(3)
            try:
                self.page.locator(FormApplicationCheckConnection.CHECK_ADDRESS_BUTTON_SECOND).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку 'Проверить адрес' в форме у футера.")
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupWithName.ADDRESS_INPUT).fill("Тестадрес")
            except Exception:
                raise AssertionError("Не удалось ввести адрес в форме тарифа.")
            try:
                self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError("Не удалось ввести имя в форме тарифа.")
            try:
                self.page.locator(MskMtsMainWeb.PHONE_INPUT_OTHER).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон в форме тарифа.")
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку отправки в форме тарифа.")
            time.sleep(4)

    @allure.title(
        "Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве в конце страницы")
    def send_popup_application_check_connection_near_futer_another(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MskMtsMainWeb.ADDRESS_SECOND).fill("Тестимя")
            except Exception:
                raise AssertionError("Не удалось ввести адрес (вариант другой формы у футера).")
            time.sleep(3)
            try:
                self.page.locator(MskMtsMainWeb.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон (вариант другой формы у футера).")
            time.sleep(3)
            try:
                self.page.locator(MskMtsMainWeb.CHECK_ADDRESS_BUTTON_SECOND).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку 'Проверить адрес' (вариант другой формы у футера).")
            time.sleep(4)

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
            for name, locator in MskMtsMainWeb.HEADER_LINKS_GPON.items():
                self.check_link(locator, f"Header: {name}")
            # self.close_thankyou_page()
            # Проверяем ссылки в футере
            for name, locator in MTSHomeOnlineMain.FOOTER_LINKS.items():
                self.check_link(locator, f"Footer: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button_gpon(self):
        region_button = self.page.locator(MskMtsMainWeb.REGION_CHOICE_BUTTON_SECOND)
        try:
            region_button.click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку выбора региона (GPON, хедер).\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в футере")
    def click_region_choice_button_futer_gpon(self):
        region_button = self.page.locator(MskMtsMainWeb.REGION_CHOICE_BUTTON_FUTER)
        try:
            region_button.click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку выбора региона (GPON, футер).\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в футере новый")
    def click_region_choice_button_futer_gpon_new(self):
        region_button = self.page.locator(RegionChoice.TELE_REGION_CHOICE_BUTTON)
        try:
            region_button.click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку выбора региона (GPON, новый вариант).\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Закрыть попап Выгодное предложение")
    def close_popup_super_offer(self):
        try:
            self.page.locator(MskMtsMainWeb.SUPER_OFFER_CLOSE_NEW).click()
        except Exception:
            raise AssertionError("Не удалось закрыть попап 'Выгодное предложение'.")