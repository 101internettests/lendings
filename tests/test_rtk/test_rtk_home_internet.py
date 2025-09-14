import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_mts.internet_mts_page import MtsInternetHomeOnlinePage
from pages.page_rtk.rostel_page import RostelecomPage


@allure.feature("https://rtk-home-internet.ru/")
class TestRTKOHomeInternetRu:

    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, попапа ")
    def test_application_popup_super_offer(self, page_fixture, rtk_home_internet_ru):
        page = page_fixture
        page.goto(rtk_home_internet_ru)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(25)
        internet_page.check_popup_super_offer()
        time.sleep(2)
        rostelecom_page.send_popup_application_connection_home_new_five()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("3. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self, page_fixture, rtk_home_internet_ru):
        page = page_fixture
        page.goto(rtk_home_internet_ru)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_on_purple_button()
        internet_page.check_popup_super_offer()
        time.sleep(2)
        rostelecom_page.send_popup_application_connection_home_new_five()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Форма с багом")
    @allure.title("4. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect(self, page_fixture, rtk_home_internet_ru):
        page = page_fixture
        page.goto(rtk_home_internet_ru)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        mts_page.click_connect_button()
        time.sleep(5)
        rostelecom_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Форма с багом")
    @allure.title("5. Отправка заявки из попапа Заявка на подключение с  кнопки Подключиться в баннере с заголовком "
                  "Подключить домашний интернет Ростелеком")
    def test_application_popup_button_application_two(self, page_fixture, rtk_home_internet_ru):
        page = page_fixture
        page.goto(rtk_home_internet_ru)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        rostelecom_page.click_connect_banner_button()
        rostelecom_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("6. Отправка заявки со ВСЕХ  форм на странице")
    def test_application_popup_all_forms(self, page_fixture, rtk_home_internet_ru):
        page = page_fixture
        page.goto(rtk_home_internet_ru)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        with allure.step("Проверьте адрес подключения к Ростелекому"):
            rostelecom_page.send_popup_application_connection_online_rtk()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()
        with allure.step("Проверьте адрес подключения к Ростелекому"):
            rostelecom_page.send_popup_application_connection_online_rtk_second()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("7. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, rtk_home_internet_ru):
        page = page_fixture
        page.goto(rtk_home_internet_ru)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        tariff_cards = rostelecom_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = rostelecom_page.get_tariff_name_dom(i)
                rostelecom_page.click_tariff_connect_button(i)
                rostelecom_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                nternet_page = MtsInternetHomeOnlinePage(page=page)
                rostelecom_page.send_tariff_connection_request()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @pytest.mark.skip("Форма с багом")
    @allure.title("8. Отправка заявки из попапа Заявка на подключение с  кнопки Подключить в блоке на странице с заголовком Выгодные условия")
    def test_application_popup_button_connect_traid(self, page_fixture, rtk_home_internet_ru):
        page = page_fixture
        page.goto(rtk_home_internet_ru)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        mts_page.click_connect_button_good_traid()
        time.sleep(5)
        rostelecom_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Форма с багом")
    @allure.title("10. Отправка заявки из попапа по кнопке Подключить из футера")
    def test_application_popup_button_connect_futer(self, page_fixture, rtk_home_internet_ru):
        page = page_fixture
        page.goto(rtk_home_internet_ru)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        mts_page.click_connect_button()
        time.sleep(5)
        rostelecom_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("11. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, rtk_home_internet_ru):
        page = page_fixture
        page.goto(rtk_home_internet_ru)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.check_all_links_rtk()

    @allure.title("12. Выбор региона Абакан из хедера")
    def test_choose_region_header(self, page_fixture, rtk_home_internet_ru):
        page = page_fixture
        page.goto(rtk_home_internet_ru)
        mts_page = MtsHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        with allure.step("Выбрать Абакан"):
            internet_page = MtsInternetHomeOnlinePage(page=page)
            internet_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Абак")
            region_page.verify_first_region_choice("Абакан")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Абакан")