import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain, ApplicationPopupWithName, ApplicationPopupCheckConnection, MtsRuLocators
from locators.mts.mts_home_online import FormApplicationCheckConnection, RegionChoice, MskMtsMainWeb, MtsThirdOnline


class MtsHomeOnlinePage(BasePage):
    @allure.title("Проверить, что попап Выгодное приложение появился")
    def check_popup_super_offer(self):
        try:
            expect(self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_HEADER)).to_be_visible(timeout=65000)
            expect(self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)).to_be_visible(timeout=65000)
        except Exception:
            raise AssertionError("Попап не появился на странице за 65 секунд")

    @allure.title("Проверить, что попап Выгодное приложение появился")
    def check_popup_super_offer_second(self):
        try:
            expect(self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)).to_be_visible(timeout=65000)
            expect(self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_TEXT)).to_be_visible(timeout=65000)
        except Exception:
            raise AssertionError("Попап не появился на странице за 65 секунд")

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                expect(self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP)).to_be_visible(timeout=65000)
            except Exception as e:
                raise AssertionError(
                    "Не появился попап 'Выгодное предложение' (поле телефона не видно).\n"
                    "Возможно попап не отрисовался, перекрыт или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupWithName.ADDRESS_INPUT_FIVE).fill("Тестоадрес")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести адрес в попап 'Выгодное предложение'.\n"
                    "Возможно, элемент недоступен, скрыт или изменился селектор."
                )
            try:
                self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попап 'Выгодное предложение'.\n"
                    "Возможно, элемент недоступен, скрыт или изменился селектор."
                )
            try:
                self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Отправить' в попапе 'Выгодное предложение'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попап 'Выгодное предложение' (новая версия).\n"
                    "Возможно, элемент недоступен, скрыт или изменился селектор."
                )
            try:
                self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Отправить' в попапе 'Выгодное предложение'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап для других страниц и проверить успешность")
    def send_popup_super_offer_other_pages(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP_SOME_PAGE).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попап 'Выгодное предложение' на странице.\n"
                    "Возможно, элемент недоступен, скрыт или изменился селектор."
                )
            try:
                self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Отправить' в попапе 'Выгодное предложение' на странице.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title("Проверить успешность отправления заявки")
    def check_sucess(self):
        # Дождёмся смены URL в разумные сроки, так как редирект на страницу благодарности может занять время
        deadline = time.time() + 16.0
        last_url = ""
        while time.time() < deadline:
            try:
                current_url = self.page.url or ""
                last_url = current_url
                lu = current_url.lower()
                if (
                    "/thanks" in lu
                    or "/tilda/form1/submitted" in lu
                    or lu.endswith("/tilda/form1/submitted/")
                ):
                    return
                # Также проверим, не открылся ли redirect в новом окне/вкладке
                try:
                    for p in self.page.context.pages:
                        pu = (p.url or "").lower()
                        if (
                            "/thanks" in pu
                            or "/tilda/form1/submitted" in pu
                            or pu.endswith("/tilda/form1/submitted/")
                        ):
                            # Переключимся на найденную страницу благодарности
                            self.page = p
                            return
                except Exception:
                    pass
            except Exception:
                pass
            time.sleep(0.5)

        # Последние попытки через ожидание URL по маскам
        try:
            self.page.wait_for_url("**/thanks**", timeout=5000)
            return
        except Exception:
            pass
        try:
            self.page.wait_for_url("**/tilda/form1/submitted**", timeout=5000)
            return
        except Exception:
            pass
        # Финальная попытка: дождаться стабилизации сети и перечитать URL
        try:
            self.page.wait_for_load_state("networkidle", timeout=5000)
            final_url = (self.page.url or "").lower()
            if "/thanks" in final_url or "/tilda/form1/submitted" in final_url or final_url.endswith("/tilda/form1/submitted/"):
                return
        except Exception:
            pass
        # Визуальный фолбэк по видимости элементов "Спасибо"
        try:
            if (
                self.page.locator(MTSHomeOnlineMain.MORE_THANKYOU).is_visible(timeout=2000)
                or self.page.locator(MTSHomeOnlineMain.THANKYOU_TEXT_SECOND).is_visible(timeout=2000)
            ):
                return
        except Exception:
            pass

        raise AssertionError(f"Страница благодарности не появилась: URL не содержит признаков успешной отправки (last: {last_url})")

    @allure.title("Проверить успешность отправления заявки")
    def check_sucess_express(self):
        expect(self.page.locator(MTSHomeOnlineMain.MORE_THANKYOU)).to_be_visible(timeout=10000)

    @allure.title("Проверить успешность отправления заявки - заявка принята")
    def check_sucess_accept(self):
        with allure.step("Проверить, что заявка отправилась"):
            expect(self.page.locator(MTSHomeOnlineMain.THANKYOU_TEXT_SECOND)).to_be_visible()

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def close_thankyou_page(self):
        # Проверяем, какая кнопка доступна и нажимаем первую доступную
        if self.page.locator(MTSHomeOnlineMain.CLOSE_BUTTON).is_visible(timeout=1000):
            self.page.locator(MTSHomeOnlineMain.CLOSE_BUTTON).click()
        elif self.page.locator(MTSHomeOnlineMain.THANKYOU_CLOSE).is_visible(timeout=1000):
            self.page.locator(MTSHomeOnlineMain.THANKYOU_CLOSE).click()
        elif self.page.locator(MTSHomeOnlineMain.CLOSE_BUTTON_NEW).is_visible(timeout=1000):
            self.page.locator(MTSHomeOnlineMain.CLOSE_BUTTON_NEW).click()
        elif self.page.locator(MTSHomeOnlineMain.CLOSE_BUTTON_MEGA).is_visible(timeout=1000):
            self.page.locator(MTSHomeOnlineMain.CLOSE_BUTTON_MEGA).click()
        elif self.page.locator(MTSHomeOnlineMain.GO_TO_MAIN).is_visible(timeout=1000):
            self.page.locator(MTSHomeOnlineMain.GO_TO_MAIN).click()

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def close_thankyou_page_sec(self):
        try:
            self.page.go_back()
        except Exception:
            raise AssertionError(
                "Не удалось вернуться со страницы благодарности.\n"
                "Возможно, страница не загрузилась или навигация заблокирована."
            )

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def close_thankyou_page_express(self):
        try:
            self.page.locator(MTSHomeOnlineMain.GO_TO_MAIN).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку возврата на главную со страницы благодарности.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def click_on_red_button(self):
        try:
            self.page.locator(MTSHomeOnlineMain.RED_BUTTON).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать на красную плавающую кнопку с телефоном.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
            )

    @allure.title("Нажать на кнопку Подключить")
    def click_connect_button(self):
        try:
            self.page.locator(MTSHomeOnlineMain.CONNECT_BUTTON).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подключить'.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Нажать на кнопку Подключиться")
    def click_connecting_button(self):
        try:
            self.page.locator(MTSHomeOnlineMain.CONNECT_BUTTON_SECOND_CONNECT).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подключиться'.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Нажать на кнопку Подключиться футер")
    def click_connecting_button_second(self):
        try:
            self.page.locator(MTSHomeOnlineMain.CONNECT_BUTTON_THIRD).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подключиться' в футере.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Нажать на кнопку Подключить из блока выгодные условия")
    def click_connect_button_good_traid(self):
        try:
            self.page.locator(MTSHomeOnlineMain.CONNECT_BUTTON_CONDITIONS).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подключить' в блоке выгодных условий.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Нажать на кнопку Подключить из футера")
    def click_connect_button_futer(self):
        try:
            self.page.locator(MTSHomeOnlineMain.CONNECT_BUTTON_FUTER).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подключить' в футере.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupWithName.ADDRESS_INPUT).fill("Тестадрес")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести адрес в попапе 'Заявка на подключение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(1)
            try:
                self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести имя в попапе 'Заявка на подключение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(1)
            try:
                self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Заявка на подключение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(1)
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе 'Заявка на подключение'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести имя в попапе 'Заявка на подключение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(1)
            try:
                self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Заявка на подключение'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(1)
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе 'Заявка на подключение'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение с других страниц")
    def send_popup_application_connection_other(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести имя в попапе connection.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupWithName.PHONE_INPUT_OTHER).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе connection.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе connection.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение с других страниц")
    def send_popup_application_connection_another(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести имя в попапе connection.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupWithName.PHONE_INPUT_ANOTHER).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе connection .\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе connection.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title("Нажать на кнопку Проверить адрес")
    def click_check_address_button(self):
        try:
            self.page.locator(MTSHomeOnlineMain.CHECK_ADDRESS_BUTTON).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Проверить адрес'.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Нажать на кнопку Проверить адрес из футера")
    def click_check_address_button_futer(self):
        try:
            self.page.locator(MTSHomeOnlineMain.CHECK_ADDRESS_BUTTON_FUTER).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Проверить адрес' в футере.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Отправить заявку в попап с названием Проверьте возможность подключения по вашему адресу")
    def send_popup_application_connection_your_address(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupCheckConnection.ADDRESS_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести адрес в попапе проверки подключения.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupCheckConnection.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе проверки подключения.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupCheckConnection.CHECK_ADDRESS_BUTTON).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' в попапе проверки подключения.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)


    @allure.title("Отправить заявку в попап с названием Проверьте возможность подключения по вашему адресу с другой страницы")
    def send_popup_application_connection_your_address_other(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupCheckConnection.ADDRESS_INPUT_SECOND).fill("Тестимя")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести адрес (другая страница) в проверке подключения.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupCheckConnection.PHONE_INPUT_SECOND).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон (другая страница) в проверке подключения.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupCheckConnection.CHECK_ADDRESS_BUTTON_SECOND).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' (другая страница) в проверке подключения.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title(
        "Отправить заявку в попап с названием Проверьте возможность подключения по вашему адресу с другой страницы")
    def send_popup_application_connection_your_address_third(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupCheckConnection.ADDRESS_INPUT_SECOND).fill("Тестимя")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести адрес в connection.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupCheckConnection.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в connection.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupCheckConnection.CHECK_ADDRESS_BUTTON).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' connection.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title(
        "Отправить заявку в попап с названием Проверьте возможность подключения по вашему адресу с другой страницы")
    def send_popup_application_connection_your_address_another(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupCheckConnection.ADDRESS_INPUT_SECOND).fill("Тестимя")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести адрес (другой вариант) в проверке подключения.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupCheckConnection.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон (другой вариант) в проверке подключения.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            try:
                self.page.locator(ApplicationPopupCheckConnection.CHECK_ADDRESS_BUTTON_SECOND).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' (другой вариант) в проверке подключения.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title("Нажать на баннер на главной стране")
    def click_on_banner(self):
        try:
            self.page.locator(MTSHomeOnlineMain.BANNER).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать на баннер на главной странице.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
            )

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве под баннером")
    def send_popup_application_check_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(FormApplicationCheckConnection.ADDRESS).fill("Тестимя")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести адрес в форму под баннером.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(3)
            try:
                self.page.locator(FormApplicationCheckConnection.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в форму под баннером.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(3)
            try:
                self.page.locator(FormApplicationCheckConnection.CHECK_ADDRESS_BUTTON).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' в форме под баннером.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве под баннером")
    def send_popup_application_check_connection_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(FormApplicationCheckConnection.ADDRESS).fill("Тестоулица11111")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести адрес в форму под баннером (новая версия).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(3)
            try:
                self.page.locator(FormApplicationCheckConnection.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в форму под баннером (новая версия).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(3)
            try:
                self.page.locator(FormApplicationCheckConnection.CHECK_ADDRESS_BUTTON).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' в форме под баннером (новая версия).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве под баннером")
    def send_popup_application_check_connection_third(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(FormApplicationCheckConnection.ADDRESS).fill("Тестоулица11111")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести адрес в форму под баннером (третий вариант).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(3)
            try:
                self.page.locator(FormApplicationCheckConnection.PHONE_INPUT_SECOND).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в форму под баннером (третий вариант).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(3)
            try:
                self.page.locator(FormApplicationCheckConnection.CHECK_ADDRESS_BUTTON_SECOND).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' в форме под баннером (третий вариант).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)


    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве в конце страницы")
    def send_popup_application_check_connection_near_futer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(FormApplicationCheckConnection.ADDRESS_SECOND).fill("Тестимя")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести адрес в форму у футера.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(3)
            try:
                self.page.locator(FormApplicationCheckConnection.PHONE_INPUT_SECOND).fill("99999999999")
            except Exception:
                raise AssertionError(
                    "Не удалось ввести телефон в форму у футера.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                )
            time.sleep(3)
            try:
                self.page.locator(FormApplicationCheckConnection.CHECK_ADDRESS_BUTTON_SECOND).click()
            except Exception:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' в форме у футера.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                )
            time.sleep(4)

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        try:
            return self.page.locator(MTSHomeOnlineMain.TARIFF_CARDS).all()
        except Exception:
            raise AssertionError(
                "Не удалось получить список тарифных карточек.\n"
                "Возможно, карточки не отрисовались или изменился селектор."
            )

    @allure.title("Получить название тарифа из карточки")
    def get_tariff_name(self, card_index):
        try:
            name_loc = self.page.locator(MTSHomeOnlineMain.TARIFF_NAMES).nth(card_index)
            expect(name_loc).to_be_visible()
            tariff_name = (name_loc.text_content() or "").strip()
            if not tariff_name:
                raise AssertionError("Название тарифа пустое.")
            return f"Тариф: \n                              {tariff_name}\n                              "
        except AssertionError:
            raise
        except Exception:
            raise AssertionError(
                f"Не удалось получить название тарифа для карточки #{card_index}.\n"
                "Возможно, элемент недоступен, скрыт или изменился селектор."
            )

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        try:
            self.page.locator(MTSHomeOnlineMain.TARIFF_CONNECT_BUTTONS).nth(card_index).click()
        except Exception:
            raise AssertionError(
                f"Не удалось нажать кнопку 'Подключить' на карточке тарифа #{card_index}.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
            )

    @allure.title("Проверить название тарифа в попапе")
    def verify_popup_tariff_name(self, expected_name):
        popup_tariff_name = self.page.locator(MTSHomeOnlineMain.POPUP_TARIFF_NAME)
        try:
            expect(popup_tariff_name).to_be_visible()
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

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError("Не удалось ввести имя в форме тарифа (новая версия).")
            try:
                self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон в форме тарифа (новая версия).")
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку отправки в форме тарифа (новая версия).")
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа для других страниц")
    def send_tariff_connection_request_other(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError("Не удалось ввести имя в форме тарифа (другая страница).")
            try:
                self.page.locator(ApplicationPopupWithName.PHONE_INPUT_OTHER).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон в форме тарифа (другая страница).")
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку отправки в форме тарифа (другая страница).")
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа для других страниц")
    def send_tariff_connection_request_another(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError("Не удалось ввести имя в форме тарифа (вариант другой страницы).")
            try:
                self.page.locator(ApplicationPopupWithName.PHONE_INPUT_ANOTHER).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон в форме тарифа (вариант другой страницы).")
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку отправки в форме тарифа (вариант другой страницы).")
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
            for name, locator in MTSHomeOnlineMain.HEADER_LINKS.items():
                self.check_link(locator, f"Header: {name}")

            # Проверяем ссылки в футере
            for name, locator in MTSHomeOnlineMain.FOOTER_LINKS.items():
                self.check_link(locator, f"Footer: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button(self):
        region_button = self.page.locator(RegionChoice.REGION_CHOICE_BUTTON)
        try:
            region_button.click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку выбора региона в хедере.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button_gpon(self):
        region_button = self.page.locator(RegionChoice.REGION_CHOICE_BUTTON_FUTER)
        try:
            region_button.click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку выбора региона в хедере (вариант GPON/футер).\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button_mts(self):
        region_button = self.page.locator(RegionChoice.NEW_REGION_CHOICE_BUTTON_MTS)
        try:
            region_button.click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку выбора региона (новая версия MTS).\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button_new(self):
        # Закрываем возможные перекрывающие попапы, если видимы
        try:
            for close_locator in [
                MTSHomeOnlineMain.SUPER_OFFER_CLOSE,
                MTSHomeOnlineMain.SUPER_OFFER_CLOSE_HOME,
                MTSHomeOnlineMain.SUPER_OFFER_CLOSE_SECOND,
            ]:
                close_btn = self.page.locator(close_locator)
                if close_btn.is_visible():
                    close_btn.click(force=True)
                    time.sleep(0.5)
        except Exception:
            pass

        # Пробуем ESC как универсальный способ закрыть оверлей
        try:
            self.page.keyboard.press("Escape")
        except Exception:
            pass

        # Пробуем разные варианты кнопок города (на разных шаблонах разные теги/позиции)
        candidates = [
            RegionChoice.NEW_REGION_CHOICE_BUTTON,
            RegionChoice.HEADER_BUTTON_NEW,
            RegionChoice.NEW_REGION_CHOICE_BUTTON_HEADER,
            RegionChoice.REGION_CHOICE_BUTTON,
            RegionChoice.REGION_CHOICE_BUTTON_FUTER,
            RegionChoice.FUTER_MTS_NEW,
            MTSHomeOnlineMain.ANOTHER_CITY_BUTTON,
        ]

        opened = False
        for sel in candidates:
            try:
                btn = self.page.locator(sel)
                if btn.count() == 0:
                    continue
                btn.scroll_into_view_if_needed()
                btn.click(force=True)
                # Ждём открытия попапа (таблица городов становится видимой)
                try:
                    self.page.locator("xpath=//table[@class='city_list']").wait_for(state="visible", timeout=5000)
                    opened = True
                    break
                except Exception:
                    try:
                        self.page.locator(RegionChoice.RANSOM_CITY_BUTTON).first.wait_for(state="attached", timeout=3000)
                        opened = True
                        break
                    except Exception:
                        continue
            except Exception:
                continue

        time.sleep(1)

    @allure.title("Нажать на кнопку выбора региона в футере")
    def click_region_choice_button_futer(self):
        region_button = self.page.locator(RegionChoice.REGION_CHOICE_BUTTON_FUTER)
        try:
            region_button.click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку выбора региона в футере.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в футере")
    def click_region_choice_button_beeline(self):
        region_button = self.page.locator(RegionChoice.FOOTER_BUTTON)
        try:
            region_button.click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку выбора региона (вариант Beeline).\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в футере после выбора города")
    def click_region_choice_button_beeline_second(self):
        region_button = self.page.locator(RegionChoice.FOOTER_SECOND_TIME)
        try:
            region_button.click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку выбора региона в футере после выбора города.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в футере")
    def click_region_choice_button_futer_new(self):
        region_button = self.page.locator(RegionChoice.FUTER_CHOICE)
        try:
            region_button.click(force=True)
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку выбора региона в футере (новая версия).\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )
        time.sleep(2)


class ChoiceRegionPage(BasePage):
    @allure.title("Ввести текст в поле поиска региона")
    def fill_region_search(self, search_text):
        city_input = self.page.locator(RegionChoice.CITY_INPUT)
        try:
            city_input.fill(search_text)
        except Exception:
            raise AssertionError(
                "Не удалось ввести текст в поле поиска региона.\n"
                "Возможно, поле недоступно, скрыто или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Ввести текст в поле поиска региона")
    def fill_region_search_new(self, search_text):
        city_input = self.page.locator(RegionChoice.NEW_CITY_INPUT)
        try:
            city_input.fill(search_text)
        except Exception:
            raise AssertionError(
                "Не удалось ввести текст в поле поиска региона (новая версия).\n"
                "Возможно, поле недоступно, скрыто или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Ввести текст в поле поиска региона")
    def fill_region_search_RTK(self, search_text):
        city_input = self.page.locator(RegionChoice.RTK_CITY_INPUT)
        try:
            city_input.fill(search_text)
        except Exception:
            raise AssertionError(
                "Не удалось ввести текст в поле поиска региона (RTK).\n"
                "Возможно, поле недоступно, скрыто или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Проверить, что первый вариант содержит ожидаемый текст")
    def verify_first_region_choice(self, expected_text):
        candidates = [
            RegionChoice.FIRST_CHOICE,
            "xpath=(//a[contains(@class,'region_item')])[1]",
            "xpath=(//table[@class='city_list']//tbody//tr//td//a)[1]",
            "xpath=(//div[contains(@class,'city_list')]//a)[1]",
            "xpath=(//*[contains(@class,'region-search')]//a)[1]",
        ]
        for selector in candidates:
            try:
                loc = self.page.locator(selector).first
                if loc.count() == 0:
                    continue
                loc.wait_for(state="visible", timeout=7000)
                return loc
            except Exception:
                continue
        raise AssertionError("Не найден первый элемент списка городов (попап выбора региона).")

    @allure.title("Проверить, что первый вариант содержит ожидаемый текст")
    def verify_first_region_choice_rtk(self, expected_text):
        try:
            first_choice = self.page.locator(RegionChoice.FIRST_CHOICE_RTK)
            expect(first_choice).to_be_visible()
            expect(first_choice).to_contain_text(expected_text)
            return first_choice
        except Exception:
            raise AssertionError(
                f"Первый вариант региона не содержит ожидаемый текст '{expected_text}' или элемент недоступен."
            )

    @allure.title("Выбрать первый регион из списка")
    def select_first_region(self):
        candidates = [
            RegionChoice.FIRST_CHOICE,
            "xpath=(//a[contains(@class,'region_item')])[1]",
            "xpath=(//table[@class='city_list']//tbody//tr//td//a)[1]",
            "xpath=(//div[contains(@class,'city_list')]//a)[1]",
            "xpath=(//*[contains(@class,'region-search')]//a)[1]",
        ]
        for selector in candidates:
            try:
                loc = self.page.locator(selector).first
                if loc.count() == 0:
                    continue
                loc.click()
                time.sleep(2)
                return
            except Exception:
                continue
        raise AssertionError("Не удалось кликнуть по первому варианту города. Список не найден.")

    @allure.title("Выбрать первый регион из списка")
    def select_first_region_rtk(self):
        try:
            first_choice = self.page.locator(RegionChoice.FIRST_CHOICE_RTK)
            expect(first_choice).to_be_visible()
            first_choice.click()
        except Exception:
            raise AssertionError(
                "Не удалось выбрать первый регион из списка (RTK).\n"
                "Возможно, список не отрисован или элемент недоступен."
            )
        time.sleep(2)

    @allure.title("Проверить текст кнопки выбора региона")
    def verify_region_button_text(self, expected_text):
        try:
            region_button = self.page.locator(RegionChoice.REGION_CHOICE_BUTTON)
            expect(region_button).to_be_visible()
            actual_text = (region_button.text_content() or "").strip()
            if actual_text != expected_text:
                raise AssertionError(
                    f"Некорректный город в кнопке выбора региона: '{actual_text}', ожидали '{expected_text}'"
                )
        except AssertionError:
            raise
        except Exception:
            raise AssertionError(
                "Не удалось проверить текст кнопки выбора региона (основной).\n"
                "Возможно, кнопка недоступна или изменился селектор."
            )

    @allure.title("Проверить текст кнопки выбора региона")
    def verify_region_button_text_updated(self, expected_text):
        try:
            region_button = self.page.locator(RegionChoice.UPDATED_REGION_BUTTON)
            expect(region_button).to_be_visible()
            actual_text = (region_button.text_content() or "").strip()
            if actual_text != expected_text:
                raise AssertionError(
                    f"Некорректный город в кнопке выбора региона: '{actual_text}', ожидали '{expected_text}'"
                )
        except AssertionError:
            raise
        except Exception:
            raise AssertionError(
                "Не удалось проверить текст кнопки выбора региона (новая версия).\n"
                "Возможно, кнопка недоступна или изменился селектор."
            )

    @allure.title("Проверить текст кнопки выбора региона")
    def verify_region_button_text_new(self, expected_text):
        try:
            region_button = self.page.locator(RegionChoice.NEW_REGION_CHOICE_BUTTON)
            expect(region_button).to_be_visible()
            actual_text = (region_button.text_content() or "").strip()
            if actual_text != expected_text:
                raise AssertionError(
                    f"Некорректный город в кнопке выбора региона: '{actual_text}', ожидали '{expected_text}'"
                )
        except AssertionError:
            raise
        except Exception:
            raise AssertionError(
                "Не удалось проверить текст кнопки выбора региона (новая версия).\n"
                "Возможно, кнопка недоступна или изменился селектор."
            )

    @allure.title("Проверить текст кнопки выбора региона")
    def verify_region_button_text_tele(self, expected_text):
        try:
            region_button = self.page.locator(RegionChoice.TELE_REGION_CHOICE_BUTTON)
            expect(region_button).to_be_visible()
            actual_text = (region_button.text_content() or "").strip()
            if actual_text != expected_text:
                raise AssertionError(
                    f"Некорректный город в кнопке выбора региона: '{actual_text}', ожидали '{expected_text}'"
                )
        except AssertionError:
            raise
        except Exception:
            raise AssertionError(
                "Не удалось проверить текст кнопки выбора региона (TELE).\n"
                "Возможно, кнопка недоступна или изменился селектор."
            )

    @allure.title("Проверить текст кнопки выбора региона")
    def verify_region_button_text_new_gpon(self, expected_text):
        try:
            region_button = self.page.locator(RegionChoice.REGION_CHOICE_BUTTON_FUTER)
            expect(region_button).to_be_visible()
            actual_text = (region_button.text_content() or "").strip()
            if actual_text != expected_text:
                raise AssertionError(
                    f"Некорректный город в кнопке выбора региона: '{actual_text}', ожидали '{expected_text}'"
                )
        except AssertionError:
            raise
        except Exception:
            raise AssertionError(
                "Не удалось проверить текст кнопки выбора региона (GPON/футер).\n"
                "Возможно, кнопка недоступна или изменился селектор."
            )

    @allure.title("Нажать на кнопку Не смогли найти город")
    def click_button_dont_find_city(self):
        try:
            self.page.locator(RegionChoice.BUTTON_DONT_CITY).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Не нашли свой город?'.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
            )
        time.sleep(2)

    @allure.title("Отправить заявку в форму Не нашли свой город?")
    def send_form_dont_find_city(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(RegionChoice.FORM_CITY).fill("Тестгород")
            except Exception:
                raise AssertionError("Не удалось ввести город в форму 'Не нашли свой город?'.")
            try:
                self.page.locator(FormApplicationCheckConnection.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон в форму 'Не нашли свой город?'.")
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку отправки в форме 'Не нашли свой город?'.")
            time.sleep(4)

    @allure.title("Закрыть попап Выгодное предложение")
    def close_popup_super_offer(self):
        try:
            self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_CLOSE).click()
        except Exception:
            raise AssertionError("Не удалось закрыть попап 'Выгодное предложение'.")

    @allure.title("Закрыть попап Выгодное предложение")
    def close_popup_super_offer_new(self):
        try:
            self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_CLOSE_MEGA).click()
        except Exception:
            raise AssertionError("Не удалось закрыть попап 'Выгодное предложение' (новая версия).")

    @allure.title("Закрыть попап Выгодное предложение")
    def close_popup_super_offer_all(self):
        # Пытаемся нажать на первую видимую кнопку закрытия
        close_buttons = [
            MTSHomeOnlineMain.SUPER_OFFER_CLOSE_MEGA,
            MTSHomeOnlineMain.SUPER_OFFER_CLOSE,
            MTSHomeOnlineMain.SUPER_OFFER_CLOSE_HOME,
            MTSHomeOnlineMain.SUPER_OFFER_CLOSE_MORE,
            MTSHomeOnlineMain.SUPER_OFFER_CLOSE_SECOND,
            MTSHomeOnlineMain.SUPER_OFFER_CLOSE_NEW
        ]

        # Пытаемся найти и нажать первую доступную кнопку
        for button_locator in close_buttons:
            if self.page.locator(button_locator).is_visible():
                self.page.locator(button_locator).click()
                break

class MTSSecondOnlinePage(BasePage):
    @allure.title("Нажать на кнопку Принять на главной странице")
    def click_confirm_button(self):
        try:
            self.page.locator(MtsThirdOnline.BUTTON_CONFIRM).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Принять' на главной странице.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Нажать на кнопку Подобрать тариф")
    def click_choose_tariff_button(self):
        try:
            self.page.locator(MtsThirdOnline.TARIFF_BUTTON).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подобрать тариф'.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Нажать на кнопку Подробнее")
    def click_more_details_button(self):
        try:
            self.page.locator(MtsThirdOnline.MORE_INFO_BUTTON).click()
        except Exception:
            raise AssertionError(
                "Не удалось нажать кнопку 'Подробнее'.\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве под баннером")
    def send_popup_application_check_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(FormApplicationCheckConnection.ADDRESS).fill("Тестоулица1111")
            except Exception:
                raise AssertionError("Не удалось ввести адрес в форму под баннером.")
            time.sleep(3)
            try:
                self.page.locator(FormApplicationCheckConnection.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон в форму под баннером.")
            time.sleep(3)
            try:
                self.page.locator(FormApplicationCheckConnection.CHECK_ADDRESS_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку 'Проверить адрес' в форме под баннером.")
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
            for name, locator in MtsThirdOnline.HEADER_LINKS.items():
                self.check_link(locator, f"Header: {name}")

            # Проверяем ссылки в футере
            for name, locator in MtsThirdOnline.FOOTER_LINKS.items():
                self.check_link(locator, f"Footer: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Открыть попап выбора")
    def other_city_popup_choice(self):
        try:
            self.page.locator(MTSHomeOnlineMain.ANOTHER_CITY_BUTTON).click()
        except Exception:
            raise AssertionError(
                "Не удалось открыть попап выбора города (кнопка 'Другой город').\n"
                "Возможно, кнопка недоступна или изменился селектор."
            )


class MTSRuPage(BasePage):
    @allure.title("Отправить заявку c баннера на первой странице")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(MtsRuLocators.ADDRESS_INPUT).fill("Тестулица")
            except Exception:
                raise AssertionError("Не удалось ввести адрес (MTS.ru).")
            try:
                self.page.locator(MtsRuLocators.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон (MTS.ru).")
            try:
                self.page.locator(MtsRuLocators.SEND_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку отправки (MTS.ru).")
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            except Exception:
                raise AssertionError("Не удалось ввести имя (MTS.ru тариф).")
            try:
                self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            except Exception:
                raise AssertionError("Не удалось ввести телефон (MTS.ru тариф).")
            try:
                self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            except Exception:
                raise AssertionError("Не удалось нажать кнопку отправки (MTS.ru тариф).")
            time.sleep(4)

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        try:
            return self.page.locator(MtsRuLocators.TARIFF_CARDS).all()
        except Exception:
            raise AssertionError("Не удалось получить список тарифных карточек (MTS.ru).")

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        try:
            self.page.locator(MtsRuLocators.TARIFF_CONNECT_BUTTONS).nth(card_index).click()
        except Exception:
            raise AssertionError(
                f"Не удалось нажать кнопку 'Подключить' на карточке тарифа #{card_index} (MTS.ru).\n"
                "Возможно, кнопка недоступна, перекрыта или изменился селектор."
            )