import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass
from pages.page_beel.beeline_page import BeelineOnlinePage, OnlineBeelinePage, BeelineInternetOnlinePage


@allure.feature("https://online-beeline.ru/")
class TestOnlineBeeline:
    @allure.title("1. Выбор региона из всплывающего попапа Уточните ваш город")
    def test_choose_region_from_popup(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        domru_page = DomRuClass(page=page)
        online_beeline_page = OnlineBeelinePage(page=page)
        time.sleep(8)
        online_beeline_page.popup_choose_city_accept()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Аксай"):
            time.sleep(3)
            region_page.fill_region_search_new("Аксай")
            region_page.verify_first_region_choice("Аксай (Ростовская область)")
            region_page.select_first_region()
            time.sleep(3)
            domru_page.click_on_logo()
            region_page.verify_region_button_text_new("выбрать город")
            time.sleep(3)

    @allure.title("1.1. Проверка работы сайта при отсутствии сертификата")
    def test_check_website_without_certificate(self, page_fixture, online_beeline):
        with allure.step("Попытка открыть сайт без игнорирования ошибок SSL"):
            try:
                page = page_fixture
                page.goto(online_beeline)
                time.sleep(5)
            except PlaywrightError as error:
                error_text = str(error)
                assert any(text in error_text.lower() for text in ["ssl", "certificate", "security"]), \
                    "Ожидалась ошибка SSL/сертификата"

    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(8)
        domru_page = DomRuClass(page=page)
        online_beeline_page = OnlineBeelinePage(page=page)
        online_beeline_page.popup_choose_city()
        time.sleep(50)
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.send_popup_super_offer_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("3. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной желтой кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.close_coockies()
        mts_page.click_on_red_button()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page.send_popup_super_offer_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("4. Отправка заявки с каждой формы на странице с названиями: подключить тарифы билайн в Москве, "
                  "проверьте адрес подключения")
    def test_a_lot_of_forms(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        with allure.step("Проверить возможность подключения подключить тарифы билайн в Москве"):
            online_beeline_page = OnlineBeelinePage(page=page)
            online_beeline_page.send_popup_from_connection()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()
        with allure.step("Проверить возможность подключения проверьте адрес подключения"):
            online_beeline_page.send_popup_from_connection_second()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()

    @allure.title("5. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        beeline_page = BeelineOnlinePage(page=page)
        domru_page.close_popup_location()
        tariff_cards = beeline_page.get_tariff_cards_new()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                # tariff_name = beeline_page.get_tariff_name(i)
                page_beel = BeelineInternetOnlinePage(page=page)
                page_beel.click_tariff_connect_button(1 - i)
                # beeline_page.verify_popup_tariff_name_new(tariff_name)
                time.sleep(3)
                beeline_internet_page = BeelineInternetOnlinePage(page=page)
                beeline_internet_page.send_popup_application_connection_pro_new()
                mts_page.check_sucess()
                domru_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("6. Отправка заявки из попапа по кнопке Подключить из футер")
    def test_application_popup_button_connect_futer(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        online_beeline_page = OnlineBeelinePage(page=page)
        time.sleep(5)
        online_beeline_page.popup_choose_city()
        online_beeline_page.click_connect_button_futer()
        beeline_internet_page = BeelineInternetOnlinePage(page=page)
        beeline_internet_page.send_popup_application_connection_pro_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("7. Отправка заявки из попапа по кнопке быстрое подключение закрепленной на экране")
    def test_application_popup_button_fast(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        online_beeline_page = OnlineBeelinePage(page=page)
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.close_coockies()
        online_beeline_page.click_button_fast_connection()
        online_beeline_page.send_popup_application_connection_home_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("8. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_online_beeline()

    @allure.title("9. Выбор региона из хедера")
    def test_choose_region_header_spb(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.click_region_choice_button_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Аксай"):
            region_page.fill_region_search_new("Аксай")
            region_page.verify_first_region_choice("Аксай (Ростовская область)")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Аксай")

    # пока больше не актуален
    # @allure.title("11. Проверка формы 'Не нашли свой город?'")
    # def test_check_dont_find_city(self, page_fixture, online_beeline):
    #     page = page_fixture
    #     page.goto(online_beeline)
    #     domru_page = DomRuClass(page=page)
    #     online_beeline_page = OnlineBeelinePage(page=page)
    #     # Открываем страницу выбора города через хедер
    #     mts_page = MtsHomeOnlinePage(page=page)
    #     mts_page.click_region_choice_button()
    #
    #     region_page = ChoiceRegionPage(page=page)
    #     online_beeline_page.click_button_dont_find_city()
    #     # region_page.close_popup_super_offer()
    #     # time.sleep(4)
    #     region_page.send_form_dont_find_city()
    #     mts_page.check_sucess()
    #     domru_page.close_thankyou_page()
    #     time.sleep(2)