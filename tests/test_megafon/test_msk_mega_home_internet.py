import time
import allure
import pytest
from playwright.sync_api import Error as PlaywrightError
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from pages.page_mega.mega_premium import MegaPremiumOnline, MegaHomeInternet
from pages.page_mts.internet_mts_page import MtsInternetHomeOnlinePage
from pages.main_steps import MainSteps
from pages.page_rtk.rostel_page import RostelecomPage


@allure.feature("https://moskva.mega-home-internet.ru/")
class TestskMegaHomeInternet:
    @allure.title(
        "2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, попапа Выгодное "
        "спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, mega_home_internet):
        page = page_fixture
        page.goto(mega_home_internet)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.check_popup_super_offer_second()
        time.sleep(2)
        steps = MainSteps(page=page)
        steps.send_popup_profit()
        # mts_page.check_sucess()

    @allure.title("3. Переход по всем ссылкам на странице ")
    def test_check_all_pages(self, page_fixture, mega_home_internet):
        page = page_fixture
        page.goto(mega_home_internet)
        rostelecom_page = RostelecomPage(page=page)
        # time.sleep(15)
        # rostelecom_page.close_popup()
        steps = MainSteps(page=page)
        steps.check_links_mega_sec()

    @allure.title("4. Выбор региона СПб из хедера")
    def test_choose_region_header(self, page_fixture, mega_home_internet):
        page = page_fixture
        page.goto(mega_home_internet)
        time.sleep(7)
        region_page = ChoiceRegionPage(page=page)
        region_page.close_popup_super_offer_new()
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button_new()
        time.sleep(2)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать СПб"):
            region_page.fill_region_search_new("Санкт")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Вы находитесь в   Санкт-Петербурге")
        with allure.step("Выбрать Абакан"):
            mts_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Абак")
            region_page.verify_first_region_choice("Абакан")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Вы находитесь в   Абакане")

    @allure.title("5. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, mega_home_internet):
        page = page_fixture
        page.goto(mega_home_internet)

        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        mts_page.click_region_choice_button_new()
        steps.check_random_beeline_cities()