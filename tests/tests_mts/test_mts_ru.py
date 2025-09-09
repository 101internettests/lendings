import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage, MTSSecondOnlinePage, MTSRuPage
from pages.page_mts.mts_home_online_page import MtsHomeOnlineSecondPage
from pages.page_mts.internet_mts_page import MtsInternetHomeOnlinePage
from pages.page_mts.mts_ru_page import MtsRuPage
from playwright.sync_api import Error as PlaywrightError


@allure.feature("http://mts-ru.ru/")
class TestMtsRu:
    @allure.title("1.1. Проверка работы сайта при отсутствии сертификата")
    def test_check_website_without_certificate(self, page_fixture, seven_url):
        with allure.step("Попытка открыть сайт без игнорирования ошибок SSL"):
            try:
                page = page_fixture
                page.goto(seven_url)
                time.sleep(5)
            except PlaywrightError as error:
                error_text = str(error)
                assert any(text in error_text.lower() for text in ["ssl", "certificate", "security"]), \
                    "Ожидалась ошибка SSL/сертификата"

    @pytest.mark.skip("Нужны правки")
    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer_third(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_second_page = MtsHomeOnlineSecondPage(page=page)
        time.sleep(25)
        mts_second_page.check_popup_super_offer()
        time.sleep(2)
        ru_page = MtsRuPage(page=page)
        ru_page.send_popup_super_offer()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("3. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_third_page = MTSSecondOnlinePage(page=page)
        mts_third_page.click_confirm_button()
        mts_page.click_on_red_button()
        mts_second_page = MtsHomeOnlineSecondPage(page=page)
        mts_second_page.check_popup_super_offer()
        time.sleep(2)
        ru_page = MtsRuPage(page=page)
        ru_page.send_popup_super_offer()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("4. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button()
        ru_page = MtsRuPage(page=page)
        ru_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("5. Отправка заявки из попапа Заявка на подключение с кликабельного баннера")
    def test_application_popup_clicable_banner(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_ru_page = MTSRuPage(page=page)
        mts_ru_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("6. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)
        mts_ru_page = MTSRuPage(page=page)
        mts_page = MtsHomeOnlinePage(page=page)
        tariff_cards = mts_ru_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = mts_page.get_tariff_name(i)
                mts_ru_page.click_tariff_connect_button(i)
                mts_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                mts_ru_page.send_tariff_connection_request()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
    #
    # @allure.title("6. Отправка заявки со ВСЕХ форм на странице")
    # def test_application_from_all_forms(self, page_fixture, seven_url):
    #     page = page_fixture
    #     page.goto(seven_url)
    #     mts_page = MtsHomeOnlinePage(page=page)
    #     mts_page.send_popup_application_check_connection()
    #     mts_page.check_sucess()
    #     mts_page.close_thankyou_page()
    #     time.sleep(3)
    #     mts_page.send_popup_application_check_connection_near_futer()
    #     mts_page.check_sucess()
    #     mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("7. Отправка заявки из попапа по кнопке Подробнее из банера с заголовком Акции от МТС")
    def test_application_popup_banner(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)
        mts_third_page = MTSSecondOnlinePage(page=page)
        mts_third_page.click_more_details_button()
        mts_page = MtsHomeOnlinePage(page=page)
        ru_page = MtsRuPage(page=page)
        ru_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title(
        "8. Отправка заявки с формы на странице с названием Проверьте возможность подключения по вашему адресу")
    def test_application_from_connection_form(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.send_popup_application_check_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("9. Отправка заявки из попапа по кнопке Подключить из футера")
    def test_application_popup_button_connect_futer(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button_futer()
        ru_page = MtsRuPage(page=page)
        ru_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("10. Отправка заявки из попапа по кнопке Проверить адрес из футера")
    def test_application_popup_button_check_address_futer(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_second_page = MtsHomeOnlineSecondPage(page=page)
        mts_second_page.click_check_address_button_futer()
        mts_page.send_popup_application_connection_your_address()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("11. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)
        mts_second_page = MTSSecondOnlinePage(page=page)
        mts_second_page.check_all_links()

    @pytest.mark.skip("Нужны правки")
    @allure.title("12. Выбор региона Азнакаево из хедера")
    def test_choose_region_header_azn(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)
        region_page = ChoiceRegionPage(page=page)
        mts_second_page = MtsHomeOnlineSecondPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            mts_second_page.click_region_choice_button()
            time.sleep(3)
            region_page.fill_region_search("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()

    @pytest.mark.skip("Нужны правки")
    @allure.title("13. Выбор региона Азнакаево из футера")
    def test_choose_region_futer_azn(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)
        mts_second_page = MtsHomeOnlineSecondPage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            mts_second_page.click_region_choice_button_futer()
            time.sleep(3)
            region_page.fill_region_search("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
    #
    # @allure.title("12. Переход по всем ссылкам городов на странице выбора города")
    # def test_check_all_city_links(self, page_fixture, seven_url):
    #     page = page_fixture
    #     page.goto(seven_url)
    #
    #     # Открываем страницу выбора города через хедер
    #     mts_second_page = MtsHomeOnlineSecondPage(page=page)
    #     mts_second_page.click_region_choice_button()
    #
    #     # Проверяем все ссылки городов
    #     region_page = ChoiceRegionPage(page=page)
    #     region_page.check_all_city_links()

    @pytest.mark.skip("Пока не актуален, нет возможности проверить сценарий")
    @allure.title("15. Проверка формы 'Не нашли свой город?'")
    def test_check_dont_find_city(self, page_fixture, seven_url):
        page = page_fixture
        page.goto(seven_url)

        # Открываем страницу выбора города через хедер
        mts_page = MtsHomeOnlinePage(page=page)
        mts_second_page = MtsHomeOnlineSecondPage(page=page)
        mts_second_page.click_region_choice_button()

        # Работаем с формой "Не нашли свой город?"
        region_page = ChoiceRegionPage(page=page)
        region_page.click_button_dont_find_city()
        region_page.close_popup_super_offer()
        time.sleep(2)
        mts_second_page.send_form_dont_find_city()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()
        time.sleep(2)