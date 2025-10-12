import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from pages.page_mts.mts_gpon import MtsGponHomeOnlinePage
from pages.page_mts.msk_mts_page import MtsMSKHomeOnlinePage
from playwright.sync_api import Error as PlaywrightError
from pages.page_beel.beeline_page import BeelineOnlinePage, BeelineInternetOnlinePage, OnlineBeelinePage
from pages.main_steps import MainSteps


@allure.feature("https://mts-home-gpon.ru/")
class TestGponMtsHomeOnline:

    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.check_popup_super_offer()
        time.sleep(2)
        steps = MainSteps(page=page)
        steps.send_popup_profit()
        time.sleep(4)
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("3. Переход по всем ссылкам на странице")
    def test_gpon_check_all_pages(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        gpon_page = MtsGponHomeOnlinePage(page=page)
        gpon_page.check_all_links()

    @allure.title("4. Выбор региона Азнакаево из хедера")
    def test_gpon_choose_region_header_azn(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        gpon_page = MtsGponHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            gpon_page.click_region_choice_button_gpon()
            region_page.fill_region_search_new("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text_new_gpon("Азнакаево")

    @allure.title("5. Выбор региона Азнакаево из футера")
    def test_gpon_choose_region_futer_azn(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        gpon_page = MtsGponHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            gpon_page.click_region_choice_button_futer_gpon_new()
            region_page.fill_region_search_new("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text_new_gpon("Азнакаево")

    @allure.title("6. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)

        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)

        # 20 раз: открыть попап, кликнуть случайный город в этой же вкладке и проверить,
        # затем снова открыть попап
        for _ in range(20):
            mts_page.click_region_choice_button_gpon()
            steps.click_random_city_and_verify_same_tab()