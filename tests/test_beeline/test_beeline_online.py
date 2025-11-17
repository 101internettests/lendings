import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass
from locators.domru.domru_locators import LocationPopup
from pages.page_beel.beeline_page import BeelineOnlinePage, OnlineBeelinePage, BeelineInternetOnlinePage
from pages.main_steps import MainSteps


@allure.feature("https://beeline-ru.online/")
class TestBeelineOnline:
    @allure.title("1. Выбор региона из всплывающего попапа Вы находитесь в Москве?")
    def test_choose_region_from_popup(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        domru_page = DomRuClass(page=page)
        domru_page.choose_msk_location_new()
        time.sleep(2)
        with allure.step("Выбрать СПб"):
            region_page = ChoiceRegionPage(page=page)
            region_page.fill_region_search_new("Санкт")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Вы находитесь в Санкт-Петербурге")

    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.check_popup_super_offer_second()
        time.sleep(2)
        steps = MainSteps(page=page)
        steps.send_popup_profit()
        time.sleep(4)
        mts_page.check_sucess()

    @allure.title("3. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_sec()

    @allure.title("4. Выбор региона из хедера")
    def test_choose_region_header_spb(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.click_region_choice_button_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Санкт Петербург"):
            region_page.fill_region_search_new("Санк")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Вы находитесь в Санкт-Петербурге")
            time.sleep(3)
        with allure.step("Выбрать Аксай"):
            domru_page.close_popup_location()
            mts_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Аксай")
            region_page.verify_first_region_choice("Аксай (Ростовская область)")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Аксай")

    @allure.title("5. Выбор региона из футера")
    def test_choose_region_futer_spb(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.click_region_choice_button_beeline()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Санкт Петербург"):
            region_page.fill_region_search_new("Санк")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Вы находитесь в Санкт-Петербурге")
            time.sleep(3)
        with allure.step("Выбрать Аксай"):
            domru_page.close_popup_location()
            mts_page.click_region_choice_button_beeline_second()
            region_page.fill_region_search_new("Аксай")
            region_page.verify_first_region_choice("Аксай (Ростовская область)")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Аксай")

    @allure.title("6. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, beeline_online):
        page = page_fixture
        page.goto(beeline_online)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)

        # 20 раз: открыть попап, кликнуть случайный город в этой же вкладке и проверить,
        # затем снова открыть попап
        for _ in range(10):
            mts_page.click_region_choice_button_new()
            steps.click_random_city_and_verify_same_tab()
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass