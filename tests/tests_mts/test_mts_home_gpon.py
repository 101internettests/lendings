import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from pages.page_mts.mts_gpon import MtsGponHomeOnlinePage
from pages.page_mts.msk_mts_page import MtsMSKHomeOnlinePage
from playwright.sync_api import Error as PlaywrightError
from pages.page_beel.beeline_page import BeelineOnlinePage, BeelineInternetOnlinePage, OnlineBeelinePage


@allure.feature("https://mts-home-gpon.ru/")
class TestGponMtsHomeOnline:
    @allure.title("1.1. Проверка работы сайта при отсутствии сертификата")
    def test_gpon_check_website_without_certificate(self, page_fixture, third_url):
        with allure.step("Попытка открыть сайт без игнорирования ошибок SSL"):
            try:
                page = page_fixture
                page.goto(third_url)
                time.sleep(5)
            except PlaywrightError as error:
                error_text = str(error)
                assert any(text in error_text.lower() for text in ["ssl", "certificate", "security"]), \
                    "Ожидалась ошибка SSL/сертификата"

    @pytest.mark.skip("Попап не высвечивается")
    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_gpon_application_popup_super_offer(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(60)
        gpon_page = MtsGponHomeOnlinePage(page=page)
        gpon_page.check_popup_super_offer()
        time.sleep(2)
        online_page = BeelineOnlinePage(page=page)
        online_page.send_popup_super_offer_new_ghome()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("3. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_gpon_application_popup_super_offer_red_button(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        mts_page = MtsHomeOnlinePage(page=page)
        gpon_page = MtsGponHomeOnlinePage(page=page)
        mts_page.click_on_red_button()
        gpon_page.check_popup_super_offer()
        time.sleep(2)
        online_page = BeelineOnlinePage(page=page)
        online_page.send_popup_super_offer_new_ghome()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("4. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_gpon_application_popup_button_connect(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        mts_page = MtsHomeOnlinePage(page=page)
        # time.sleep(6)
        choice_page = ChoiceRegionPage(page=page)
        gpon_page = MtsGponHomeOnlinePage(page=page)
        # choice_page.close_popup_super_offer()
        gpon_page.click_connect_button()
        online = BeelineOnlinePage(page=page)
        online.send_popup_super_offer_new_phone()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("5. Отправка заявки со ВСЕХ форм на странице")
    def test_gpon_application_from_all_forms(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.send_popup_application_check_connection()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()
        time.sleep(10)
        region_page = ChoiceRegionPage(page=page)
        # region_page.close_popup_super_offer()
        gpon_page = BeelineOnlinePage(page=page)
        gpon_page.send_popup_super_offer_new_address_first()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("6. Отправка заявок с карточек тарифа")
    def test_gpon_application_from_tariff_cards(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        mts_page = MtsMSKHomeOnlinePage(page=page)
        tariff_cards = mts_page.get_tariff_cards()
        # time.sleep(10)
        region_page = ChoiceRegionPage(page=page)
        gpon_page = MtsGponHomeOnlinePage(page=page)
        # region_page.close_popup_super_offer()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = mts_page.get_tariff_name(i)
                if tariff_name is None:
                    continue

                mts_page.click_tariff_connect_button(i)
                time.sleep(3)
                mts_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                online_page = BeelineOnlinePage(page=page)
                online_page.send_popup_super_offer_new_phone()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @pytest.mark.skip("Нужны правки")
    @allure.title("7. Отправка заявки из попапа по кнопке Подключить из футера")
    def test_gpon_application_popup_button_connect_futer(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button_futer()
        online = BeelineOnlinePage(page=page)
        online.send_popup_super_offer_new_phone()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("8. Отправка заявки из попапа по кнопке Проверить адрес из футера")
    def test_gpon_application_popup_button_check_address_futer(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        # time.sleep(10)
        region_page = ChoiceRegionPage(page=page)
        # region_page.close_popup_super_offer()
        mts_page = MtsHomeOnlinePage(page=page)
        gpon_page = MtsGponHomeOnlinePage(page=page)
        gpon_page.click_check_address_button_futer()
        online = BeelineInternetOnlinePage(page=page)
        online.send_popup_application_connection_pro_new_phone()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()

    @allure.title("9. Проверка всех ссылок")
    def test_gpon_check_all_pages(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        gpon_page = MtsGponHomeOnlinePage(page=page)
        gpon_page.check_all_links()

    @allure.title("10. Выбор региона Азнакаево из хедера")
    def test_gpon_choose_region_header_azn(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        gpon_page = MtsGponHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            gpon_page.click_region_choice_button_gpon()
            region_page.fill_region_search_new("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text_new_gpon("Азнакаево")

    @allure.title("11. Выбор региона Азнакаево из футера")
    def test_gpon_choose_region_futer_azn(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)
        gpon_page = MtsGponHomeOnlinePage(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Азнакаево"):
            gpon_page.click_region_choice_button_futer_gpon_new()
            region_page.fill_region_search_new("Азнак")
            region_page.verify_first_region_choice("Азнакаево")
            region_page.select_first_region()
            region_page.verify_region_button_text_new_gpon("Азнакаево")

    # @allure.title("12. Переход по всем ссылкам городов на странице выбора города")
    # def test_gpon_check_all_city_links(self, page_fixture, third_url):
    #     page = page_fixture
    #     page.goto(third_url)
    #
    #     # Открываем страницу выбора города через хедер
    #     gpon_page = MtsGponHomeOnlinePage(page=page)
    #     gpon_page.click_region_choice_button_gpon()
    #
    #     # Проверяем все ссылки городов
    #     region_page = ChoiceRegionPage(page=page)
    #     region_page.check_all_city_links()

    @pytest.mark.skip("Пока не актуален, нет возможности проверить сценарий")
    @allure.title("16. Проверка формы 'Не нашли свой город?'")
    def test_gpon_check_dont_find_city(self, page_fixture, third_url):
        page = page_fixture
        page.goto(third_url)

        # Открываем страницу выбора города через хедер
        mts_page = MtsHomeOnlinePage(page=page)
        gpon_page = MtsGponHomeOnlinePage(page=page)
        gpon_page.click_region_choice_button_gpon()

        # Работаем с формой "Не нашли свой город?"
        region_page = ChoiceRegionPage(page=page)
        region_page.click_button_dont_find_city()
        gpon_page.close_popup_super_offer()
        time.sleep(4)
        region_page.send_form_dont_find_city()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()
        time.sleep(2)