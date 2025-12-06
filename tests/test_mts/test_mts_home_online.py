import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_beel.beeline_page import BeelineOnlinePage, BeelineInternetOnlinePage, OnlineBeelinePage
from pages.main_steps import MainSteps


@allure.feature("https://mts-home.online/")
class TestMolMainRegionPage:
    @pytest.mark.skip("Нет попапа")
    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, base_url):
        page = page_fixture
        page.goto(base_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.check_popup_super_offer()
        time.sleep(2)
        steps = MainSteps(page=page)
        steps.send_popup_profit()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("3. Переход по всем ссылкам на странице домашнего интернета")
    def test_check_all_pages(self, page_fixture, base_url):
        page = page_fixture
        page.goto(base_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.check_all_links()

    @allure.title("4.1. Выбор региона СПб из хедера")
    def test_choose_region_header_spb(self, page_fixture, base_url):
        page = page_fixture
        page.goto(base_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать СПб"):
            region_page.fill_region_search_new("Санкт")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Санкт-Петербург")

    @allure.title("4.2. Выбор региона Азнакаево из хедера")
    def test_choose_region_header_azn(self, page_fixture, base_url):
        page = page_fixture
        page.goto(base_url)
        mts_page = MtsHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            mts_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Азнакаево")

    @allure.title("5.1. Выбор регион СПб из футера")
    def test_choose_region_futer_spb(self, page_fixture, base_url):
        page = page_fixture
        page.goto(base_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button_futer_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать СПб"):
            region_page.fill_region_search_new("Санкт")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Санкт-Петербург")

    @allure.title("5.2. Выбор региона Азнакаево из футера")
    def test_choose_region_futer_azn(self, page_fixture, base_url):
        page = page_fixture
        page.goto(base_url)
        mts_page = MtsHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            mts_page.click_region_choice_button_futer_new()
            time.sleep(3)
            region_page.fill_region_search_new("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Азнакаево")

    @allure.title("6. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, base_url):
        page = page_fixture
        page.goto(base_url)

        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)

        # 20 раз: открыть попап, кликнуть случайный город в этой же вкладке и проверить,
        # затем снова открыть попап
        for _ in range(20):
            mts_page.click_region_choice_button_new()
            steps.click_random_city_and_verify_same_tab()