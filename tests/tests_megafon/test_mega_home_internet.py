import time
import allure
import pytest
from playwright.sync_api import Error as PlaywrightError
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from pages.page_mega.mega_premium import MegaPremiumOnline, MegaHomeInternet


@allure.feature("https://mega-home-internet.ru/")
class TestMegaHomeInternet:
    @allure.title("1.1. Проверка работы сайта при отсутствии сертификата")
    def test_check_website_without_certificate(self, page_fixture, nine_url):
        with allure.step("Попытка открыть сайт без игнорирования ошибок SSL"):
            try:
                page = page_fixture
                page.goto(nine_url)
                time.sleep(5)
            except PlaywrightError as error:
                error_text = str(error)
                assert any(text in error_text.lower() for text in ["ssl", "certificate", "security"]), \
                    "Ожидалась ошибка SSL/сертификата"

    @allure.title(
        "2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, попапа Выгодное "
        "спецпредложение!")
    def test_application_popup(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(20)
        mts_page.check_popup_super_offer()
        time.sleep(2)
        mts_page.send_popup_super_offer()
        mts_page.check_sucess()
        mega_page = MegaPremiumOnline(page=page)
        mega_page.close_thankyou_page()

    @allure.title("3. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной зеленой кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_green_button(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_on_red_button()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        mts_page.send_popup_super_offer()
        mts_page.check_sucess()

    @allure.title("4. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button()
        mts_page.send_popup_application_connection()
        mts_page.check_sucess()

    @allure.title("5. Отправка заявки со ВСЕХ форм на странице с названием Проверьте возможность подключения по "
                  "вашему адресу")
    def test_application_from_all_forms(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.send_popup_application_check_connection_first()
        mts_page.check_sucess()
        mega_page.close_thankyou_page()
        mega_page.send_popup_application_check_connection_second()
        mts_page.check_sucess()

    @allure.title("6. Отправка заявки с формы  с названием Не определились с тарифом?")
    def test_application_form_dont_choose(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.send_popup_application_tariff_form()
        mts_page.check_sucess()

    @allure.title("7. Отправка заявки из попапа по кнопке Уточнить")
    def test_application_button_clarify(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.click_clarify_button()
        mts_page.send_popup_application_connection()
        mts_page.check_sucess()

    @allure.title("8. Отправка заявки из попапа по кнопке Подключить из футера")
    def test_application_popup_button_connect_futer(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button_futer()
        mts_page.send_popup_application_connection()
        mts_page.check_sucess()
        mega_page = MegaPremiumOnline(page=page)
        mega_page.close_thankyou_page()

    @allure.title("9. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mega_page = MegaPremiumOnline(page=page)
        tariff_cards = mega_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                mega_page.click_tariff_connect_button(i)
                time.sleep(3)
                mts_page.send_tariff_connection_request()
                mts_page.check_sucess()
                mega_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("10. Переход по всем ссылкам на странице ")
    def test_check_popup_links(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.check_popup_links()

    @allure.title("11. Проверка якорных ссылок в хэдере")
    def test_check_all_pages_header(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.check_header_links()

    @allure.title("12. Проверка якорных ссылок в футере")
    def test_check_all_pages_futer(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.check_footer_links()

    @allure.title("13. Выбор региона СПб из хедера")
    def test_choose_region_header_spb(self, page_fixture, nine_url):
        page = page_fixture
        page.goto(nine_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button()
        time.sleep(2)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать СПб"):
            region_page.fill_region_search("Санкт")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text("Санкт-Петербург")

    @allure.title("15. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение! СПБ")
    def test_application_popup_two(self, page_fixture, nine_two_url):
        page = page_fixture
        page.goto(nine_two_url)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(20)
        mts_page.check_popup_super_offer()
        time.sleep(2)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.send_popup_super_offer()
        mts_page.check_sucess()

    @allure.title("16. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной зеленой кнопки "
                  "звонка в правом нижнем углу СПБ")
    def test_application_popup_super_offer_green_button_two(self, page_fixture, nine_two_url):
        page = page_fixture
        page.goto(nine_two_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_on_red_button()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.send_popup_super_offer()
        mts_page.check_sucess()

    @allure.title("17. Отправка заявки из попапа по кнопке Подключить из хедера СПБ")
    def test_application_popup_button_connect_two(self, page_fixture, nine_two_url):
        page = page_fixture
        page.goto(nine_two_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button()
        mega_page = MegaPremiumOnline(page=page)
        mega_page.send_popup_application_connection()
        mts_page.check_sucess()

    @allure.title("18. Отправка заявки со ВСЕХ форм на странице с названием Проверьте возможность подключения по "
                  "вашему адресу СПБ")
    def test_application_from_all_forms_two(self, page_fixture, nine_two_url):
        page = page_fixture
        page.goto(nine_two_url)
        mts_page = MtsHomeOnlinePage(page=page)
        int_page = MegaHomeInternet(page=page)
        int_page.send_popup_application_check_connection_first()
        mts_page.check_sucess()

    @allure.title("21. Отправка заявки из попапа по кнопке Подключить из футера СПБ")
    def test_application_popup_button_connect_futer_two(self, page_fixture, nine_two_url):
        page = page_fixture
        page.goto(nine_two_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_connect_button_futer()
        int_page = MegaHomeInternet(page=page)
        int_page.send_popup_application_connection()
        mts_page.check_sucess()
        mega_page = MegaPremiumOnline(page=page)
        mega_page.close_thankyou_page()

    @allure.title("22. Отправка заявок с карточек тарифа СПБ")
    def test_application_from_tariff_cards_two(self, page_fixture, nine_two_url):
        page = page_fixture
        page.goto(nine_two_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mega_page = MegaPremiumOnline(page=page)
        int_page = MegaHomeInternet(page=page)
        tariff_cards = int_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                int_page.click_tariff_connect_button(i - 1)
                time.sleep(3)
                int_page.send_tariff_connection_request()
                mts_page.check_sucess()
                mega_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("23.1. Переход по всем ссылкам на странице СПБ")
    def test_check_popup_links_two(self, page_fixture, nine_two_url):
        page = page_fixture
        page.goto(nine_two_url)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.check_popup_links()

    @allure.title("23.2. Проверка якорных ссылок в хэдере СПБ")
    def test_check_all_pages_header_two(self, page_fixture, nine_two_url):
        page = page_fixture
        page.goto(nine_two_url)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.check_header_links()

    @allure.title("23.3. Проверка якорных ссылок в футере СПБ")
    def test_check_all_pages_futer_two(self, page_fixture, nine_two_url):
        page = page_fixture
        page.goto(nine_two_url)
        mega_page = MegaPremiumOnline(page=page)
        mega_page.check_footer_links()

    @allure.title("25. Отправка заявки из попапа по кнопке Не нашли город")
    def test_application_dont_find_city(self, page_fixture, nine_two_url):
        page = page_fixture
        page.goto(nine_two_url)
        mts_page = MtsHomeOnlinePage(page=page)
        mega_page = MegaPremiumOnline(page=page)
        mts_page.click_region_choice_button()
        region_page = ChoiceRegionPage(page=page)
        mega_page.click_button_dont_find_city()
        region_page.send_form_dont_find_city()
        mts_page.check_sucess()
        mega_page.close_thankyou_page()
        time.sleep(2)
