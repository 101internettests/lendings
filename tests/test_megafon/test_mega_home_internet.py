import time
import allure
import pytest
from playwright.sync_api import Error as PlaywrightError
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from pages.page_mega.mega_premium import MegaPremiumOnline, MegaHomeInternet
from pages.page_mts.internet_mts_page import MtsInternetHomeOnlinePage
from locators.mts.mts_home_online import MTSHomeOnlineMain
from pages.main_steps import MainSteps


@allure.feature("https://mega-home-internet.ru/")
class TestMegaHomeInternet:
    @allure.title(
        "2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, попапа Выгодное "
        "спецпредложение!")
    def test_application_popup(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.check_popup_super_offer_second()
        time.sleep(2)
        steps = MainSteps(page=page)
        steps.send_popup_profit()
        time.sleep(4)
        mts_page.check_sucess()

    @allure.title("3. Переход по всем ссылкам на странице ")
    def test_check_popup_links(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Проверка попапа 'Выгодное спецпредложение' и закрытие при наличии (до 50с)"):
            try:
                def strip_xpath(sel: str) -> str:
                    return sel[len("xpath="):] if sel.startswith("xpath=") else sel

                union_xpath = (
                    f"xpath=({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_TEXT)})"
                )
                page.wait_for_selector(union_xpath, state="visible", timeout=30000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass
        mega_page = MegaPremiumOnline(page=page)
        mega_page.check_popup_links()

    @allure.title("4. Проверка якорных ссылок в хэдере")
    def test_check_all_pages_header(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.check_header_links()

    @allure.title("5. Проверка якорных ссылок в футере")
    def test_check_all_pages_futer(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.check_footer_links()

    @allure.title("6. Выбор региона СПб из хедера")
    def test_choose_region_header_spb(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
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

    @allure.title("7. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)

        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        time.sleep(7)
        region_page = ChoiceRegionPage(page=page)
        region_page.close_popup_super_offer_new()
        # 20 раз: открыть попап, кликнуть случайный город в этой же вкладке и проверить,
        # затем снова открыть попап
        for _ in range(20):
            mts_page.click_region_choice_button_new()
            steps.click_random_city_and_verify_same_tab()

