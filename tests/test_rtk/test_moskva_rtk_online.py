import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_mts.internet_mts_page import MtsInternetHomeOnlinePage
from pages.page_rtk.rostel_page import RostelecomPage
from pages.page_beel.beeline_page import OnlineBeelinePage
from conftest import check_page_status_code


@allure.feature("https://moskva.rtk-ru.online/")
class TestMoskvaRTKOnline:
    @allure.title("1.1. Проверка работы сайта при отсутствии сертификата")
    def test_check_website_without_certificate(self, page_fixture, msk_rtk_online):
        with allure.step("Попытка открыть сайт без игнорирования ошибок SSL"):
            try:
                page = page_fixture
                page.goto(msk_rtk_online)
                time.sleep(5)
            except PlaywrightError as error:
                error_text = str(error)
                assert any(text in error_text.lower() for text in ["ssl", "certificate", "security"]), \
                    "Ожидалась ошибка SSL/сертификата"

    @allure.title("3. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self, page_fixture, msk_rtk_online):
        page = page_fixture
        page.goto(msk_rtk_online)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_on_purple_button()
        internet_page.check_popup_super_offer()
        time.sleep(2)
        rostelecom_page.send_popup_application_connection_home_new_five()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("4. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect(self, page_fixture, msk_rtk_online):
        page = page_fixture
        page.goto(msk_rtk_online)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button()
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(5)
        rostelecom_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("5. Отправка заявки из попапа Заявка на подключение с  кнопки Подключиться в баннере с заголовком "
                  "Подключить домашний интернет Ростелеком")
    def test_application_popup_button_application_two(self, page_fixture, msk_rtk_online):
        page = page_fixture
        page.goto(msk_rtk_online)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_connect_banner_button()
        rostelecom_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("6. Отправка заявки со ВСЕХ  форм на странице с названием Проверить возможность подключения "
                  "Ростелеком по вашему адресу")
    def test_application_popup_all_forms(self, page_fixture, msk_rtk_online):
        page = page_fixture
        page.goto(msk_rtk_online)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        with allure.step("Проверить возможность подключения Ростелеком по вашему адресу в Москве около хедера"):
            rostelecom_page.send_popup_application_connection_header()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()
        with allure.step("Проверить возможность подключения Ростелеком по вашему адресу в Москве около футера"):
            rostelecom_page.send_popup_application_connection_futer()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("7. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, msk_rtk_online):
        page = page_fixture
        page.goto(msk_rtk_online)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        tariff_cards = rostelecom_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = rostelecom_page.get_tariff_name(i)
                rostelecom_page.click_tariff_connect_button(i)
                rostelecom_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                nternet_page = MtsInternetHomeOnlinePage(page=page)
                rostelecom_page.send_tariff_connection_request()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("8. Отправка заявки из попапа Заявка на подключение с  кнопки Подключиться в баннере с заголовком "
                  "Как подключить домашний интернет Ростелеком")
    def test_application_popup_button_application_rostelecom(self, page_fixture, msk_rtk_online):
        page = page_fixture
        page.goto(msk_rtk_online)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_connect_banner_button_middle()
        rostelecom_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("9. Отправка заявки из попапа по кнопке Подключить из футера")
    def test_application_popup_button_connect_futer(self, page_fixture, msk_rtk_online):
        page = page_fixture
        page.goto(msk_rtk_online)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button_futer()
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(5)
        rostelecom_page.send_popup_application_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("10. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, msk_rtk_online):
        page = page_fixture
        page.goto(msk_rtk_online)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.check_all_links()

    @allure.title("11. Выбор региона Азнакаево из хедера")
    def test_choose_region_header_spb(self, page_fixture, msk_rtk_online):
        page = page_fixture
        page.goto(msk_rtk_online)
        mts_page = MtsHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Санкт-Петербург"):
            internet_page = MtsInternetHomeOnlinePage(page=page)
            internet_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Санкт")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Санкт-Петербург")


@allure.feature("https://moskva.rtk-ru.online/domashnij-internet")
class TestMoskvaRTKOnlineHomeInternet:
    @pytest.mark.skip("Нужны правки")
    @allure.title("15. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button_home(self, page_fixture, msk_rtk_online_home_inter):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_on_purple_button()
        internet_page.check_popup_super_offer()
        time.sleep(2)
        rostelecom_page.send_popup_application_connection_home_new_four()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("16. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect_home(self, page_fixture, msk_rtk_online_home_inter):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter)
        mts_page = MtsHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        # region_page.close_popup_super_offer()
        mts_page.click_connect_button()
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(5)
        rostelecom_page.send_popup_application_connection_futer_dom()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("17. Отправка заявки из попапа Заявка на подключение с  кнопки Подключиться в баннере с заголовком "
                  "Подключить домашний интернет Ростелеком")
    def test_application_popup_button_application_two(self, page_fixture, msk_rtk_online_home_inter):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_connect_banner_button()
        rostelecom_page.send_popup_application_connection_futer_dom()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("18. Отправка заявки со формы на странице с названием Подключить интернет Ростелеком в Москве")
    def test_application_popup_all_forms(self, page_fixture, msk_rtk_online_home_inter):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        with allure.step("Проверить возможность подключения Ростелеком по вашему адресу в Москве около хедера"):
            rostelecom_page.send_popup_application_connection_header()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("19. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, msk_rtk_online_home_inter):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        tariff_cards = rostelecom_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = rostelecom_page.get_tariff_name_dom(i)
                rostelecom_page.click_tariff_connect_button(i)
                rostelecom_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                nternet_page = MtsInternetHomeOnlinePage(page=page)
                rostelecom_page.send_tariff_connection_request_dom()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @pytest.mark.skip("Нужны правки")
    @allure.title("20. Отправка заявки из попапа Заявка на подключение с  кнопки Подключиться в баннере с заголовком "
                  "Как подключить домашний интернет Ростелеком")
    def test_application_popup_button_application_rostelecom(self, page_fixture, msk_rtk_online_home_inter):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_connect_banner_button_middle()
        rostelecom_page.send_popup_application_connection_futer_dom()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("21. Отправка заявки из попапа по кнопке Подключить из футера")
    def test_application_popup_button_connect_futer(self, page_fixture, msk_rtk_online_home_inter):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button_futer()
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(5)
        rostelecom_page.send_popup_application_connection_futer_dom()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()


@allure.feature("https://moskva.rtk-ru.online/internet-tv")
class TestMoskvaRTKOnlineHomeInternetTV:
    @allure.title("15. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button_home(self, page_fixture, msk_rtk_online_home_inter_tv):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_on_purple_button()
        internet_page.check_popup_super_offer()
        time.sleep(2)
        rostelecom_page.send_popup_application_connection_home_new_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("16. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect_home(self, page_fixture, msk_rtk_online_home_inter_tv):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        # region_page.close_popup_super_offer()
        mts_page.click_connect_button()
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(5)
        rostelecom_page.send_popup_application_connection_futer_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("17. Отправка заявки из попапа Заявка на подключение с  кнопки Подключиться в баннере с заголовком "
                  "Подключить домашний интернет Ростелеком")
    def test_application_popup_button_application_two(self, page_fixture, msk_rtk_online_home_inter_tv):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_connect_banner_button()
        rostelecom_page.send_popup_application_connection_futer_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("18. Отправка заявкy со формы на странице с названием Подключить интернет и телевидение Ростелеком по вашему адресу в Москве")
    def test_application_popup_all_forms(self, page_fixture, msk_rtk_online_home_inter_tv):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        with allure.step("Проверить возможность подключения Ростелеком по вашему адресу в Москве около хедера"):
            rostelecom_page.send_popup_application_connection_header()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("19. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, msk_rtk_online_home_inter_tv):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        tariff_cards = rostelecom_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = rostelecom_page.get_tariff_name_dom(i)
                rostelecom_page.click_tariff_connect_button(i)
                rostelecom_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                nternet_page = MtsInternetHomeOnlinePage(page=page)
                rostelecom_page.send_tariff_connection_request_tv()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("20. Отправка заявки из попапа Заявка на подключение с  кнопки Подключиться в баннере с заголовком "
                  "Как подключить домашний интернет Ростелеком")
    def test_application_popup_button_application_rostelecom(self, page_fixture, msk_rtk_online_home_inter_tv):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_connect_banner_button_middle()
        rostelecom_page.send_popup_application_connection_futer_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("21. Отправка заявки из попапа по кнопке Подключить из футера")
    def test_application_popup_button_connect_futer(self, page_fixture, msk_rtk_online_home_inter_tv):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button_futer()
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(5)
        rostelecom_page.send_popup_application_connection_futer_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()


@allure.feature("https://moskva.rtk-ru.online/internet-tv-mobile")
class TestMoskvaRTKOnlineHomeInternetTVmobile:
    @allure.title("15. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button_home(self, page_fixture, msk_rtk_online_home_inter_tv_mobile):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv_mobile)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_on_purple_button()
        internet_page.check_popup_super_offer()
        time.sleep(2)
        rostelecom_page.send_popup_application_connection_home_new_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("16. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect_home(self, page_fixture, msk_rtk_online_home_inter_tv_mobile):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv_mobile)
        mts_page = MtsHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        # region_page.close_popup_super_offer()
        mts_page.click_connect_button()
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(5)
        rostelecom_page.send_popup_application_connection_futer_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("17. Отправка заявки из попапа Заявка на подключение с  кнопки Подключиться в баннере с заголовком "
                  "Подключить домашний интернет Ростелеком")
    def test_application_popup_button_application_two(self, page_fixture, msk_rtk_online_home_inter_tv_mobile):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv_mobile)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_connect_banner_button()
        rostelecom_page.send_popup_application_connection_futer_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("18. Отправка заявкy со формы на странице с названием Подключить интернет и телевидение Ростелеком по вашему адресу в Москве")
    def test_application_popup_all_forms(self, page_fixture, msk_rtk_online_home_inter_tv_mobile):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv_mobile)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        with allure.step("Проверить возможность подключения Ростелеком по вашему адресу в Москве около хедера"):
            rostelecom_page.send_popup_application_connection_header()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("19. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, msk_rtk_online_home_inter_tv_mobile):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv_mobile)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        tariff_cards = rostelecom_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = rostelecom_page.get_tariff_name_dom(i)
                rostelecom_page.click_tariff_connect_button(i)
                rostelecom_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                nternet_page = MtsInternetHomeOnlinePage(page=page)
                rostelecom_page.send_tariff_connection_request_tv()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("20. Отправка заявки из попапа Заявка на подключение с  кнопки Подключиться в баннере с заголовком "
                  "Как подключить домашний интернет Ростелеком")
    def test_application_popup_button_application_rostelecom(self, page_fixture, msk_rtk_online_home_inter_tv_mobile):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv_mobile)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_connect_banner_button_middle()
        rostelecom_page.send_popup_application_connection_futer_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("21. Отправка заявки из попапа по кнопке Подключить из футера")
    def test_application_popup_button_connect_futer(self, page_fixture, msk_rtk_online_home_inter_tv_mobile):
        page = page_fixture
        page.goto(msk_rtk_online_home_inter_tv_mobile)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button_futer()
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(5)
        rostelecom_page.send_popup_application_connection_futer_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()


@allure.feature("https://moskva.rtk-ru.online/all-tariffs")
class TestMoskvaRTKOnlineHomeAllTariffs:
    @allure.title("15. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button_home(self, page_fixture, msk_rtk_online_home_tariffs):
        page = page_fixture
        page.goto(msk_rtk_online_home_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_on_purple_button()
        internet_page.check_popup_super_offer()
        time.sleep(2)
        rostelecom_page.send_popup_application_connection_home_new_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("16. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect_home(self, page_fixture, msk_rtk_online_home_tariffs):
        page = page_fixture
        page.goto(msk_rtk_online_home_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        # region_page.close_popup_super_offer()
        mts_page.click_connect_button()
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(5)
        rostelecom_page.send_popup_application_connection_futer_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("17. Отправка заявки из попапа Заявка на подключение с  кнопки Подключиться в баннере с заголовком "
                  "Подключить домашний интернет Ростелеком")
    def test_application_popup_button_application_two(self, page_fixture, msk_rtk_online_home_tariffs):
        page = page_fixture
        page.goto(msk_rtk_online_home_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_connect_banner_button()
        rostelecom_page.send_popup_application_connection_futer_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("18. Отправка заявкy со формы на странице с названием Подключить интернет и телевидение Ростелеком по вашему адресу в Москве")
    def test_application_popup_all_forms(self, page_fixture, msk_rtk_online_home_tariffs):
        page = page_fixture
        page.goto(msk_rtk_online_home_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        with allure.step("Проверить возможность подключения Ростелеком по вашему адресу в Москве около хедера"):
            rostelecom_page.send_popup_application_connection_header()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("19. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, msk_rtk_online_home_tariffs):
        page = page_fixture
        page.goto(msk_rtk_online_home_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        tariff_cards = rostelecom_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = rostelecom_page.get_tariff_name(i)
                rostelecom_page.click_tariff_connect_button(i)
                rostelecom_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                nternet_page = MtsInternetHomeOnlinePage(page=page)
                rostelecom_page.send_tariff_connection_request_tv()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("20. Отправка заявки из попапа Заявка на подключение с  кнопки Подключиться в баннере с заголовком "
                  "Как подключить домашний интернет Ростелеком")
    def test_application_popup_button_application_rostelecom(self, page_fixture, msk_rtk_online_home_tariffs):
        page = page_fixture
        page.goto(msk_rtk_online_home_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.click_connect_banner_button_middle()
        rostelecom_page.send_popup_application_connection_futer_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("21. Отправка заявки из попапа по кнопке Подключить из футера")
    def test_application_popup_button_connect_futer(self, page_fixture, msk_rtk_online_home_tariffs):
        page = page_fixture
        page.goto(msk_rtk_online_home_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button_futer()
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(5)
        rostelecom_page.send_popup_application_connection_futer_tv()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()