import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass
from pages.page_beel.beeline_page import BeelineOnlinePage, OnlineBeelinePage, BeelineInternetOnlinePage
from pages.page_tele.tele_two_page import TeleTwoPage


@allure.feature("https://t2-official.ru/moskva")
class TestTeleTwo:

    @pytest.mark.skip("Нужны правки")
    @allure.title("3. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect(self, page_fixture, tele_two):
        page = page_fixture
        page.goto(tele_two)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        tele_page = TeleTwoPage(page=page)
        time.sleep(5)
        tele_page.click_connect_button_header()
        tele_page.send_popup_application_connection()
        time.sleep(2)
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("4. Отправка заявки из попапа по кнопке Подключить из банера с заголовком ИНТЕРНЕТ В ПОДАРОК")
    def test_application_banner_button_connect(self, page_fixture, tele_two):
        page = page_fixture
        page.goto(tele_two)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        tele_page = TeleTwoPage(page=page)
        time.sleep(5)
        tele_page.click_connect_button_banner()
        tele_page.send_popup_application_connection()
        time.sleep(2)
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("5.1. Отправка заявок с карточек тарифа мобил")
    def test_application_from_tariff_cards(self, page_fixture, tele_two):
        page = page_fixture
        page.goto(tele_two)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        time.sleep(5)
        tele_page = TeleTwoPage(page=page)
        tariff_cards = tele_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tele_page.click_tariff_connect_button(i)
                time.sleep(3)
                tele_page.send_popup_application_connection_cards_new()
                mts_page.check_sucess()
                domru_page.close_thankyou_page()
                time.sleep(2)

    @pytest.mark.skip("Нужны правки")
    @allure.title("5.2. Отправка заявок с карточек тарифа домашний")
    def test_application_from_tariff_cards_second(self, page_fixture, tele_two):
        page = page_fixture
        page.goto(tele_two)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        time.sleep(5)
        tele_page = TeleTwoPage(page=page)
        tariff_cards = tele_page.get_tariff_cards_home()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tele_page.click_tariff_connect_button(i)
                time.sleep(3)
                tele_page.send_popup_application_connection_cards_new()
                mts_page.check_sucess()
                domru_page.close_thankyou_page()
                time.sleep(2)

    @pytest.mark.skip("Нужны правки")
    @allure.title("6. Отправка заявки с каждой формы на странице с названиями: подключить тарифы билайн в Москве, "
                  "проверьте адрес подключения")
    def test_a_lot_of_forms(self, page_fixture, tele_two):
        page = page_fixture
        page.goto(tele_two)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        with allure.step("Проверить возможность подключения подключить тарифы билайн в Москве"):
            tele_two_page = TeleTwoPage(page=page)
            time.sleep(5)
            tele_two_page.send_popup_from_your_connection()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("7. Отправка заявки из попапа по кнопке Подключить из футер")
    def test_application_popup_button_connect_futer(self, page_fixture, tele_two):
        page = page_fixture
        page.goto(tele_two)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        time.sleep(5)
        tele_two_page = TeleTwoPage(page=page)
        tele_two_page.click_connect_button_futer()
        tele_two_page.send_popup_application_connection()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("8. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, tele_two):
        page = page_fixture
        page.goto(tele_two)
        time.sleep(5)
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_online_tele()

    @pytest.mark.skip("Бот не может нажать")
    @allure.title("9. Выбор региона из хедера")
    def test_choose_region_header(self, page_fixture, tele_two):
        page = page_fixture
        page.goto(tele_two)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(5)
        mts_page.click_region_choice_button()
        time.sleep(2)
        mts_page.click_region_choice_button()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Абакан"):
            time.sleep(4)
            region_page.fill_region_search("Абак")
            region_page.verify_first_region_choice("Абакан")
            region_page.select_first_region()
            region_page.verify_region_button_text("Абакан")

    @pytest.mark.skip("Бот не может нажать")
    @allure.title("11. Проверка формы 'Не нашли свой город?'")
    def test_check_dont_find_city(self, page_fixture, tele_two):
        page = page_fixture
        page.goto(tele_two)
        domru_page = DomRuClass(page=page)
        bee_page = OnlineBeelinePage(page=page)
        # Открываем страницу выбора города через хедер
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(5)
        mts_page.click_region_choice_button()
        time.sleep(2)
        mts_page.click_region_choice_button()

        region_page = ChoiceRegionPage(page=page)
        tele_two_page = TeleTwoPage(page=page)
        tele_two_page.click_button_dont_find_city()
        # region_page.close_popup_super_offer()
        # time.sleep(4)
        region_page.send_form_dont_find_city()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()
        time.sleep(2)