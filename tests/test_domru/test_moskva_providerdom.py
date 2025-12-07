import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass
from pages.main_steps import MainSteps


@allure.feature("https://moskva.providerdom.ru/")
class TestMoskvaDomruProviderDom:
    @allure.title("1. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, msk_providerdom_url):
        page = page_fixture
        page.goto(msk_providerdom_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.check_popup_super_offer_second()
        time.sleep(2)
        steps = MainSteps(page=page)
        steps.send_popup_profit()
        time.sleep(4)
        mts_page.check_sucess()

    @allure.title("2. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, msk_providerdom_url):
        page = page_fixture
        page.goto(msk_providerdom_url)
        domru_page = DomRuClass(page=page)
        domru_page.check_all_links()

    @allure.title("3. Выбор региона Ангарск из хедера")
    def test_choose_region_header(self, page_fixture, msk_providerdom_url):
        page = page_fixture
        page.goto(msk_providerdom_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Ангарск"):
            region_page.fill_region_search_new("Ангар")
            region_page.verify_first_region_choice("Ангарск")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Вы находитесь в  Ангарске")

    @allure.title("4. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, msk_providerdom_url):
        page = page_fixture
        page.goto(msk_providerdom_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        mts_page.click_region_choice_button_new()
        steps.check_random_beeline_cities()
