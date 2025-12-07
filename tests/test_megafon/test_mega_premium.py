import time
import allure
import pytest
from playwright.sync_api import Error as PlaywrightError
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from pages.page_mega.mega_premium import MegaPremiumOnline
from pages.page_mts.internet_mts_page import MtsInternetHomeOnlinePage
from pages.main_steps import MainSteps


@allure.feature("https://mega-premium.ru/")
class TestMegaPremium:
    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, eight_url):
        page = page_fixture
        page.goto(eight_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.check_popup_super_offer_second()
        time.sleep(2)
        steps = MainSteps(page=page)
        steps.send_popup_profit()
        time.sleep(4)

    @allure.title("3. Переход по всем ссылкам на странице ")
    def test_check_popup_links(self, page_fixture, eight_url):
        page = page_fixture
        page.goto(eight_url)
        steps = MainSteps(page=page)
        steps.check_links_mega()

    @allure.title("4. Проверка якорных ссылок в хэдере")
    def test_check_all_pages_header(self, page_fixture, eight_url):
        page = page_fixture
        page.goto(eight_url)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.check_header_links_mega()

    @allure.title("5. Проверка якорных ссылок в футере")
    def test_check_all_pages_futer(self, page_fixture, eight_url):
        page = page_fixture
        page.goto(eight_url)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.check_footer_links()

    @allure.title("6. Выбор региона СПб из хедера")
    def test_choose_region_header(self, page_fixture, eight_url):
        page = page_fixture
        page.goto(eight_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button_new()
        time.sleep(2)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать СПб"):
            region_page.fill_region_search_new("Санкт")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Вы находитесь в   Санкт-Петербурге")

    @allure.title("7. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, eight_url):
        page = page_fixture
        page.goto(eight_url)

        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        mts_page.click_region_choice_button_new()
        steps.check_random_beeline_cities()