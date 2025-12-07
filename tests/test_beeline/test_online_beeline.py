import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass
from pages.page_beel.beeline_page import BeelineOnlinePage, OnlineBeelinePage, BeelineInternetOnlinePage
from pages.main_steps import MainSteps


@allure.feature("https://online-beeline.ru/")
class TestOnlineBeeline:
    @allure.title("1. Выбор региона из всплывающего попапа Уточните ваш город")
    def test_choose_region_from_popup(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        online_beeline_page = OnlineBeelinePage(page=page)
        time.sleep(8)
        online_beeline_page.popup_choose_city_accept()
        with allure.step("Выбрать СПб"):
            region_page = ChoiceRegionPage(page=page)
            region_page.fill_region_search_new("Санкт")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Санкт-Петербург")

    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(8)
        online_beeline_page = OnlineBeelinePage(page=page)
        online_beeline_page.popup_choose_city()
        mts_page.check_popup_super_offer_second()
        time.sleep(2)
        steps = MainSteps(page=page)
        steps.send_popup_profit()
        time.sleep(4)
        mts_page.check_sucess()

    @allure.title("3. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        steps = MainSteps(page=page)
        steps.check_links_beeline_sec()

    @allure.title("4. Выбор региона из хедера")
    def test_choose_region_header(self, page_fixture, online_beeline):
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

    @allure.title("6. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, online_beeline):
        page = page_fixture
        page.goto(online_beeline)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        mts_page.click_region_choice_button_new()
        steps.check_random_beeline_cities()
