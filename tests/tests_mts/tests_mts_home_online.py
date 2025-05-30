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

    @allure.title("5. Отправка заявки из попапа  по кнопке Проверить адрес из хедера")
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
            
            # Получаем все тарифные карточки
            tariff_cards = mts_page.get_tariff_cards()
            
            # Для каждой карточки выполняем сценарий подключения
            for i in range(len(tariff_cards)):
                with allure.step(f"Подключение тарифа {i + 1}"):
                    # Получаем название тарифа
                    tariff_name = mts_page.get_tariff_name(i)
                    
                    # Нажимаем кнопку "Подключить"
                    mts_page.click_tariff_connect_button(i)
                    
                    # Проверяем название тарифа в попапе
                    mts_page.verify_popup_tariff_name(tariff_name)
                    
                    # Отправляем заявку
                    mts_page.send_tariff_connection_request()
                    mts_page.check_sucess()
                    mts_page.close_thankyou_page()
                    time.sleep(2)


