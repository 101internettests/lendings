import time
import allure
import pytest
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from pages.page_domru.domru_page import DomRuClass
from pages.page_beel.beeline_page import BeelineOnlinePage, BeelineInternetOnlinePage, OnlineBeelinePage


@allure.feature("https://moskva.beeline-ru.online/")
class TestMskBeelineOnline:
    @allure.title("1.1. Проверка работы сайта при отсутствии сертификата")
    def test_check_website_without_certificate(self, page_fixture, msk_beeline_online):
        with allure.step("Попытка открыть сайт без игнорирования ошибок SSL"):
            try:
                page = page_fixture
                page.goto(msk_beeline_online)
                time.sleep(5)
            except PlaywrightError as error:
                error_text = str(error)
                assert any(text in error_text.lower() for text in ["ssl", "certificate", "security"]), \
                    "Ожидалась ошибка SSL/сертификата"

    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(58)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.send_popup_super_offer_new_moscow()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("3. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной желтой кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.close_coockies()
        mts_page.click_on_red_button()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page.send_popup_super_offer_new_moscow()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("4. Отправка заявки из попапа по кнопке Подключить из хедера")
    def test_application_popup_button_connect(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.click_connect_button()
        online_page = BeelineInternetOnlinePage(page=page)
        online_page.send_popup_application_connection_pro_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("5. Отправка заявки с каждой формы на странице с названиями Проверьте подключение вашего дома")
    def test_a_lot_of_forms(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        with allure.step("Проверить возможность подключения билайн по вашему адресу в Москве первый"):
            beeline_page = BeelineOnlinePage(page=page)
            online_beeline_page = OnlineBeelinePage(page=page)
            online_beeline_page.send_popup_application_connection_home_new()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()
        with allure.step("Проверить возможность подключения билайн по вашему адресу в Москве второй"):
            online_beeline_page.send_popup_from_connection_home_new()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()

    @allure.title("6. Отправка заявок с карточек тарифа")
    def test_application_from_tariff_cards(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        beeline_page = BeelineOnlinePage(page=page)
        beeline_internet_page = BeelineInternetOnlinePage(page=page)
        domru_page.close_popup_location()
        tariff_cards = beeline_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = beeline_page.get_tariff_name(i)
                beeline_page.click_tariff_connect_button(i)
                beeline_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                beeline_internet_page.send_popup_application_connection_pro_new()
                mts_page.check_sucess()
                domru_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("7. Отправка заявки из попапа по кнопке Подключить из футер")
    def test_application_popup_button_connect_futer(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.click_connect_button_futer()
        beeline_internet_page = BeelineInternetOnlinePage(page=page)
        beeline_internet_page.send_popup_application_connection_pro_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @pytest.mark.skip("Нужны правки")
    @allure.title("8. Проверка всех ссылок")
    def test_check_all_pages(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_msk()

    @allure.title("9. Выбор региона из хедера")
    def test_choose_region_header_spb(self, page_fixture, msk_beeline_online):
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
            region_page.verify_region_button_text_new("Санкт-Петербург")
            time.sleep(3)
        with allure.step("Выбрать Аксай"):
            # domru_page.close_popup_location()
            mts_page.click_region_choice_button_new()
            region_page.fill_region_search_new("Аксай")
            region_page.verify_first_region_choice("Аксай (Ростовская область)")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Аксай")

    @allure.title("10. Выбор региона из футера")
    def test_choose_region_futer_spb(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.click_region_choice_button_futer_new()
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Выбрать Санкт Петербург"):
            region_page.fill_region_search_new("Санк")
            region_page.verify_first_region_choice("Санкт-Петербург")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Санкт-Петербург")
            time.sleep(3)
        with allure.step("Выбрать Аксай"):
            # domru_page.close_popup_location()
            mts_page.click_region_choice_button_futer_new()
            region_page.fill_region_search_new("Аксай")
            region_page.verify_first_region_choice("Аксай (Ростовская область)")
            region_page.select_first_region()
            region_page.verify_region_button_text_new("Аксай")

    @pytest.mark.skip("Пока не актуален, нет возможности проверить сценарий")
    @allure.title("12. Проверка формы 'Не нашли свой город?'")
    def test_check_dont_find_city(self, page_fixture, msk_beeline_online):
        page = page_fixture
        page.goto(msk_beeline_online)
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

    @pytest.mark.skip("Попап не высвечивается")
    @allure.title("13. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение! для урла Домашний интернет")
    def test_application_popup_super_offer_dom(self, page_fixture, msk_beeline_online_dom):
        page = page_fixture
        page.goto(msk_beeline_online_dom)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(58)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.send_popup_super_offer_new_moscow()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("14. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной желтой кнопки "
                  "звонка в правом нижнем углу для урла Домашний интернет")
    def test_application_popup_super_offer_red_button_dom(self, page_fixture, msk_beeline_online_dom):
        page = page_fixture
        page.goto(msk_beeline_online_dom)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.close_coockies()
        mts_page.click_on_red_button()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page.send_popup_super_offer_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("15. Отправка заявки из попапа по кнопке Подключить из хедера для урла Домашний интернет")
    def test_application_popup_button_connect_dom(self, page_fixture, msk_beeline_online_dom):
        page = page_fixture
        page.goto(msk_beeline_online_dom)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.click_connect_button()
        online_beeline_page = OnlineBeelinePage(page=page)
        online_beeline_page.send_popup_from_connection_home_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("16. Отправка заявки с каждой формы на странице с названиями Проверьте подключение вашего дома для урла Домашний интернет")
    def test_a_lot_of_forms_dom(self, page_fixture, msk_beeline_online_dom):
        page = page_fixture
        page.goto(msk_beeline_online_dom)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        with allure.step("Проверить возможность подключения билайн по вашему адресу в Москве первый"):
            beeline_page = BeelineOnlinePage(page=page)
            online_beeline_page = OnlineBeelinePage(page=page)
            online_beeline_page.send_popup_application_connection_home_new()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()

    @allure.title("17. Отправка заявок с карточек тарифа для урла Домашний интернет")
    def test_application_from_tariff_cards_dom(self, page_fixture, msk_beeline_online_dom):
        page = page_fixture
        page.goto(msk_beeline_online_dom)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        beeline_page = BeelineOnlinePage(page=page)
        domru_page.close_popup_location()
        tariff_cards = beeline_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = beeline_page.get_tariff_name(i)
                beeline_page.click_tariff_connect_button(i)
                beeline_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                online_beeline_page = OnlineBeelinePage(page=page)
                online_beeline_page.send_popup_from_connection_home_new()
                mts_page.check_sucess()
                domru_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("18. Отправка заявки из попапа по кнопке Подключить из футер для урла Домашний интернет")
    def test_application_popup_button_connect_futer_dom(self, page_fixture, msk_beeline_online_dom):
        page = page_fixture
        page.goto(msk_beeline_online_dom)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.click_connect_button_futer()
        online_beeline_page = OnlineBeelinePage(page=page)
        online_beeline_page.send_popup_from_connection_home_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("19. Проверка всех ссылок для урла Домашний интернет")
    def test_check_all_pages_dom(self, page_fixture, msk_beeline_online_dom):
        page = page_fixture
        page.goto(msk_beeline_online_dom)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_msk_dom()

    @pytest.mark.skip("Попап не высвечивается")
    @allure.title("20. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение! для урла Домашний интернет и тв")
    def test_application_popup_super_offer_tv(self, page_fixture, msk_beeline_online_tv):
        page = page_fixture
        page.goto(msk_beeline_online_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(58)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.send_popup_super_offer_dom()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("21. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной желтой кнопки "
                  "звонка в правом нижнем углу для урла Домашний интернет и тв")
    def test_application_popup_super_offer_red_button_tv(self, page_fixture, msk_beeline_online_tv):
        page = page_fixture
        page.goto(msk_beeline_online_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.close_coockies()
        mts_page.click_on_red_button()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page.send_popup_super_offer_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("22. Отправка заявки из попапа по кнопке Подключить из хедера для урла Домашний интернет и тв")
    def test_application_popup_button_connect_tv(self, page_fixture, msk_beeline_online_tv):
        page = page_fixture
        page.goto(msk_beeline_online_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.click_connect_button()
        online_beeline_page = OnlineBeelinePage(page=page)
        online_beeline_page.send_popup_from_connection_home_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title(
        "23. Отправка заявки с каждой формы на странице с названиями Проверьте подключение вашего дома для урла Домашний интернет и тв")
    def test_a_lot_of_forms_tv(self, page_fixture, msk_beeline_online_tv):
        page = page_fixture
        page.goto(msk_beeline_online_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        with allure.step("Проверить возможность подключения билайн по вашему адресу в Москве первый"):
            online_beeline_page = OnlineBeelinePage(page=page)
            online_beeline_page.send_popup_application_connection_home_new()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()

    @allure.title("24. Отправка заявок с карточек тарифа для урла Домашний интернет и тв")
    def test_application_from_tariff_cards_tv(self, page_fixture, msk_beeline_online_tv):
        page = page_fixture
        page.goto(msk_beeline_online_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        beeline_page = BeelineOnlinePage(page=page)
        domru_page.close_popup_location()
        tariff_cards = beeline_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = beeline_page.get_tariff_name(i)
                beeline_page.click_tariff_connect_button(i)
                beeline_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                online_beeline_page = OnlineBeelinePage(page=page)
                online_beeline_page.send_popup_from_connection_home_new()
                mts_page.check_sucess()
                domru_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("25. Отправка заявки из попапа по кнопке Подключить из футер для урла Домашний интернет и тв")
    def test_application_popup_button_connect_futer_tv(self, page_fixture, msk_beeline_online_tv):
        page = page_fixture
        page.goto(msk_beeline_online_tv)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.click_connect_button_futer()
        online_beeline_page = OnlineBeelinePage(page=page)
        online_beeline_page.send_popup_from_connection_home_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("26. Проверка всех ссылок для урла Домашний интернет и тв")
    def test_check_all_pages_tv(self, page_fixture, msk_beeline_online_tv):
        page = page_fixture
        page.goto(msk_beeline_online_tv)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_msk_dom()

    @pytest.mark.skip("Попап не высвечивается")
    @allure.title("27. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение! для урла Тарифы")
    def test_application_popup_super_offer_tariffs(self, page_fixture, msk_beeline_online_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(58)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.send_popup_super_offer_dom()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("28. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной желтой кнопки "
                  "звонка в правом нижнем углу для урла Тарифы")
    def test_application_popup_super_offer_red_button_tariffs(self, page_fixture, msk_beeline_online_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.close_coockies()
        mts_page.click_on_red_button()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page.send_popup_super_offer_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("29. Отправка заявки из попапа по кнопке Подключить из хедера для урла Тарифы")
    def test_application_popup_button_connect_tariffs(self, page_fixture, msk_beeline_online_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.click_connect_button()
        online_beeline_page = OnlineBeelinePage(page=page)
        online_beeline_page.send_popup_from_connection_home_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title(
        "30. Отправка заявки с каждой формы на странице с названиями Проверьте подключение вашего дома для урла Тарифы")
    def test_a_lot_of_forms_tariffs(self, page_fixture, msk_beeline_online_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        with allure.step("Проверить возможность подключения билайн по вашему адресу в Москве первый"):
            online_beeline_page = OnlineBeelinePage(page=page)
            online_beeline_page.send_popup_application_connection_home_new()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()

    @allure.title("31. Отправка заявок с карточек тарифа для урла Тарифы")
    def test_application_from_tariff_cards_tariffs(self, page_fixture, msk_beeline_online_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        beeline_page = BeelineOnlinePage(page=page)
        domru_page.close_popup_location()
        tariff_cards = beeline_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = beeline_page.get_tariff_name(i)
                beeline_page.click_tariff_connect_button(i)
                beeline_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                online_beeline_page = OnlineBeelinePage(page=page)
                online_beeline_page.send_popup_from_connection_home_new()
                mts_page.check_sucess()
                domru_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("32. Отправка заявки из попапа по кнопке Подключить из футер для урла Тарифы")
    def test_application_popup_button_connect_futer_tariffs(self, page_fixture, msk_beeline_online_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.click_connect_button_futer()
        online_beeline_page = OnlineBeelinePage(page=page)
        online_beeline_page.send_popup_from_connection_home_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("33. Проверка всех ссылок для урла Тарифы")
    def test_check_all_pages_tariffs(self, page_fixture, msk_beeline_online_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_tariffs)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_msk_dom()

    @pytest.mark.skip("Попап не высвечивается")
    @allure.title("34. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение! для урла Все Тарифы")
    def test_application_popup_super_offer_all_tariffs(self, page_fixture, msk_beeline_online_all_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_all_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        time.sleep(58)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.send_popup_super_offer_dom()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("35. Отправка заявки из попапа Выгодное спецпредложение! по нажатию фиксированной желтой кнопки "
                  "звонка в правом нижнем углу для урла Все Тарифы")
    def test_application_popup_super_offer_red_button_all_tariffs(self, page_fixture, msk_beeline_online_all_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_all_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.close_coockies()
        mts_page.click_on_red_button()
        mts_page.check_popup_super_offer()
        time.sleep(2)
        beeline_page.send_popup_super_offer_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("36. Отправка заявки из попапа по кнопке Подключить из хедера для урла Все Тарифы")
    def test_application_popup_button_connect_all_tariffs(self, page_fixture, msk_beeline_online_all_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_all_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.click_connect_button()
        online_beeline_page = OnlineBeelinePage(page=page)
        online_beeline_page.send_popup_from_connection_home_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title(
        "37. Отправка заявки с каждой формы на странице с названиями Проверьте подключение вашего дома для урла Все Тарифы")
    def test_a_lot_of_forms_all_tariffs(self, page_fixture, msk_beeline_online_all_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_all_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        with allure.step("Проверить возможность подключения билайн по вашему адресу в Москве первый"):
            online_beeline_page = OnlineBeelinePage(page=page)
            online_beeline_page.send_popup_application_connection_home_new()
            mts_page.check_sucess()
            domru_page.close_thankyou_page()

    @allure.title("38. Отправка заявок с карточек тарифа для урла Все Тарифы")
    def test_application_from_tariff_cards_all_tariffs(self, page_fixture, msk_beeline_online_all_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_all_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        beeline_page = BeelineOnlinePage(page=page)
        domru_page.close_popup_location()
        tariff_cards = beeline_page.get_tariff_cards()
        for i in range(len(tariff_cards)):
            with allure.step(f"Подключение тарифа {i + 1}"):
                tariff_name = beeline_page.get_tariff_name(i)
                beeline_page.click_tariff_connect_button(i)
                beeline_page.verify_popup_tariff_name(tariff_name)
                time.sleep(3)
                online_beeline_page = OnlineBeelinePage(page=page)
                online_beeline_page.send_popup_from_connection_home_new()
                mts_page.check_sucess()
                domru_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("39. Отправка заявки из попапа по кнопке Подключить из футер для урла Все Тарифы")
    def test_application_popup_button_connect_futer_all_tariffs(self, page_fixture, msk_beeline_online_all_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_all_tariffs)
        mts_page = MtsHomeOnlinePage(page=page)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.click_connect_button_futer()
        online_beeline_page = OnlineBeelinePage(page=page)
        online_beeline_page.send_popup_from_connection_home_new()
        mts_page.check_sucess()
        domru_page.close_thankyou_page()

    @allure.title("40. Проверка всех ссылок для урла Все Тарифы")
    def test_check_all_pages_all_tariffs(self, page_fixture, msk_beeline_online_all_tariffs):
        page = page_fixture
        page.goto(msk_beeline_online_all_tariffs)
        domru_page = DomRuClass(page=page)
        domru_page.close_popup_location()
        beeline_page = BeelineOnlinePage(page=page)
        beeline_page.check_all_links_msk_dom()