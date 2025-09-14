import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass
from pages.page_beel.beeline_page import BeelineOnlinePage, OnlineBeelinePage, BeelineInternetOnlinePage


@allure.feature("https://beeline-ru.online/")
class TestBeelineOnline:
    @allure.title("1. Выбор региона из всплывающего попапа Вы находитесь в Москве?")
    def test_choose_region_from_popup(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        domru_page = DomRuClass(page=page)
        domru_page.choose_msk_location_new()
        time.sleep(2)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Санкт-Петербург"):
            region_page.fill_region_search_new("Санкт-Петербург")
            time.sleep(3)
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            time.sleep(3)
        with allure.step("Выбрать Аксай"):
            domru_page.choose_msk_location_new()
            time.sleep(3)
            region_page.fill_region_search_new("Аксай")
            region_page.verify_first_region_choice("Аксай (Ростовская область)")
            region_page.select_first_region()
            time.sleep(3)
            domru_page.close_popup_location()
            domru_page.click_on_logo()
            region_page.verify_region_button_text_new("Москва")
            time.sleep(3)

    @pytest.mark.skip("Попап не высвечивается")
    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(65)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page = BeelineOnlinePage(page=page)
        online_page = OnlineBeelinePage(page=page)
        online_page.send_popup_application_connection_home_new_five()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("3. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной желтой кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.close_coockies()
        mts_page.click_on_red_button()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        online_page = OnlineBeelinePage(page=page)
        online_page.send_popup_application_connection_home_new_five()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("4. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.click_connect_button()
        beeline_internet_page = BeelineInternetOnlinePage(page=page)
        beeline_internet_page.send_popup_application_connection_pro_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("5. Отправка заявки с каждой формы на странице с названиями: Подключите стабильный интернет, "
                  "Попробуйте скоростной безлимитный интернет")
    def test_a_lot_of_forms(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        online_beeline_page = OnlineBeelinePage(page=page)
        with allure.step("Проверить возможность подключения билайн по вашему адресу в Москве первый"):
            beeline_page = BeelineOnlinePage(page=page)
            online_beeline_page.send_popup_application_connection_home_new()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()
        with allure.step("Проверить возможность подключения билайн по вашему адресу в Москве второй"):
            online_beeline_page.send_popup_from_connection_home_new()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("6. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        beeline_page = BeelineOnlinePage(page=page)
        domru_page.close_popup_location()
        tariff_cards = beeline_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = beeline_page.get_tariff_name(i)
                beeline_page.click_tariff_connect_button(i)
                beeline_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                beeline_internet_page = BeelineInternetOnlinePage(page=page)
                beeline_internet_page.send_popup_application_connection_pro_new()
                mts_page.check_sucess()
                domru_page.close_thankyou_page()
                time.sleep(2)

    @pytest.mark.skip("Нужны правки")
    @allure.title("7. Отправка заявки из попапа по кнопке Подключить из футер")
    def test_application_popup_button_connect_futer(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.click_connect_button_futer()
        beeline_internet_page = BeelineInternetOnlinePage(page=page)
        beeline_internet_page.send_popup_application_connection_pro_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("8. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_sec()

    @allure.title("9. Выбор региона из хедера")
    def test_choose_region_header_spb(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.choose_msk_location_new()
        # mts_page.click_region_choice_button()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Санкт Петербург"):
            region_page.fill_region_search_new("Санк")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Санкт-Петербург")
            time.sleep(3)
        with allure.step("Выбрать Аксай"):
            domru_page.close_popup_location()
            mts_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Аксай")
            region_page.verify_first_region_choice("Аксай (Ростовская область)")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Аксай")

    @allure.title("10. Выбор региона из футера")
    def test_choose_region_futer_spb(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.click_region_choice_button_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Санкт Петербург"):
            region_page.fill_region_search_new("Санк")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            domru_page.close_popup_location()
            # region_page.verify_region_button_text("Санкт-Петербург")
            time.sleep(3)
        with allure.step("Выбрать Аксай"):
            # domru_page.close_popup_location()
            mts_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Аксай")
            region_page.verify_first_region_choice("Аксай (Ростовская область)")
            region_page.select_first_region()
            region_page.verify_region_button_text("Аксай")

    @pytest.mark.skip("Пока не актуален, нет возможности проверить сценарий")
    @allure.title("12. Проверка формы 'Не нашли свой город?'")
    def test_check_dont_find_city(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        # Открываем страницу выбора города через хедер
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button()

        # Работаем с формой "Не нашли свой город?"
        region_page = ChoiceRegionPage(page=page)
        region_page.click_button_dont_find_city()
        # region_page.close_popup_super_offer()
        # time.sleep(4)
        region_page.send_form_dont_find_city()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()
        time.sleep(2)