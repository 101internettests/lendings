import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_mts.internet_mts_page import MtsInternetHomeOnlinePage
from pages.page_rtk.rostel_page import RostelecomPage
from pages.main_steps import MainSteps


@allure.feature("https://rtk-internet.online/")
class TestRTKImternetOnlineSecond:
    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer_third(self, page_fixture, rtk_internet_online_second):
        page = page_fixture
        page.goto(rtk_internet_online_second)
        mts_page = MtsHomeOnlinePage(page=page)
        internet_page = MtsInternetHomeOnlinePage(page=page)
        internet_page.check_popup_super_offer()
        time.sleep(2)
        steps = MainSteps(page=page)
        steps.send_popup_profit()
        time.sleep(4)
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("3. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, rtk_internet_online_second):
        page = page_fixture
        page.goto(rtk_internet_online_second)
        rostelecom_page = RostelecomPage(page=page)
        rostelecom_page.check_all_links_rtk_home()

    @allure.title("4. Выбор региона СПБ и Абакан из хедера")
    def test_choose_region_header(self, page_fixture, rtk_internet_online_second):
        page = page_fixture
        page.goto(rtk_internet_online_second)
        region_page = ChoiceRegionPage(page=page)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        with allure.step("Выбрать СПб"):
            internet_page = MtsInternetHomeOnlinePage(page=page)
            internet_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Санкт")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Санкт-Петербург")
        with allure.step("Выбрать Абакан"):
            internet_page = MtsInternetHomeOnlinePage(page=page)
            internet_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Абак")
            region_page.verify_first_region_choice("Абакан")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Абакан")

    @allure.title("6. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, rtk_internet_online_ru):
        page = page_fixture
        page.goto(rtk_internet_online_ru)
        rostelecom_page = RostelecomPage(page=page)
        time.sleep(15)
        rostelecom_page.close_popup()
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        # 20 раз: открыть попап, кликнуть случайный город в этой же вкладке и проверить,
        # затем снова открыть попап
        for _ in range(20):
            mts_page.click_region_choice_button_new()
            steps.click_random_city_and_verify_same_tab()