import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain, ApplicationPopupWithName, ApplicationPopupCheckConnection
from locators.mts.mts_home_online import FormApplicationCheckConnection, RegionChoice, MskMtsMainWeb


class MtsGponHomeOnlinePage(BasePage):
    @allure.title("Проверить, что попап Выгодное приложение появился")
    def check_popup_super_offer(self):
        expect(self.page.locator(MskMtsMainWeb.SUPER_OFFER_HEADER)).to_be_visible()
        expect(self.page.locator(MskMtsMainWeb.SUPER_OFFER_TEXT)).to_be_visible()

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(MskMtsMainWeb.INPUT_OFFER_POPUP).fill("99999999999")
            self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)

    @allure.title("Нажать на кнопку Подключить")
    def click_connect_button(self):
        self.page.locator(MskMtsMainWeb.CONNECT_BUTTON).click()

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(MskMtsMainWeb.PHONE_INPUT_OTHER).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Нажать на кнопку Проверить адрес")
    def click_check_address_button(self):
        self.page.locator(MskMtsMainWeb.CHECK_ADDRESS_BUTTON).click()

    @allure.title("Нажать на кнопку Проверить адрес из футера")
    def click_check_address_button_futer(self):
        self.page.locator(MskMtsMainWeb.CHECK_ADDRESS_BUTTON_FUTER).click()

    @allure.title(
        "Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве в конце страницы")
    def send_popup_application_check_connection_near_futer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(FormApplicationCheckConnection.ADDRESS_SECOND).fill("Тестимя")
            time.sleep(3)
            self.page.locator(ApplicationPopupCheckConnection.PHONE_INPUT).fill("99999999999")
            time.sleep(3)
            self.page.locator(FormApplicationCheckConnection.CHECK_ADDRESS_BUTTON_SECOND).click()
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(MskMtsMainWeb.PHONE_INPUT_OTHER).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title(
        "Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве в конце страницы")
    def send_popup_application_check_connection_near_futer_another(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(MskMtsMainWeb.ADDRESS_SECOND).fill("Тестимя")
            time.sleep(3)
            self.page.locator(MskMtsMainWeb.PHONE_INPUT).fill("99999999999")
            time.sleep(3)
            self.page.locator(MskMtsMainWeb.CHECK_ADDRESS_BUTTON_SECOND).click()
            time.sleep(4)

    @allure.title("Проверить ссылку и убедиться, что страница существует")
    def check_link(self, locator, link_name):
        """
        Проверяет ссылку и убеждается, что страница существует
        :param locator: локатор ссылки
        :param link_name: название ссылки для отчета
        """
        with allure.step(f"Проверка ссылки {link_name}"):
            max_retries = 3
            retry_count = 0
            
            while retry_count < max_retries:
                try:
                    # Закрываем все возможные всплывающие окна
                    try:
                        # Пробуем закрыть основное всплывающее окно
                        popup = self.page.locator("#popup-lead-catcher")
                        if popup.is_visible():
                            # Сначала пробуем найти и кликнуть по кнопке закрытия
                            close_button = self.page.locator(MskMtsMainWeb.SUPER_OFFER_CLOSE)
                            if close_button.is_visible():
                                close_button.click(force=True)
                                time.sleep(2)
                            
                            # Если окно все еще видимо, пробуем удалить его через JavaScript
                            if popup.is_visible():
                                self.page.evaluate("""() => {
                                    const popup = document.querySelector('#popup-lead-catcher');
                                    if (popup) popup.remove();
                                }""")
                                time.sleep(1)
                    except Exception as e:
                        allure.attach(f"Не удалось закрыть всплывающее окно: {str(e)}", "warning")
                    
                    link = self.page.locator(locator)
                    expect(link).to_be_visible()
                    
                    # Получаем атрибут href перед кликом
                    href = link.get_attribute('href')
                    if not href:
                        allure.attach(f"Ссылка {link_name} не имеет атрибута href", "warning")
                        return
                    
                    # Прокручиваем к элементу перед кликом
                    link.scroll_into_view_if_needed()
                    time.sleep(2)  # Увеличиваем время ожидания после прокрутки
                    
                    # Пробуем кликнуть обычным способом
                    try:
                        link.click(modifiers=["Control"], timeout=30000)
                    except Exception as click_error:
                        allure.attach(f"Обычный клик не удался, пробуем через JavaScript: {str(click_error)}", "warning")
                        # Если обычный клик не удался, пробуем через JavaScript
                        self.page.evaluate("""(selector) => {
                            const element = document.querySelector(selector);
                            if (element) {
                                const event = new MouseEvent('click', {
                                    bubbles: true,
                                    cancelable: true,
                                    view: window,
                                    ctrlKey: true
                                });
                                element.dispatchEvent(event);
                            }
                        }""", locator)
                    
                    # Ждем новую страницу с увеличенным таймаутом
                    new_page = self.page.context.wait_for_event("page", timeout=30000)
                    new_page.wait_for_load_state("networkidle", timeout=30000)
                    
                    # Проверяем, что страница не 404
                    expect(new_page).not_to_have_url("**/404")
                    new_page.close()
                    return
                    
                except Exception as e:
                    retry_count += 1
                    if retry_count == max_retries:
                        allure.attach(f"Не удалось проверить ссылку {link_name} после {max_retries} попыток. Ошибка: {str(e)}", "error")
                        raise
                    time.sleep(2)  # Ждем перед повторной попыткой

    @allure.title("Проверить все ссылки на странице")
    def check_all_links(self):
        """Проверяет все ссылки в хедере и футере"""
        # Проверяем ссылки в хедере
        for name, locator in MskMtsMainWeb.HEADER_LINKS_GPON.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in MTSHomeOnlineMain.FOOTER_LINKS.items():
            self.check_link(locator, f"Footer: {name}")

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button_gpon(self):
        region_button = self.page.locator(MskMtsMainWeb.REGION_CHOICE_BUTTON_SECOND)
        region_button.click()
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в футере")
    def click_region_choice_button_futer_gpon(self):
        region_button = self.page.locator(MskMtsMainWeb.REGION_CHOICE_BUTTON_FUTER)
        region_button.click()
        time.sleep(2)

    @allure.title("Закрыть попап Выгодное предложение")
    def close_popup_super_offer(self):
        self.page.locator(MskMtsMainWeb.SUPER_OFFER_CLOSE).click()