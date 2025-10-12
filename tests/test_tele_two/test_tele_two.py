import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass
from pages.page_beel.beeline_page import BeelineOnlinePage, OnlineBeelinePage
from pages.page_tele.tele_two_page import TeleTwoPage
from pages.main_steps import MainSteps


@allure.feature("https://t2-official.ru/")
class TestTeleTwo:

    @allure.title("3. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, tele_two):
        page = page_fixture
        page.goto(tele_two)
        time.sleep(5)
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_online_tele()

    @allure.title("4. Выбор региона из хедера")
    def test_choose_region_header(self, page_fixture, tele_two):
        page = page_fixture
        page.goto(tele_two)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(5)
        mts_page.click_region_choice_button()
        # time.sleep(2)
        # mts_page.click_region_choice_button()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Абакан"):
            time.sleep(4)
            region_page.fill_region_search_new("Абак")
            region_page.verify_first_region_choice("Абакан")
            region_page.select_first_region()
            region_page.verify_region_button_text("Абакан")

    @allure.title("6. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, tele_two):
        page = page_fixture
        page.goto(tele_two)

        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        # 20 раз: открыть попап, кликнуть случайный город в этой же вкладке и проверить,
        # затем снова открыть попап
        for _ in range(20):
            mts_page.click_region_choice_button()
            steps.click_random_city_and_verify_same_tab()
