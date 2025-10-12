import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass
from pages.main_steps import MainSteps


@allure.feature("https://dom-provider.online/")
class TestDomruProviderOnline:
    @allure.title("1. Выбор региона из всплывающего попапа Вы находитесь в Москве?")
    def test_moscow_location(self, page_fixture, dom_provider_online_url):
        page = page_fixture
        page.goto(dom_provider_online_url)
        domru_page = DomRuClass(page=page)
        domru_page.choose_msk_location_new_third()
        time.sleep(2)
        with allure.step("Выбрать СПб"):
            region_page = ChoiceRegionPage(page=page)
            region_page.fill_region_search_new("Санкт")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Вы находитесь в  Санкт-Петербурге")

    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, dom_provider_online_url):
        page = page_fixture
        page.goto(dom_provider_online_url)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(2)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.check_popup_super_offer_second()
        time.sleep(2)
        steps = MainSteps(page=page)
        steps.send_popup_profit()
        time.sleep(4)
        mts_page.check_sucess()

    @allure.title("3. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, dom_provider_online_url):
        page = page_fixture
        page.goto(dom_provider_online_url)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        domru_page.check_all_links_sec()

    @allure.title("4. Выбор региона Абинск из хедера")
    def test_choose_region_header_spb(self, page_fixture, dom_provider_online_url):
        page = page_fixture
        page.goto(dom_provider_online_url)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.click_region_choice_button_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Абинск"):
            region_page.fill_region_search_new("Аби")
            region_page.verify_first_region_choice("Абинск")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Вы находитесь в  Абинске")

    @allure.title("5. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, dom_provider_online_url):
        page = page_fixture
        page.goto(dom_provider_online_url)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)

        # 20 раз: открыть попап, кликнуть случайный город в этой же вкладке и проверить,
        # затем снова открыть попап
        for _ in range(20):
            mts_page.click_region_choice_button_new()
            steps.click_random_city_and_verify_same_tab()