import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from pages.page_mts.mts_home_online_page import MtsHomeOnlineSecondPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_beel.beeline_page import BeelineOnlinePage,  BeelineInternetOnlinePage, OnlineBeelinePage
from pages.main_steps import MainSteps


@allure.feature("https://mts-home-online.ru/")
class TestMtsMskHomeOnlineSecond:
    @pytest.mark.skip("Нет попапа")
    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, four_url):
        page = page_fixture
        page.goto(four_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_second_page = MtsHomeOnlineSecondPage(page=page)
        mts_second_page.check_popup_super_offer()
        time.sleep(2)
        steps = MainSteps(page=page)
        steps.send_popup_profit()
        time.sleep(4)
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("3. Переход по всем ссылкам на странице")
    def test_check_all_pages(self, page_fixture, four_url):
        page = page_fixture
        page.goto(four_url)
        steps = MainSteps(page=page)
        steps.def_check_links_without_footer()

    @allure.title("4. Выбор региона Азнакаево из хедера")
    def test_choose_region_header(self, page_fixture, four_url):
        page = page_fixture
        page.goto(four_url)
        region_page = ChoiceRegionPage(page=page)
        mts_second_page = MtsHomeOnlineSecondPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            mts_second_page.click_region_choice_button_new_two()
            region_page.fill_region_search_new("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Азнакаево")

    @allure.title("5. Выбор региона Азнакаево из футера")
    def test_choose_region_futer(self, page_fixture, four_url):
        page = page_fixture
        page.goto(four_url)
        mts_second_page = MtsHomeOnlineSecondPage(page=page)
        mts_page = MtsHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            mts_second_page.click_region_choice_button_futer_new()
            region_page.fill_region_search_new("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Азнакаево")

    @allure.title("6. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, four_url):
        page = page_fixture
        page.goto(four_url)

        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        mts_page.click_region_choice_button_new()
        steps.check_random_beeline_cities()
