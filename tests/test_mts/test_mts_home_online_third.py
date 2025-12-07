import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage, MTSSecondOnlinePage
from pages.page_mts.mts_home_online_page import MtsHomeOnlineSecondPage
from pages.page_mts.internet_mts_page import MtsInternetHomeOnlinePage
from playwright.sync_api import Error as PlaywrightError
from pages.main_steps import MainSteps


@allure.feature("https://mts-internet.online/")
class TestMtsMskHomeOnlineThird:
    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer_third(self, page_fixture, six_url):
        page = page_fixture
        page.goto(six_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_second_page = MtsHomeOnlineSecondPage(page=page)
        mts_second_page.check_popup_super_offer()
        time.sleep(2)
        steps = MainSteps(page=page)
        steps.send_popup_profit()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("3. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, six_url):
        page = page_fixture
        page.goto(six_url)
        steps = MainSteps(page=page)
        steps.def_check_links_without_footer()

    @allure.title("4. Выбор региона Азнакаево из хедера")
    def test_choose_region_header(self, page_fixture, six_url):
        page = page_fixture
        page.goto(six_url)
        region_page = ChoiceRegionPage(page=page)
        mts_second_page = MtsHomeOnlineSecondPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            mts_second_page.click_region_choice_button_futer_new()
            time.sleep(2)
            region_page.fill_region_search_new("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text_updated("Азнакаево")

    @allure.title("5. Выбор региона Азнакаево из футера")
    def test_choose_region_futer(self, page_fixture, six_url):
        page = page_fixture
        page.goto(six_url)
        mts_second_page = MtsHomeOnlineSecondPage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            mts_second_page.click_region_choice_button_futer_new()
            region_page.fill_region_search_new("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text_updated("Азнакаево")

    @allure.title("6. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, six_url):
        page = page_fixture
        page.goto(six_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        # internet_page.check_popup_super_offer()
        region_page = ChoiceRegionPage(page=page)
        # region_page.close_popup_super_offer()
        mts_page.click_region_choice_button_mts()
        steps.check_random_beeline_cities()
