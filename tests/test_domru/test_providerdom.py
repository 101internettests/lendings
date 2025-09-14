import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass


@allure.feature("https://providerdom.ru/")
class TestDomruProviderDom:
    @pytest.mark.skip("Нужны правки")
    @allure.title("1. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, providerdom_url):
        page = page_fixture
        page.goto(providerdom_url)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(25)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        domru_page.send_popup_super_offer_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("2. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self, page_fixture, providerdom_url):
        page = page_fixture
        page.goto(providerdom_url)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.click_on_red_button()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        domru_page.send_popup_super_offer_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("3. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect(self, page_fixture, providerdom_url):
        page = page_fixture
        page.goto(providerdom_url)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.click_connect_button()
        domru_page.send_popup_application_connection_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("4. Отправка заявки с каждой формы на странице с названиями: Подключите стабильный интернет, "
                  "Бесплатный тест-драйв роутера на 14 дней, Тест-драйв скорости до 800 Мбит/с на 3 месяца, "
                  "Попробуйте скоростной безлимитный интернет")
    def test_a_lot_of_forms(self, page_fixture, providerdom_url):
        page = page_fixture
        page.goto(providerdom_url)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        with allure.step("Подключите стабильный интернет в Москве"):
            domru_page.send_popup_from_banner()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()
        with allure.step("Бесплатный тест-драйв роутера на 14 дней"):
            domru_page.send_popup_free_tes_drive()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()
        with allure.step("Тест-драйв скорости до 800 Мбит/с на 3 месяца"):
            domru_page.send_popup_tes_drive_three_months()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()
        with allure.step("Попробуйте скоростной безлимитный интернет"):
            domru_page.send_popup_speed_inter()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("5. Отправка заявки с формы на странице с названием Проверьте возможность подключения по вашему "
                  "адресу")
    def test_check_possibilitie_connection(self, page_fixture, providerdom_url):
        page = page_fixture
        page.goto(providerdom_url)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        domru_page.send_popup_check_connection()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("6. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, providerdom_url):
        page = page_fixture
        page.goto(providerdom_url)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        tariff_cards = domru_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = mts_page.get_tariff_name(i)
                domru_page.click_tariff_connect_button(i)
                mts_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                domru_page.send_tariff_connection_request()
                mts_page.check_sucess()
                domru_page.close_thankyou_page()
                time.sleep(2)

    @pytest.mark.skip("Нужны правки")
    @allure.title("7. Отправка заявки из попапа Заявка на подключение с кнопки Подключить интернет с группы блоков "
                  "под заголовком Дом.ру — ваш план для самых разных задач")
    def test_popup_application_connection(self, page_fixture, providerdom_url):
        page = page_fixture
        page.goto(providerdom_url)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        with allure.step("Нажать на кнопку Подключить интернет первую"):
            domru_page.open_popup_connection()
            domru_page.send_tariff_connection_request()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()
            time.sleep(2)
        with allure.step("Нажать на кнопку Подключить интернет вторую"):
            domru_page.open_popup_connection_second()
            domru_page.send_tariff_connection_request()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()
            time.sleep(2)
        with allure.step("Нажать на кнопку Подключить интернет вторую"):
            domru_page.open_popup_connection_third()
            domru_page.send_tariff_connection_request()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()
            time.sleep(2)

    @allure.title("8. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, providerdom_url):
        page = page_fixture
        page.goto(providerdom_url)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        domru_page.check_all_links()

    @pytest.mark.skip("Нужны правки")
    @allure.title("9. Выбор региона Ангарск из хедера")
    def test_choose_region_header_spb(self, page_fixture, providerdom_url):
        page = page_fixture
        page.goto(providerdom_url)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.click_region_choice_button()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Ангарск"):
            region_page.fill_region_search("Ангар")
            region_page.verify_first_region_choice("Ангарск")
            region_page.select_first_region()
            region_page.verify_region_button_text("Ангарск")

    @pytest.mark.skip("Нужны правки")
    @allure.title("11. Проверка формы 'Не нашли свой город?'")
    def test_check_dont_find_city(self, page_fixture, providerdom_url):
        page = page_fixture
        page.goto(providerdom_url)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        # Открываем страницу выбора города через хедер
        mts_page = MtsHomeOnlinePage(page=page)
        mts_page.click_region_choice_button()

        # Работаем с формой "Не нашли свой город?"
        region_page = ChoiceRegionPage(page=page)
        region_page.click_button_dont_find_city()
        # region_page.close_popup_super_offer()
        # time.sleep(4)
        region_page.send_form_dont_find_city()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()
        time.sleep(2)