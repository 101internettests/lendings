import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_mts.internet_mts_page import MtsInternetHomeOnlinePage
from pages.page_rtk.rostel_page import RostelecomPage


@allure.feature("https://rtk-home.ru/")
class TestRTKHomeRUSecond:

    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, попапа ")
    def test_application_popup_super_offer(self, page_fixture, rtk_home_ru_second):
        page = page_fixture
        page.goto(rtk_home_ru_second)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(10)
        internet_page.check_popup_super_offer()
        time.sleep(2)
        rostelecom_page.send_popup_application_connection_home_new_five()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("3. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self, page_fixture, rtk_home_ru_second):
        page = page_fixture
        page.goto(rtk_home_ru_second)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_on_purple_button()
        internet_page.check_popup_super_offer()
        time.sleep(2)
        rostelecom_page.send_popup_application_connection_home_new_five()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("4. Отправка заявки из попапа по кнопке Подключиться из хедера")
    def test_application_popup_button_connect(self, page_fixture, rtk_home_ru_second):
        page = page_fixture
        page.goto(rtk_home_ru_second)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        mts_page.click_connecting_button()
        time.sleep(5)
        rostelecom_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("5. Отправка заявки с формы на странице с названием Подключить домашний интернет Ростелеком")
    def test_application_popup_form(self, page_fixture, rtk_home_ru_second):
        page = page_fixture
        page.goto(rtk_home_ru_second)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        rostelecom_page.send_popup_application_connection_online_rtk()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    # @allure.title("5. Отправка заявки из попапа Заявка на подключение с  кнопки Подключиться в баннере с заголовком "
    #               "Подключить домашний интернет Ростелеком")
    # def test_application_popup_button_application_two(self, page_fixture, rtk_home_ru_second):
    #     page = page_fixture
    #     page.goto(rtk_home_ru_second)
    #     mts_page = MtsHomeOnlinePage(page=page)
    #     rostelecom_page = RostelecomPage(page=page)
    #     time.sleep(15)
    #     rostelecom_page.close_popup()
    #     rostelecom_page.click_connect_banner_button()
    #     rostelecom_page.send_popup_application_connection()
    #     mts_page.check_sucess()
    #     mts_page.close_thankyou_page()

    @allure.title("6. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, rtk_home_ru_second):
        page = page_fixture
        page.goto(rtk_home_ru_second)
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

    @allure.title("7. Отправка заявки из попапа Заявка на подключение с  кнопок Узнайте больше о тарифах в блоке на странице с заголовком Акции от Ростелеком")
    def test_application_popup_button_connect_traid(self, page_fixture, rtk_home_ru_second):
        page = page_fixture
        page.goto(rtk_home_ru_second)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        mts_page.click_connect_button_good_traid()
        time.sleep(5)
        rostelecom_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("8. Оставьте заявку на подключение")
    def test_application_popup_leave_connection(self, page_fixture, rtk_home_ru_second):
        page = page_fixture
        page.goto(rtk_home_ru_second)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        with allure.step("Оставьте заявку на подключение"):
            rostelecom_page.send_popup_application_connection_online_rtk()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("9. Отправка заявки из попапа по кнопке Подключиться из футера")
    def test_application_popup_button_connect_futer(self, page_fixture, rtk_home_ru_second):
        page = page_fixture
        page.goto(rtk_home_ru_second)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        mts_page.click_connecting_button_second()
        time.sleep(5)
        rostelecom_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("10. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, rtk_home_ru_second):
        page = page_fixture
        page.goto(rtk_home_ru_second)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.check_all_links_rtk_home()

    @allure.title("11. Выбор региона Абакан из хедера")
    def test_choose_region_header(self, page_fixture, rtk_home_ru_second):
        page = page_fixture
        page.goto(rtk_home_ru_second)
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