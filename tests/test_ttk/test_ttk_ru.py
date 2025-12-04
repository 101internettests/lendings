import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass
from pages.page_beel.beeline_page import BeelineOnlinePage, OnlineBeelinePage, BeelineInternetOnlinePage
from pages.main_steps import MainSteps


@allure.feature("https://ttk-internet.ru/")
class TestTTKInternet:
    @allure.title("1. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, ttk_internet):
        page = page_fixture
        page.goto(ttk_internet)
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_ttk()

    @allure.title("2. Выбор региона из хедера")
    def test_choose_region_header(self, page_fixture, ttk_internet):
        page = page_fixture
        page.goto(ttk_internet)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Екатеринбург"):
            region_page.fill_region_search_new("Ека")
            region_page.verify_first_region_choice("Екатеринбург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Екатеринбург")
            time.sleep(3)
        with allure.step("Выбрать click_region_choice_button_beeline"):
            mts_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Барн")
            region_page.verify_first_region_choice("Барнаул")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Барнаул")

    @allure.title("3. Выбор региона из футера")
    def test_choose_region_footer(self, page_fixture, ttk_internet):
        page = page_fixture
        page.goto(ttk_internet)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button_futer_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Екатеринбург"):
            region_page.fill_region_search_new("Ека")
            region_page.verify_first_region_choice("Екатеринбург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Екатеринбург")
            time.sleep(3)
        with allure.step("Выбрать click_region_choice_button_beeline"):
            mts_page.click_region_choice_button_futer_new()
            region_page.fill_region_search_new("Барн")
            region_page.verify_first_region_choice("Барнаул")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Барнаул")

    @allure.title("4. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, ttk_internet):
        page = page_fixture
        page.goto(ttk_internet)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)

        # 20 раз: открыть попап, кликнуть случайный город в этой же вкладке и проверить,
        # затем снова открыть попап
        for _ in range(20):
            mts_page.click_region_choice_button_new()
            steps.click_random_city_and_verify_same_tab_new()


@allure.feature("https://ttk-ru.online/")
class TestTTKRyOnline:
    @allure.title("1. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, ttk_online):
        page = page_fixture
        page.goto(ttk_online)
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_ttk()

    @allure.title("2. Выбор региона из хедера")
    def test_choose_region_header(self, page_fixture, ttk_online):
        page = page_fixture
        page.goto(ttk_online)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Екатеринбург"):
            region_page.fill_region_search_new("Ека")
            region_page.verify_first_region_choice("Екатеринбург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Екатеринбург")
            time.sleep(3)
        with allure.step("Выбрать click_region_choice_button_beeline"):
            mts_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Барн")
            region_page.verify_first_region_choice("Барнаул")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Барнаул")

    @allure.title("3. Выбор региона из футера")
    def test_choose_region_footer(self, page_fixture, ttk_online):
        page = page_fixture
        page.goto(ttk_online)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button_futer_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Екатеринбург"):
            region_page.fill_region_search_new("Ека")
            region_page.verify_first_region_choice("Екатеринбург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Екатеринбург")
            time.sleep(3)
        with allure.step("Выбрать click_region_choice_button_beeline"):
            mts_page.click_region_choice_button_futer_new()
            region_page.fill_region_search_new("Барн")
            region_page.verify_first_region_choice("Барнаул")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Барнаул")

    @allure.title("4. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, ttk_online):
        page = page_fixture
        page.goto(ttk_online)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)

        # 20 раз: открыть попап, кликнуть случайный город в этой же вкладке и проверить,
        # затем снова открыть попап
        for _ in range(20):
            mts_page.click_region_choice_button_new()
            steps.click_random_city_and_verify_same_tab_new()