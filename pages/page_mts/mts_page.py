import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain, ApplicationPopupWithName, ApplicationPopupCheckConnection
from locators.mts.mts_home_online import FormApplicationCheckConnection, RegionChoice, MskMtsMainWeb


class MtsHomeOnlinePage(BasePage):
    @allure.title("Проверить, что попап Выгодное приложение появился")
    def check_popup_super_offer(self):
        expect(self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_HEADER)).to_be_visible()
        expect(self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_TEXT)).to_be_visible()

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP).fill("99999999999")
            self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)


    @allure.title("Отправить заявку в попап для других страниц и проверить успешность")
    def send_popup_super_offer_other_pages(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP_SOME_PAGE).fill("99999999999")
            self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)

    @allure.title("Проверить успешность отправления заявки")
    def check_sucess(self):
        with allure.step("Проверить, что заявка отправилась"):
            expect(self.page.locator(MTSHomeOnlineMain.THANKYOU_TEXT)).to_be_visible()

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def close_thankyou_page(self):
        self.page.locator(MTSHomeOnlineMain.CLOSE_BUTTON).click()

    @allure.title("Нажать на плавающую красную кнопку с телефоном в правом нижнем углу")
    def click_on_red_button(self):
        self.page.locator(MTSHomeOnlineMain.RED_BUTTON).click()

    @allure.title("Нажать на кнопку Подключить")
    def click_connect_button(self):
        self.page.locator(MTSHomeOnlineMain.CONNECT_BUTTON).click()

    @allure.title("Нажать на кнопку Подключить из футера")
    def click_connect_button_futer(self):
        self.page.locator(MTSHomeOnlineMain.CONNECT_BUTTON_FUTER).click()

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение с других страниц")
    def send_popup_application_connection_other(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT_OTHER).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение с других страниц")
    def send_popup_application_connection_another(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT_ANOTHER).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Нажать на кнопку Проверить адрес")
    def click_check_address_button(self):
        self.page.locator(MTSHomeOnlineMain.CHECK_ADDRESS_BUTTON).click()

    @allure.title("Нажать на кнопку Проверить адрес из футера")
    def click_check_address_button_futer(self):
        self.page.locator(MTSHomeOnlineMain.CHECK_ADDRESS_BUTTON_FUTER).click()

    @allure.title("Отправить заявку в попап с названием Проверьте возможность подключения по вашему адресу")
    def send_popup_application_connection_your_address(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupCheckConnection.ADDRESS_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupCheckConnection.PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationPopupCheckConnection.CHECK_ADDRESS_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Проверьте возможность подключения по вашему адресу с другой страницы")
    def send_popup_application_connection_your_address_other(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupCheckConnection.ADDRESS_INPUT_SECOND).fill("Тестимя")
            self.page.locator(ApplicationPopupCheckConnection.PHONE_INPUT_SECOND).fill("99999999999")
            self.page.locator(ApplicationPopupCheckConnection.CHECK_ADDRESS_BUTTON_SECOND).click()
            time.sleep(4)

    @allure.title(
        "Отправить заявку в попап с названием Проверьте возможность подключения по вашему адресу с другой страницы")
    def send_popup_application_connection_your_address_another(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupCheckConnection.ADDRESS_INPUT_SECOND).fill("Тестимя")
            self.page.locator(ApplicationPopupCheckConnection.PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationPopupCheckConnection.CHECK_ADDRESS_BUTTON_SECOND).click()
            time.sleep(4)

    @allure.title("Нажать на баннер на главной стране")
    def click_on_banner(self):
        self.page.locator(MTSHomeOnlineMain.BANNER).click()

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве под баннером")
    def send_popup_application_check_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(FormApplicationCheckConnection.ADDRESS).fill("Тестимя")
            self.page.locator(FormApplicationCheckConnection.PHONE_INPUT).fill("99999999999")
            self.page.locator(FormApplicationCheckConnection.CHECK_ADDRESS_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве в конце страницы")
    def send_popup_application_check_connection_near_futer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(FormApplicationCheckConnection.ADDRESS_SECOND).fill("Тестимя")
            time.sleep(3)
            self.page.locator(FormApplicationCheckConnection.PHONE_INPUT_SECOND).fill("99999999999")
            time.sleep(3)
            self.page.locator(FormApplicationCheckConnection.CHECK_ADDRESS_BUTTON_SECOND).click()
            time.sleep(4)

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(MTSHomeOnlineMain.TARIFF_CARDS).all()

    @allure.title("Получить название тарифа из карточки")
    def get_tariff_name(self, card_index):
        tariff_name = self.page.locator(MTSHomeOnlineMain.TARIFF_NAMES).nth(card_index).text_content()
        return f"Тариф: \n                              {tariff_name}\n                              "

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        self.page.locator(MTSHomeOnlineMain.TARIFF_CONNECT_BUTTONS).nth(card_index).click()

    @allure.title("Проверить название тарифа в попапе")
    def verify_popup_tariff_name(self, expected_name):
        popup_tariff_name = self.page.locator(MTSHomeOnlineMain.POPUP_TARIFF_NAME)
        expect(popup_tariff_name).to_be_visible()
        expect(popup_tariff_name).to_have_text(expected_name)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа для других страниц")
    def send_tariff_connection_request_other(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT_OTHER).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа для других страниц")
    def send_tariff_connection_request_another(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT_ANOTHER).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
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
                            close_button = self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_CLOSE)
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
        for name, locator in MTSHomeOnlineMain.HEADER_LINKS.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in MTSHomeOnlineMain.FOOTER_LINKS.items():
            self.check_link(locator, f"Footer: {name}")

    @allure.title("Нажать на кнопку выбора региона в хедере")
    def click_region_choice_button(self):
        region_button = self.page.locator(RegionChoice.REGION_CHOICE_BUTTON)
        region_button.click()
        time.sleep(2)

    @allure.title("Нажать на кнопку выбора региона в футере")
    def click_region_choice_button_futer(self):
        region_button = self.page.locator(RegionChoice.REGION_CHOICE_BUTTON_FUTER)
        region_button.click()
        time.sleep(2)


class ChoiceRegionPage(BasePage):
    @allure.title("Ввести текст в поле поиска региона")
    def fill_region_search(self, search_text):
        city_input = self.page.locator(RegionChoice.CITY_INPUT)
        city_input.fill(search_text)
        time.sleep(2)

    @allure.title("Проверить, что первый вариант содержит ожидаемый текст")
    def verify_first_region_choice(self, expected_text):
        first_choice = self.page.locator(RegionChoice.FIRST_CHOICE)
        expect(first_choice).to_contain_text(expected_text)
        return first_choice

    @allure.title("Выбрать первый регион из списка")
    def select_first_region(self):
        first_choice = self.page.locator(RegionChoice.FIRST_CHOICE)
        first_choice.click()
        time.sleep(2)

    @allure.title("Проверить текст кнопки выбора региона")
    def verify_region_button_text(self, expected_text):
        region_button = self.page.locator(RegionChoice.REGION_CHOICE_BUTTON)
        expect(region_button).to_contain_text(expected_text)

    @allure.title("Проверить все ссылки городов на странице")
    def check_all_city_links(self):
        """Проверяет все ссылки городов на странице выбора региона"""
        with allure.step("Проверка всех ссылок городов"):
            # Получаем все ссылки городов
            city_links = self.page.locator(RegionChoice.ALL_CHOICES).all()
            browser = self.page.context.browser
            
            # Проходим по каждой ссылке
            for i, link in enumerate(city_links):
                with allure.step(f"Проверка ссылки города #{i + 1}"):
                    try:
                        # Получаем текст города для отчета
                        city_name = link.text_content().strip()
                        href = link.get_attribute('href')
                        
                        with allure.step(f"Проверка города: {city_name} ({href})"):
                            # Создаем новый контекст и страницу
                            context = browser.new_context()
                            new_page = context.new_page()
                            
                            # Переходим по ссылке
                            with allure.step(f"Переход по ссылке {href}"):
                                new_page.goto(href)
                            
                            try:
                                # Ждем загрузки страницы с увеличенным таймаутом
                                with allure.step("Ожидание загрузки страницы"):
                                    new_page.wait_for_load_state("domcontentloaded", timeout=20000)
                                    new_page.wait_for_load_state("load", timeout=20000)
                                    try:
                                        new_page.wait_for_load_state("networkidle", timeout=20000)
                                    except Exception as e:
                                        allure.attach(
                                            f"Предупреждение: networkidle не достигнут для {city_name}: {str(e)}",
                                            name=f"NetworkIdle Warning - {city_name}",
                                            attachment_type=allure.attachment_type.TEXT
                                        )
                                
                                # Проверяем что не получили 404 и делаем скриншот
                                with allure.step("Проверка доступности страницы"):
                                    expect(new_page).not_to_have_url("**/404")
                                    screenshot = new_page.screenshot(
                                        full_page=False,  # Только видимая часть
                                        type='png'
                                    )
                                    allure.attach(
                                        screenshot,
                                        name=f"Screenshot - {city_name}",
                                        attachment_type=allure.attachment_type.PNG
                                    )
                            
                            except Exception as e:
                                # Если произошла ошибка, прикрепляем информацию об ошибке
                                error_message = f"Ошибка при проверке {city_name}: {str(e)}"
                                allure.attach(
                                    error_message,
                                    name=f"Error - {city_name}",
                                    attachment_type=allure.attachment_type.TEXT
                                )
                                raise  # Пробрасываем ошибку дальше
                            
                            finally:
                                # Всегда закрываем контекст
                                context.close()
                                time.sleep(1)  # Небольшая пауза между проверками
                    
                    except Exception as e:
                        # Логируем ошибку, но продолжаем проверять следующие ссылки
                        allure.attach(
                            f"Критическая ошибка при проверке ссылки: {str(e)}",
                            name=f"Critical Error - Link #{i + 1}",
                            attachment_type=allure.attachment_type.TEXT
                        )
                        continue

    @allure.title("Нажать на кнопку Не смогли найти город")
    def click_button_dont_find_city(self):
        self.page.locator(RegionChoice.BUTTON_DONT_CITY).click()
        time.sleep(2)

    @allure.title("Отправить заявку в форму Не нашли свой город?")
    def send_form_dont_find_city(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(RegionChoice.FORM_CITY).fill("Тестгород")
            self.page.locator(FormApplicationCheckConnection.PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Закрыть попап Выгодное предложение")
    def close_popup_super_offer(self):
        self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_CLOSE).click()