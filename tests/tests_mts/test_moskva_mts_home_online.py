import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from pages.page_mts.msk_mts_page import MtsMSKHomeOnlinePage
from playwright.sync_api import Error as PlaywrightError
from pages.page_mts.internet_mts_page import MtsInternetHomeOnlinePage
from pages.page_beel.beeline_page import BeelineOnlinePage, BeelineInternetOnlinePage, OnlineBeelinePage


@allure.feature("https://moskva.mts-home.online/")
class TestMoskvaMtsHomeOnline:

    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_msk_application_popup_super_offer(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(65)
        mts_page.check_popup_super_offer()
        time.sleep(2)
        online_page = BeelineOnlinePage(page=page)
        online_page.send_popup_super_offer_new_moscow()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("3. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_msk_application_popup_super_offer_red_button(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_on_red_button()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        online_page = BeelineOnlinePage(page=page)
        online_page.send_popup_super_offer_new_moscow()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("4. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_msk_application_popup_button_connect(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button()
        online_page = BeelineOnlinePage(page=page)
        online_page.send_popup_super_offer_new_address()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("5. Отправка заявки из попапа по кнопке Проверить адрес из хедера")
    def test_msk_application_popup_button_check_address(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_check_address_button()
        online_page = BeelineInternetOnlinePage(page=page)
        online_page.send_popup_application_connection_pro_new()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("6. Отправка заявки из попапа Заявка на подключение с кликабельного баннера")
    def test_msk_application_popup_clicable_banner(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        mts_page = MtsHomeOnlinePage(page=page)
        msk_page = MtsMSKHomeOnlinePage(page=page)
        msk_page.click_on_banner()
        online_page = BeelineOnlinePage(page=page)
        online_page.send_popup_super_offer_new_address()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("7. Отправка заявки со ВСЕХ форм на странице")
    def test_msk_application_from_all_forms(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        mts_page = MtsHomeOnlinePage(page=page)
        online = OnlineBeelinePage(page=page)
        online.send_popup_application_connection_home_new()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()
        time.sleep(3)
        online.send_popup_from_connection_home_new()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("8. Отправка заявок с карточек тарифа")
    def test_msk_application_from_tariff_cards(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        mts_page = MtsMSKHomeOnlinePage(page=page)
        tariff_cards = mts_page.get_tariff_cards()
        
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = mts_page.get_tariff_name(i)
                if tariff_name is None:
                    continue
                    
                mts_page.click_tariff_connect_button(i)
                time.sleep(3)
                mts_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                online = BeelineOnlinePage(page=page)
                online.send_popup_super_offer_new_address()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("9. Отправка заявки из попапа по кнопке Подключить из футера")
    def test_msk_application_popup_button_connect_futer(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button_futer()
        online_page = BeelineOnlinePage(page=page)
        online_page.send_popup_super_offer_new_address()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("10. Отправка заявки из попапа по кнопке Проверить адрес из футера")
    def test_msk_application_popup_button_check_address_futer(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_check_address_button_futer()
        online_page = BeelineInternetOnlinePage(page=page)
        online_page.send_popup_application_connection_pro_new()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("11. Проверка всех ссылок")
    def test_msk_check_all_pages(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        msk_page = MtsMSKHomeOnlinePage(page=page)
        msk_page.check_all_links()

    @allure.title("13.1. Выбор региона СПб из хедера")
    def test_msk_choose_region_header_spb(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        internet_page.click_region_choice_button_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать СПб"):
            time.sleep(5)
            region_page.fill_region_search_new("Санкт")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Санкт-Петербург")

    @allure.title("13.2. Выбор региона Азнакаево из хедера")
    def test_msk_choose_region_header_azn(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        mts_page = MtsHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            internet_page = MtsInternetHomeOnlinePage(page=page)
            internet_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Азнакаево")

    @allure.title("14.1. Выбор регион СПб из футера")
    def test_msk_choose_region_futer_spb(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        msk_page = MtsInternetHomeOnlinePage(page=page)
        msk_page.click_region_choice_button_futer_msk_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать СПб"):
            region_page.fill_region_search_new("Санкт")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Санкт-Петербург")

    @allure.title("14.2. Выбор региона Азнакаево из футера")
    def test_msk_choose_region_futer_azn(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)
        msk_page = MtsInternetHomeOnlinePage(page=page)
        msk_page.click_region_choice_button_futer_msk_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            region_page.fill_region_search_new("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Азнакаево")

    # @allure.title("15. Переход по всем ссылкам городов на странице выбора города")
    # def test_msk_check_all_city_links(self, page_fixture, second_url):
    #     page = page_fixture
    #     page.goto(second_url)
    #
    #     # Открываем страницу выбора города через хедер
    #     mts_page = MtsHomeOnlinePage(page=page)
    #     mts_page.click_region_choice_button()
    #
    #     # Проверяем все ссылки городов
    #     region_page = ChoiceRegionPage(page=page)
    #     region_page.check_all_city_links()

    @pytest.mark.skip("Пока не актуален, нет возможности проверить сценарий")
    @allure.title("16. Проверка формы 'Не нашли свой город?'")
    def test_msk_check_dont_find_city(self, page_fixture, second_url):
        page = page_fixture
        page.goto(second_url)

        # Открываем страницу выбора города через хедер
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button()

        # Работаем с формой "Не нашли свой город?"
        region_page = ChoiceRegionPage(page=page)
        region_page.click_button_dont_find_city()
        # region_page.close_popup_super_offer()
        time.sleep(4)
        region_page.send_form_dont_find_city()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()
        time.sleep(2)