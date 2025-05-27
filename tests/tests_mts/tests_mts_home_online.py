import os
import time
import allure
from playwright.sync_api import sync_playwright
from pages.page_mts.mts_page import MtsHomeOnlinePage

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
            browser = playwright.chromium.launch()
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            time.sleep(65)
            mts_page.check_popup_super_offer()
            time.sleep(2)
            mts_page.send_popup_super_offer()
            mts_page.close_thankyou_page()

    @allure.title("3. Отправка заявки из  попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки "
                  "звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            mts_page.click_on_red_button()
            mts_page.check_popup_super_offer()
            time.sleep(2)
            mts_page.send_popup_super_offer()
            mts_page.close_thankyou_page()

