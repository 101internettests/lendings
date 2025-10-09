import time
import allure
import pytest
from pages.main_steps import MainSteps
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass


class TestForms:
    @pytest.mark.skip("Доработать")
    @allure.title("1. Отправка заявки из  попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self, page_fixture, example_url):
        page = page_fixture
        page.goto(example_url)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        steps = MainSteps(page=page)
        steps.open_popup_for_colorful_button()
        steps.send_popup_profit()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()
        steps.open_popup_for_colorful_button()
        steps.button_change_city_profit()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Воронеж"):
            time.sleep(2)
            region_page.fill_region_search_new("Воронеж")
            region_page.verify_first_region_choice("Воронеж")
            time.sleep(2)
            region_page.select_first_region()
        steps.send_popup_profit_second_house()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @pytest.mark.skip("Доработать")
    @allure.title("2. Отправка заявки из попапа  по кнопке Подключить (все кнопки на странице)")
    def test_application_popup_button_connect(self, page_fixture, example_url):
        page = page_fixture
        page.goto(example_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)

        #
        # mts_page.click_connect_button()
        # online_page = BeelineInternetOnlinePage(page=page)
        # online_page.send_popup_application_connection_pro_new()
        # mts_page.check_sucess()
        # mts_page.close_thankyou_page()

    @pytest.mark.skip("Доработать")
    @allure.title("8. Отправка заявки со ВСЕХ  попапов со всех кнопок Подробнее на странице Бизнес")
    def test_application_popup_button_connect(self, page_fixture, example_url):
        page = page_fixture
        page.goto(example_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
