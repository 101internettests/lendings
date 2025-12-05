import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass
from pages.page_beel.beeline_page import BeelineOnlinePage, BeelineInternetOnlinePage, OnlineBeelinePage
from pages.main_steps import MainSteps
from locators.mts.mts_home_online import MTSHomeOnlineMain
from locators.domru.domru_locators import LocationPopup


@allure.feature("https://moskva.beeline-ru.online/")
class TestMskBeelineOnline:
    @allure.title("1. Выбор региона из всплывающего попапа Вы находитесь в Москве?")
    def test_choose_region_from_popup(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
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
    def test_application_popup_super_offer(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
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
    def test_check_all_pages(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
        domru_page = DomRuClass(page=page)
        region_page = ChoiceRegionPage(page=page)
        domru_page.close_popup_location()
        with allure.step("Проверка попапа 'Выгодное спецпредложение' и закрытие при наличии (до 50с)"):
            try:
                def strip_xpath(sel: str) -> str:
                    return sel[len("xpath="):] if sel.startswith("xpath=") else sel

                union_xpath = (
                    f"xpath=({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_TEXT)})"
                )
                page.wait_for_selector(union_xpath, state="visible", timeout=60000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_msk()

    @allure.title("4. Выбор региона из хедера")
    def test_choose_region_header(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
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
            mts_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Аксай")
            region_page.verify_first_region_choice("Аксай (Ростовская область)")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Аксай")

    @allure.title("5. Выбор региона из футера")
    def test_choose_region_futer(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.click_region_choice_button_beeline_second()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Санкт Петербург"):
            region_page.fill_region_search_new("Санк")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Вы находитесь в Санкт-Петербурге")
            time.sleep(3)
        with allure.step("Выбрать Аксай"):
            mts_page.click_region_choice_button_beeline_second()
            region_page.fill_region_search_new("Аксай")
            region_page.verify_first_region_choice("Аксай (Ростовская область)")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Аксай")

    @allure.title("6. Переход по случайным 20 ссылкам городов на странице выбора города и проверка")
    def test_check_all_city_links(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
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
                page.wait_for_selector(union_xpath, state="visible", timeout=50000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass

        # 20 раз: открыть попап, кликнуть случайный город в этой же вкладке и проверить,
        # затем снова открыть попап
        for _ in range(5):
            mts_page.click_region_choice_button_new()
            steps.click_random_city_and_verify_new_cutyloc()
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass