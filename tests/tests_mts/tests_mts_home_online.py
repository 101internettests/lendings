import os
import time
import allure
from playwright.sync_api import sync_playwright
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import expect

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

    @allure.title("11. Проверка всех ссылок")
    def test_check_all_pages(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            mts_page.check_all_links()

    @allure.title("12.1. Повторить кейсы 2-10 на странице Домашнего интернета")
    def test_check_domashnij_internet(self):
        full_url = "https://mts-home.online/domashnij-internet"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            with allure.step("Форма 'Выгодное спецпредложение' через таймер"):
                time.sleep(65)
                mts_page.check_popup_super_offer()
                time.sleep(2)
                mts_page.send_popup_super_offer_other_pages()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 2. Форма "Выгодное спецпредложение" через красную кнопку
            with allure.step("Форма 'Выгодное спецпредложение' через красную кнопку"):
                mts_page.click_on_red_button()
                mts_page.check_popup_super_offer()
                time.sleep(2)
                mts_page.send_popup_super_offer_other_pages()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 3. Форма через кнопку "Подключить" в хедере
            with allure.step("Форма через кнопку 'Подключить' в хедере"):
                mts_page.click_connect_button()
                time.sleep(3)
                mts_page.send_popup_application_connection_other()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 4. Форма через кнопку "Проверить адрес" в хедере
            with allure.step("Форма через кнопку 'Проверить адрес' в хедере"):
                mts_page.click_check_address_button()
                mts_page.send_popup_application_connection_your_address_other()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 6. Формы "Проверьте возможность подключения"
            with allure.step("Формы 'Проверьте возможность подключения'"):
                mts_page.send_popup_application_check_connection()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(3)
            # 7. Формы с карточек тарифов
            with allure.step("Формы с карточек тарифов"):
                tariff_cards = mts_page.get_tariff_cards()
                for i in range(len(tariff_cards)):
                    with allure.step(f"Подключение тарифа {i + 1}"):
                        tariff_name = mts_page.get_tariff_name(i)
                        mts_page.click_tariff_connect_button(i)
                        mts_page.verify_popup_tariff_name(tariff_name)
                        time.sleep(3)
                        mts_page.send_tariff_connection_request_other()
                        mts_page.check_sucess()
                        mts_page.close_thankyou_page()
                        time.sleep(2)
            # 8. Форма через кнопку "Подключить" в футере
            with allure.step("Форма через кнопку 'Подключить' в футере"):
                mts_page.click_connect_button_futer()
                mts_page.send_popup_application_connection_other()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 9. Форма через кнопку "Проверить адрес" в футере
            with allure.step("Форма через кнопку 'Проверить адрес' в футере"):
                mts_page.click_check_address_button_futer()
                mts_page.send_popup_application_connection_your_address_other()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("12.2. Повторить кейсы 2-10 на странице Интернет и телевидение")
    def test_check_internet_tv(self):
        full_url = "https://mts-home.online/internet-i-televidenie"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            # 1. Форма "Выгодное спецпредложение" через таймер
            with allure.step("Форма 'Выгодное спецпредложение' через таймер"):
                time.sleep(65)
                mts_page.check_popup_super_offer()
                time.sleep(2)
                mts_page.send_popup_super_offer_other_pages()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 2. Форма "Выгодное спецпредложение" через красную кнопку
            with allure.step("Форма 'Выгодное спецпредложение' через красную кнопку"):
                mts_page.click_on_red_button()
                mts_page.check_popup_super_offer()
                time.sleep(2)
                mts_page.send_popup_super_offer_other_pages()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 3. Форма через кнопку "Подключить" в хедере
            with allure.step("Форма через кнопку 'Подключить' в хедере"):
                mts_page.click_connect_button()
                time.sleep(3)
                mts_page.send_popup_application_connection_another()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 4. Форма через кнопку "Проверить адрес" в хедере
            with allure.step("Форма через кнопку 'Проверить адрес' в хедере"):
                mts_page.click_check_address_button()
                mts_page.send_popup_application_connection_your_address_another()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 6. Формы "Проверьте возможность подключения"
            with allure.step("Формы 'Проверьте возможность подключения'"):
                mts_page.send_popup_application_check_connection()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(3)
            # 7. Формы с карточек тарифов
            with allure.step("Формы с карточек тарифов"):
                tariff_cards = mts_page.get_tariff_cards()
                for i in range(len(tariff_cards)):
                    with allure.step(f"Подключение тарифа {i + 1}"):
                        tariff_name = mts_page.get_tariff_name(i)
                        mts_page.click_tariff_connect_button(i)
                        mts_page.verify_popup_tariff_name(tariff_name)
                        time.sleep(3)
                        mts_page.send_tariff_connection_request_another()
                        mts_page.check_sucess()
                        mts_page.close_thankyou_page()
                        time.sleep(2)
            # 8. Форма через кнопку "Подключить" в футере
            with allure.step("Форма через кнопку 'Подключить' в футере"):
                mts_page.click_connect_button_futer()
                mts_page.send_popup_application_connection_another()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 9. Форма через кнопку "Проверить адрес" в футере
            with allure.step("Форма через кнопку 'Проверить адрес' в футере"):
                mts_page.click_check_address_button_futer()
                time.sleep(3)
                mts_page.send_popup_application_connection_your_address_another()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("12.3. Повторить кейсы 2-10 на странице Интернет, телевидение и мобильная связь")
    def test_check_internet_tv_mobile(self):
        full_url = "https://mts-home.online/internet-tv-mobile"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            # 1. Форма "Выгодное спецпредложение" через таймер
            with allure.step("Форма 'Выгодное спецпредложение' через таймер"):
                time.sleep(65)
                mts_page.check_popup_super_offer()
                time.sleep(2)
                mts_page.send_popup_super_offer_other_pages()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 2. Форма "Выгодное спецпредложение" через красную кнопку
            with allure.step("Форма 'Выгодное спецпредложение' через красную кнопку"):
                mts_page.click_on_red_button()
                mts_page.check_popup_super_offer()
                time.sleep(2)
                mts_page.send_popup_super_offer_other_pages()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 3. Форма через кнопку "Подключить" в хедере
            with allure.step("Форма через кнопку 'Подключить' в хедере"):
                mts_page.click_connect_button()
                time.sleep(3)
                mts_page.send_popup_application_connection_another()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 4. Форма через кнопку "Проверить адрес" в хедере
            with allure.step("Форма через кнопку 'Проверить адрес' в хедере"):
                mts_page.click_check_address_button()
                mts_page.send_popup_application_connection_your_address_another()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 6. Формы "Проверьте возможность подключения"
            with allure.step("Формы 'Проверьте возможность подключения'"):
                mts_page.send_popup_application_check_connection()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(3)
            # 7. Формы с карточек тарифов
            with allure.step("Формы с карточек тарифов"):
                tariff_cards = mts_page.get_tariff_cards()
                for i in range(len(tariff_cards)):
                    with allure.step(f"Подключение тарифа {i + 1}"):
                        tariff_name = mts_page.get_tariff_name(i)
                        mts_page.click_tariff_connect_button(i)
                        mts_page.verify_popup_tariff_name(tariff_name)
                        time.sleep(3)
                        mts_page.send_tariff_connection_request_another()
                        mts_page.check_sucess()
                        mts_page.close_thankyou_page()
                        time.sleep(2)
            # 8. Форма через кнопку "Подключить" в футере
            with allure.step("Форма через кнопку 'Подключить' в футере"):
                mts_page.click_connect_button_futer()
                mts_page.send_popup_application_connection_another()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 9. Форма через кнопку "Проверить адрес" в футере
            with allure.step("Форма через кнопку 'Проверить адрес' в футере"):
                mts_page.click_check_address_button_futer()
                time.sleep(3)
                mts_page.send_popup_application_connection_your_address_another()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("12.4. Повторить кейсы 2-10 на странице Семейные тарифы МТС")
    def test_check_semejnye_tarify(self):
        full_url = "https://mts-home.online/semejnye-tarify"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            # 1. Форма "Выгодное спецпредложение" через таймер
            with allure.step("Форма 'Выгодное спецпредложение' через таймер"):
                time.sleep(65)
                mts_page.check_popup_super_offer()
                time.sleep(2)
                mts_page.send_popup_super_offer_other_pages()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 2. Форма "Выгодное спецпредложение" через красную кнопку
            with allure.step("Форма 'Выгодное спецпредложение' через красную кнопку"):
                mts_page.click_on_red_button()
                mts_page.check_popup_super_offer()
                time.sleep(2)
                mts_page.send_popup_super_offer_other_pages()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 3. Форма через кнопку "Подключить" в хедере
            with allure.step("Форма через кнопку 'Подключить' в хедере"):
                mts_page.click_connect_button()
                time.sleep(3)
                mts_page.send_popup_application_connection_another()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 4. Форма через кнопку "Проверить адрес" в хедере
            with allure.step("Форма через кнопку 'Проверить адрес' в хедере"):
                mts_page.click_check_address_button()
                mts_page.send_popup_application_connection_your_address_another()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 6. Формы "Проверьте возможность подключения"
            with allure.step("Формы 'Проверьте возможность подключения'"):
                mts_page.send_popup_application_check_connection()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(3)
            # 7. Формы с карточек тарифов
            with allure.step("Формы с карточек тарифов"):
                tariff_cards = mts_page.get_tariff_cards()
                for i in range(len(tariff_cards)):
                    with allure.step(f"Подключение тарифа {i + 1}"):
                        tariff_name = mts_page.get_tariff_name(i)
                        mts_page.click_tariff_connect_button(i)
                        mts_page.verify_popup_tariff_name(tariff_name)
                        time.sleep(3)
                        mts_page.send_tariff_connection_request_another()
                        mts_page.check_sucess()
                        mts_page.close_thankyou_page()
                        time.sleep(2)
            # 8. Форма через кнопку "Подключить" в футере
            with allure.step("Форма через кнопку 'Подключить' в футере"):
                mts_page.click_connect_button_futer()
                mts_page.send_popup_application_connection_another()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)
            # 9. Форма через кнопку "Проверить адрес" в футере
            with allure.step("Форма через кнопку 'Проверить адрес' в футере"):
                mts_page.click_check_address_button_futer()
                time.sleep(3)
                mts_page.send_popup_application_connection_your_address_another()
                mts_page.check_sucess()
                mts_page.close_thankyou_page()
                time.sleep(2)

    @allure.title("13.1. Выбор региона СПб из хедера")
    def test_choose_region_header_spb(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            mts_page.click_region_choice_button()
            region_page = ChoiceRegionPage(page=page)
            with allure.step("Выбрать СПб"):
                region_page.fill_region_search("Санкт")
                region_page.verify_first_region_choice("Санкт-Петербург")
                region_page.select_first_region()
                region_page.verify_region_button_text("Санкт-Петербург")

    @allure.title("13.2. Выбор региона Азнакаево из хедера")
    def test_choose_region_header_azn(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            region_page = ChoiceRegionPage(page=page)
            with allure.step("Выбрать Азнакаево"):
                mts_page.click_region_choice_button()
                region_page.fill_region_search("Азнак")
                region_page.verify_first_region_choice("Азнакаево")
                region_page.select_first_region()
                region_page.verify_region_button_text("Азнакаево")

    @allure.title("14.1. Выбор регион СПб из футера")
    def test_choose_region_futer_spb(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            mts_page.click_region_choice_button_futer()
            region_page = ChoiceRegionPage(page=page)
            with allure.step("Выбрать СПб"):
                region_page.fill_region_search("Санкт")
                region_page.verify_first_region_choice("Санкт-Петербург")
                region_page.select_first_region()
                region_page.verify_region_button_text("Санкт-Петербург")

    @allure.title("14.2. Выбор региона Азнакаево из футера")
    def test_choose_region_futer_azn(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)
            region_page = ChoiceRegionPage(page=page)
            with allure.step("Выбрать Азнакаево"):
                mts_page.click_region_choice_button_futer()
                region_page.fill_region_search("Азнак")
                region_page.verify_first_region_choice("Азнакаево")
                region_page.select_first_region()
                region_page.verify_region_button_text("Азнакаево")

    @allure.title("15. Переход по всем ссылкам городов на странице выбора города")
    def test_choose_region_futer_azn(self):
        full_url = "https://mts-home.online/"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(full_url)
            mts_page = MtsHomeOnlinePage(page=page)

