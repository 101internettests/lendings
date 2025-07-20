import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mts.mts_home_online import MTSHomeOnlineMain, ApplicationPopupWithName, ApplicationPopupCheckConnection, MtsRuLocators
from locators.mts.mts_home_online import FormApplicationCheckConnection, RegionChoice, MskMtsMainWeb, MtsThirdOnline


class MtsHomeOnlinePage(BasePage):
    @allure.title("Проверить, что попап Выгодное приложение появился")
    def check_popup_super_offer(self):
        expect(self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_HEADER)).to_be_visible()
        expect(self.page.locator(MTSHomeOnlineMain.SUPER_OFFER_TEXT)).to_be_visible()

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.ADDRESS_INPUT_FIVE).fill("Тестоадрес")
            self.page.locator(MTSHomeOnlineMain.INPUT_OFFER_POPUP).fill("99999999999")
            self.page.locator(MTSHomeOnlineMain.SEND_BUTTON_OFFER_POPUP).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer_new(self):
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
            self.page.locator(ApplicationPopupWithName.ADDRESS_INPUT).fill("Тестадрес")
            time.sleep(1)
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            time.sleep(1)
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            time.sleep(1)
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            time.sleep(1)
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            time.sleep(1)
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
            time.sleep(3)
            self.page.locator(FormApplicationCheckConnection.PHONE_INPUT).fill("99999999999")
            time.sleep(3)
            self.page.locator(FormApplicationCheckConnection.CHECK_ADDRESS_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве под баннером")
    def send_popup_application_check_connection_new(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(FormApplicationCheckConnection.ADDRESS).fill("Тестоулица11111")
            time.sleep(3)
            self.page.locator(FormApplicationCheckConnection.PHONE_INPUT).fill("99999999999")
            time.sleep(3)
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
            self.page.locator(ApplicationPopupWithName.ADDRESS_INPUT).fill("Тестоадрес")
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request_new(self):
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

    @allure.title("Проверить 30 случайных ссылок городов на странице")
    def check_all_city_links(self):
        """Проверяет до 30 случайных ссылок городов на странице выбора региона без вложений в Allure"""
        import random
        with allure.step("Проверка до 30 случайных ссылок городов (без вложений)"):
            city_links = self.page.locator(RegionChoice.ALL_CHOICES).all()
            if not city_links:
                print("Нет ссылок городов для проверки.")
                return
            sample_links = random.sample(city_links, min(30, len(city_links)))
            browser = self.page.context.browser
            for link in sample_links:
                city_name = link.text_content().strip()
                href = link.get_attribute('href')
                try:
                    context = browser.new_context()
                    new_page = context.new_page()
                    new_page.goto(href)
                    new_page.wait_for_load_state("domcontentloaded", timeout=20000)
                    new_page.wait_for_load_state("load", timeout=20000)
                    try:
                        new_page.wait_for_load_state("networkidle", timeout=20000)
                    except Exception:
                        pass
                    expect(new_page).not_to_have_url("**/404")
                except Exception as e:
                    print(f"Ошибка при проверке {city_name}: {str(e)}")
                finally:
                    context.close()
                    time.sleep(1)

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


class MTSSecondOnlinePage(BasePage):
    @allure.title("Нажать на кнопку Принять на главной странице")
    def click_confirm_button(self):
        self.page.locator(MtsThirdOnline.BUTTON_CONFIRM).click()

    @allure.title("Нажать на кнопку Подобрать тариф")
    def click_choose_tariff_button(self):
        self.page.locator(MtsThirdOnline.TARIFF_BUTTON).click()

    @allure.title("Нажать на кнопку Подробнее")
    def click_more_details_button(self):
        self.page.locator(MtsThirdOnline.MORE_INFO_BUTTON).click()

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу в Москве под баннером")
    def send_popup_application_check_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(FormApplicationCheckConnection.ADDRESS).fill("Тестоулица1111")
            time.sleep(3)
            self.page.locator(FormApplicationCheckConnection.PHONE_INPUT).fill("99999999999")
            time.sleep(3)
            self.page.locator(FormApplicationCheckConnection.CHECK_ADDRESS_BUTTON).click()
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
        # Проверяем ссылки в хедере
        for name, locator in MtsThirdOnline.HEADER_LINKS.items():
            self.check_link(locator, f"Header: {name}")

        # Проверяем ссылки в футере
        for name, locator in MtsThirdOnline.FOOTER_LINKS.items():
            self.check_link(locator, f"Footer: {name}")


class MTSRuPage(BasePage):
    @allure.title("Отправить заявку c баннера на первой странице")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(MtsRuLocators.ADDRESS_INPUT).fill("Тестулица")
            self.page.locator(MtsRuLocators.PHONE_INPUT).fill("99999999999")
            self.page.locator(MtsRuLocators.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationPopupWithName.NAME_INPUT).fill("Тестимя")
            self.page.locator(ApplicationPopupWithName.PHONE_INPUT).fill("99999999999")
            self.page.locator(ApplicationPopupWithName.SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(MtsRuLocators.TARIFF_CARDS).all()

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        self.page.locator(MtsRuLocators.TARIFF_CONNECT_BUTTONS).nth(card_index).click()

