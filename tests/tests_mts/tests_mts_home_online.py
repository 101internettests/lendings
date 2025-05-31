import os
import time
import allure
from playwright.sync_api import sync_playwright
from pages.page_mts.mts_page import MtsHomeOnlinePage
HEADLESS = True if os.getenv("HEADLESS") == "True" else False

class TestMolMainRegionPage:
    # @allure.title("1.1. Проверка работы сайта при отсутствии сертификата")
    # def test_check_website_without_sertificate(self):
    #     full_url = "https://mts-home.online/"
    #     with sync_playwright() as playwright:
    #         browser = playwright.chromium.launch()
    #         page = browser.new_page()
    #         page.goto(full_url)
    #         pass

    @allure.title("2. Отправка заявки из всплывающего через некоторое время, после захода на страницу, "
                  "попапа Выгодное спецпредложение!")
    def test_application_popup_super_offer(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            time.sleep(65)
            mts_page.check_popup_super_offer()
            time.sleep(2)
            mts_page.send_popup_super_offer()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("3. Отправка заявки из  попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            mts_page.click_on_red_button()
            mts_page.check_popup_super_offer()
            time.sleep(2)
            mts_page.send_popup_super_offer()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("4. Отправка заявки из попапа  по кнопке Подключить из хедера")
    def test_application_popup_button_connect(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            mts_page.click_connect_button()
            mts_page.send_popup_application_connection()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("5. Отправка заявки из попапа по кнопке Проверить адрес из хедера")
    def test_application_popup_button_check_address(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            mts_page.click_check_address_button()
            mts_page.send_popup_application_connection_your_address()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("6. Отправка заявки из попапа Заявка на подключение с  кликабельного баннера, который идет сразу "
                  "после заголовка Подключить домашний интернет МТС")
    def test_application_popup_clicable_banner(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            mts_page.click_on_banner()
            mts_page.send_popup_application_connection()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("7. Отправка заявки со ВСЕХ  форм на странице с названием Проверьте возможность подключения по "
                  "вашему адресу")
    def test_application_from_all_forms(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            mts_page.send_popup_application_check_connection()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()
            time.sleep(3)
            mts_page.send_popup_application_check_connection_near_futer()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("8. Отправка заявок с карточек тарифа (С КАЖДОЙ, КОТОРАЯ ЕСТЬ НА СТРАНИЦЕ)")
    def test_application_from_tariff_cards(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            tariff_cards = mts_page.get_tariff_cards()
            for i in range(len(tariff_cards)):
                with allure.step(f"Подключение тарифа {i + 1}"):
                    tariff_name = mts_page.get_tariff_name(i)
                    mts_page.click_tariff_connect_button(i)
                    mts_page.verify_popup_tariff_name(tariff_name)
                    time.sleep(3)
                    mts_page.send_tariff_connection_request()
                    mts_page.check_sucess()
                    mts_page.close_thankyou_page()
                    time.sleep(2)

    @allure.title("9. Отправка заявки из попапа по кнопке Подключить из футера")
    def test_application_popup_button_connect_futer(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            mts_page.click_connect_button_futer()
            mts_page.send_popup_application_connection()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("10. Отправка заявки из попапа  по кнопке Проверить адрес из футера")
    def test_application_popup_button_check_address_futer(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            mts_page.click_check_address_button_futer()
            mts_page.send_popup_application_connection_your_address()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()

    @allure.title("11. Проверка всех ссылок и функционала на всех страницах")
    def test_check_all_pages(self):
        urls = [
            "https://mts-home.online/",
            "https://mts-home.online/domashnij-internet",
            "https://mts-home.online/internet-i-televidenie",
            "https://mts-home.online/internet-tv-mobile",
            "https://mts-home.online/semejnye-tarify"
        ]
        
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            context = browser.new_context()
            page = context.new_page()
            mts_page = MtsHomeOnlinePage(page=page)
            
            for url in urls:
                with allure.step(f"Тестирование страницы {url}"):
                    # Переходим на страницу
                    page.goto(url)
                    if url == "https://mts-home.online/":
                        mts_page.check_all_links()
                    
                    # Для всех страниц выполняем тесты 2-10
                    for test_number in range(2, 11):
                        with allure.step(f"Выполнение теста #{test_number}"):
                            if test_number == 2:
                                time.sleep(65)
                                mts_page.check_popup_super_offer()
                                time.sleep(2)
                                mts_page.send_popup_super_offer()
                                mts_page.check_sucess()
                                mts_page.close_thankyou_page()
                            elif test_number == 3:
                                mts_page.click_on_red_button()
                                mts_page.check_popup_super_offer()
                                time.sleep(2)
                                mts_page.send_popup_super_offer()
                                mts_page.check_sucess()
                                mts_page.close_thankyou_page()
                            elif test_number == 4:
                                mts_page.click_connect_button()
                                mts_page.send_popup_application_connection()
                                mts_page.check_sucess()
                                mts_page.close_thankyou_page()
                            elif test_number == 5:
                                mts_page.click_check_address_button()
                                mts_page.send_popup_application_connection_your_address()
                                mts_page.check_sucess()
                                mts_page.close_thankyou_page()
                            elif test_number == 6:
                                mts_page.click_on_banner()
                                mts_page.send_popup_application_connection()
                                mts_page.check_sucess()
                                mts_page.close_thankyou_page()
                            elif test_number == 7:
                                mts_page.send_popup_application_check_connection()
                                mts_page.check_sucess()
                                mts_page.close_thankyou_page()
                                time.sleep(3)
                                mts_page.send_popup_application_check_connection_near_futer()
                                mts_page.check_sucess()
                                mts_page.close_thankyou_page()
                            elif test_number == 8:
                                tariff_cards = mts_page.get_tariff_cards()
                                for i in range(len(tariff_cards)):
                                    with allure.step(f"Подключение тарифа {i + 1}"):
                                        tariff_name = mts_page.get_tariff_name(i)
                                        mts_page.click_tariff_connect_button(i)
                                        mts_page.verify_popup_tariff_name(tariff_name)
                                        time.sleep(3)
                                        mts_page.send_tariff_connection_request()
                                        mts_page.check_sucess()
                                        mts_page.close_thankyou_page()
                                        time.sleep(2)
                            elif test_number == 9:
                                mts_page.click_connect_button_futer()
                                mts_page.send_popup_application_connection()
                                mts_page.check_sucess()
                                mts_page.close_thankyou_page()
                            elif test_number == 10:
                                mts_page.click_check_address_button_futer()
                                mts_page.send_popup_application_connection_your_address()
                                mts_page.check_sucess()
                                mts_page.close_thankyou_page()
                            time.sleep(2)



