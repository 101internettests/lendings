import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_mts.internet_mts_page import MtsInternetHomeOnlinePage


class TestInternetMtsHome:
    @allure.title("1.1. Проверка работы сайта при отсутствии сертификата")
    def test_check_website_without_certificate(self, page_fixture, five_url):
        with allure.step("Попытка открыть сайт без игнорирования ошибок SSL"):
            try:
                page = page_fixture
                page.goto(five_url)
                time.sleep(5)
            except PlaywrightError as error:
                error_text = str(error)
                assert any(text in error_text.lower() for text in ["ssl", "certificate", "security"]), \
                    "Ожидалась ошибка SSL/сертификата"
                with allure.step("Создание скриншота и сохранение данных об ошибке"):
                    screenshot = page.screenshot(
                        full_page=True,
                        type='png'
                    )
                    allure.attach(
                        screenshot,
                        name="SSL Error Screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
                    allure.attach(
                        error_text,
                        name="SSL Error Details",
                        attachment_type=allure.attachment_type.TEXT
                    )

    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(15)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        internet_page.check_popup_super_offer()
        time.sleep(2)
        internet_page.send_popup_super_offer()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("3. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        internet_page.click_on_accept()
        mts_page.click_on_red_button()
        internet_page.check_popup_super_offer()
        time.sleep(2)
        internet_page.send_popup_super_offer()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("4. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button()
        internet_page = MtsInternetHomeOnlinePage(page=page)
        internet_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("5. Отправка заявки из попапа по кнопке Проверить адрес из хедера")
    def test_application_popup_button_check_address(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_check_address_button()
        internet_page = MtsInternetHomeOnlinePage(page=page)
        internet_page.send_popup_application_connection_your_address()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("6. Отправка заявки из попапа Заявка на подключение с кликабельного баннера")
    def test_application_popup_clicable_banner(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        internet_page.click_on_banner()
        internet_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("7. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)
        mts_page = MtsHomeOnlinePage(page=page)
        tariff_cards = mts_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = mts_page.get_tariff_name(i)
                mts_page.click_tariff_connect_button(i)
                mts_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                nternet_page = MtsInternetHomeOnlinePage(page=page)
                nternet_page.send_tariff_connection_request()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @allure.title(
        "8. Отправка заявки с формы на странице с названием Проверьте возможность подключения по вашему адресу")
    def test_application_from_all_forms(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.send_popup_application_check_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("9. Отправка заявки из попапа по кнопке Подключить из футера")
    def test_application_popup_button_connect_futer(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button_futer()
        internet_page = MtsInternetHomeOnlinePage(page=page)
        internet_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("10. Отправка заявки из попапа по кнопке Проверить адрес из футера")
    def test_application_popup_button_check_address_futer(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_check_address_button_futer()
        internet_page = MtsInternetHomeOnlinePage(page=page)
        internet_page.send_popup_application_connection_your_address()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("11. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        internet_page.check_all_links()

    @allure.title("13. Выбор региона Азнакаево из хедера")
    def test_choose_region_header_azn(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)
        mts_page = MtsHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            internet_page = MtsInternetHomeOnlinePage(page=page)
            internet_page.click_region_choice_button()
            region_page.fill_region_search("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text("Азнакаево")

    @allure.title("14. Выбор региона Азнакаево из футера")
    def test_choose_region_futer_azn(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)
        mts_page = MtsHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            internet_page = MtsInternetHomeOnlinePage(page=page)
            internet_page.click_region_choice_button_futer()
            region_page.fill_region_search("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text("Азнакаево")

    # @allure.title("15. Переход по всем ссылкам городов на странице выбора города")
    # def test_check_all_city_links(self, page_fixture, five_url):
    #     page = page_fixture
    #     page.goto(five_url)
    #
    #     # Открываем страницу выбора города через хедер
    #     internet_page = MtsInternetHomeOnlinePage(page=page)
    #     internet_page.click_region_choice_button()
    #
    #     # Проверяем все ссылки городов
    #     region_page = ChoiceRegionPage(page=page)
    #     region_page.check_all_city_links()

    @allure.title("16. Проверка формы 'Не нашли свой город?'")
    def test_check_dont_find_city(self, page_fixture, five_url):
        page = page_fixture
        page.goto(five_url)

        # Открываем страницу выбора города через хедер
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        internet_page.click_region_choice_button()

        # Работаем с формой "Не нашли свой город?"
        region_page = ChoiceRegionPage(page=page)
        region_page.click_button_dont_find_city()
        region_page.close_popup_super_offer()
        time.sleep(4)
        region_page.send_form_dont_find_city()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()
        time.sleep(2)