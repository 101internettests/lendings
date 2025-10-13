import time
import allure
import pytest
from pages.main_steps import MainSteps
from pages.page_domru.domru_page import DomRuClass
from locators.domru.domru_locators import LocationPopup
from pages.page_mts.mts_page import MtsHomeOnlinePage, ChoiceRegionPage
from playwright.sync_api import Error as PlaywrightError
from locators.mts.mts_home_online import MTSHomeOnlineMain
from pages.page_beel.beeline_page import BeelineOnlinePage,  BeelineInternetOnlinePage


class TestForms:
    @allure.title("1. Отправка заявки из  попапа Выгодное спецпредложение! по нажатию фиксированной красной кнопки звонка в правом нижнем углу")
    def test_application_popup_super_offer_red_button(self, page_fixture, example_url):
        page = page_fixture
        page.goto(example_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Проверка попапа 'Вы находитесь в городе Х' и закрытие при наличии"):
            domru_page = DomRuClass(page=page)
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass
        with allure.step("Проверка попапа 'Выгодное спецпредложение' и закрытие при наличии (до 10с)"):
            try:
                def strip_xpath(sel: str) -> str:
                    return sel[len("xpath="):] if sel.startswith("xpath=") else sel
                union_xpath = (
                    f"xpath=({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_TEXT)})"
                )
                page.wait_for_selector(union_xpath, state="visible", timeout=10000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass
        steps.open_popup_for_colorful_button()
        steps.send_popup_profit()
        mts_page.check_sucess()
        mts_page.close_thankyou_page()
        # try:
        #     if page.locator(LocationPopup.YES_BUTTON).count() > 0:
        #         domru_page.close_popup_location()
        # except Exception:
        #     pass
        # try:
        #     if page.locator(LocationPopup.CLOSE_POPUP).count() > 0:
        #         domru_page.close_popup()
        # except Exception:
        #     pass
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
        mts_page.close_thankyou_page()

    @allure.title("2. Отправка заявки из попапа  по кнопке Подключить (все кнопки на странице)")
    def test_application_popup_button_connect(self, page_fixture, example_url):
        page = page_fixture
        page.goto(example_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Проверка попапа 'Вы находитесь в городе Х' и закрытие при наличии (до 10с)"):
            domru_page = DomRuClass(page=page)
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass
        with allure.step("Проверка попапа 'Выгодное спецпредложение' и закрытие при наличии (до 50с)"):
            try:
                def strip_xpath(sel: str) -> str:
                    return sel[len("xpath="):] if sel.startswith("xpath=") else sel
                union_xpath = (
                    f"xpath=({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_TEXT)})"
                )
                page.wait_for_selector(union_xpath, state="visible", timeout=50000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass

        with allure.step("Посчитать кнопки и пройти по всем"):
            total = steps.count_connect_buttons()
            assert total > 0, "Не найдено кнопок Подключить"
            for i in range(1, total + 1):
                with allure.step(f"Кнопка #{i}"):
                    steps.click_connect_button_index(i)
                    if i == 1:
                        steps.send_popup_connection()
                    elif i == 2:
                        steps.button_change_city_connection()
                        region_page = ChoiceRegionPage(page=page)
                        time.sleep(2)
                        region_page.fill_region_search_new("Воронеж")
                        region_page.verify_first_region_choice("Воронеж")
                        time.sleep(2)
                        region_page.select_first_region()
                        steps.send_popup_connection_second()
                    else:
                        # 3-я и далее: чередуем 1/2 вариант
                        if i % 2 == 1:
                            steps.send_popup_connection()
                        else:
                            steps.button_change_city_connection()
                            region_page = ChoiceRegionPage(page=page)
                            time.sleep(2)
                            region_page.fill_region_search_new("Воронеж")
                            region_page.verify_first_region_choice("Воронеж")
                            time.sleep(2)
                            region_page.select_first_region()
                            steps.send_popup_connection_second()
                    mts_page.check_sucess()
                    mts_page.close_thankyou_page()

    @allure.title("2.1 Отправка заявок с карточек тарифа")
    def test_application_popup_button_connect_cards(self, page_fixture, example_url):
        page = page_fixture
        page.goto(example_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Проверка попапа 'Вы находитесь в городе Х' и закрытие при наличии (до 10с)"):
            domru_page = DomRuClass(page=page)
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass
        with allure.step("Проверка попапа 'Выгодное спецпредложение' и закрытие при наличии (до 50с)"):
            try:
                def strip_xpath(sel: str) -> str:
                    return sel[len("xpath="):] if sel.startswith("xpath=") else sel
                union_xpath = (
                    f"xpath=({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_TEXT)})"
                )
                page.wait_for_selector(union_xpath, state="visible", timeout=50000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass

        with allure.step("Посчитать кнопки и пройти по всем"):
            total = steps.count_connect_buttons_cards()
            assert total > 0, "Не найдено кнопок Подключить"
            for i in range(1, total + 1):
                with allure.step(f"Кнопка #{i}"):
                    steps.click_connect_button_index_cards(i)
                    if i == 1:
                        steps.send_popup_connection()
                    elif i == 2:
                        steps.button_change_city_connection()
                        region_page = ChoiceRegionPage(page=page)
                        time.sleep(2)
                        region_page.fill_region_search_new("Воронеж")
                        region_page.verify_first_region_choice("Воронеж")
                        time.sleep(2)
                        region_page.select_first_region()
                        steps.send_popup_connection_second()
                    else:
                        # 3-я и далее: чередуем 1/2 вариант
                        if i % 2 == 1:
                            steps.send_popup_connection()
                        else:
                            steps.button_change_city_connection()
                            region_page = ChoiceRegionPage(page=page)
                            time.sleep(2)
                            region_page.fill_region_search_new("Воронеж")
                            region_page.verify_first_region_choice("Воронеж")
                            time.sleep(2)
                            region_page.select_first_region()
                            steps.send_popup_connection_second()
                    mts_page.check_sucess()
                    mts_page.close_thankyou_page()

    @allure.title("3.1 Отправка заявки со ВСЕХ  форм-попапов на странице с названиями Проверить адрес")
    def test_application_popup_button_checkaddress(self, page_fixture, example_url):
        page = page_fixture
        page.goto(example_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Проверка попапа 'Вы находитесь в городе Х' и закрытие при наличии (до 10с)"):
            domru_page = DomRuClass(page=page)
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass
        with allure.step("Проверка попапа 'Выгодное спецпредложение' и закрытие при наличии (до 50с)"):
            try:
                def strip_xpath(sel: str) -> str:
                    return sel[len("xpath="):] if sel.startswith("xpath=") else sel

                union_xpath = (
                    f"xpath=({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_TEXT)})"
                )
                page.wait_for_selector(union_xpath, state="visible", timeout=50000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass

        with allure.step("Посчитать кнопки и пройти по всем"):
            total = steps.count_checkaddress_popup_buttons()
            assert total > 0, "Не найдено кнопок Проверить адрес"
            for i in range(1, total + 1):
                with allure.step(f"Кнопка #{i}"):
                    steps.click_checkaddress_popup_index(i)
                    if i == 1:
                        steps.send_popup_checkaddress()
                    elif i == 2:
                        steps.button_change_city_checkaddress()
                        region_page = ChoiceRegionPage(page=page)
                        time.sleep(2)
                        region_page.fill_region_search_new("Воронеж")
                        region_page.verify_first_region_choice("Воронеж")
                        time.sleep(2)
                        region_page.select_first_region()
                        steps.send_popup_checkaddress_second()
                    else:
                        # 3-я и далее: чередуем 1/2 вариант
                        if i % 2 == 1:
                            steps.send_popup_checkaddress()
                        else:
                            steps.button_change_city_checkaddress()
                            region_page = ChoiceRegionPage(page=page)
                            time.sleep(2)
                            region_page.fill_region_search_new("Воронеж")
                            region_page.verify_first_region_choice("Воронеж")
                            time.sleep(2)
                            region_page.select_first_region()
                            steps.send_popup_checkaddress_second()
                    mts_page.check_sucess()
                    mts_page.close_thankyou_page()

    @allure.title("3.2 Отправка заявки со ВСЕХ  форм на странице с названиями Проверить адрес")
    def test_application_popup_button_checkaddress(self, page_fixture, example_url):
        page = page_fixture
        page.goto(example_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Проверка попапа 'Вы находитесь в городе Х' и закрытие при наличии (до 10с)"):
            domru_page = DomRuClass(page=page)
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass
        with allure.step("Проверка попапа 'Выгодное спецпредложение' и закрытие при наличии (до 50с)"):
            try:
                def strip_xpath(sel: str) -> str:
                    return sel[len("xpath="):] if sel.startswith("xpath=") else sel

                union_xpath = (
                    f"xpath=({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_TEXT)})"
                )
                page.wait_for_selector(union_xpath, state="visible", timeout=50000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass

        with allure.step("Посчитать кол-во блоков и пройти по всем"):
            total = steps.count_checkaddress_blocks()
            assert total > 0, "Не найдено кнопок Проверить адрес"
            for i in range(1, total + 1):
                with allure.step(f"Кнопка #{i}"):
                    if i == 1:
                        steps.send_popup_checkaddress_block(i)
                    elif i == 2:
                        steps.button_change_city_checkaddress_block(i)
                        region_page = ChoiceRegionPage(page=page)
                        time.sleep(2)
                        region_page.fill_region_search_new("Воронеж")
                        region_page.verify_first_region_choice("Воронеж")
                        time.sleep(2)
                        region_page.select_first_region()
                        steps.send_popup_checkaddress_block_second(i)
                    mts_page.check_sucess()
                    mts_page.close_thankyou_page()

    @allure.title("4.1 Отправка заявки с формы Остались вопросы?")
    def test_application_undecided(self, page_fixture, example_url):
        page = page_fixture
        page.goto(example_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Проверка попапа 'Вы находитесь в городе Х' и закрытие при наличии (до 10с)"):
            domru_page = DomRuClass(page=page)
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass
        with allure.step("Проверка попапа 'Выгодное спецпредложение' и закрытие при наличии (до 50с)"):
            try:
                def strip_xpath(sel: str) -> str:
                    return sel[len("xpath="):] if sel.startswith("xpath=") else sel

                union_xpath = (
                    f"xpath=({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_TEXT)})"
                )
                page.wait_for_selector(union_xpath, state="visible", timeout=50000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass

        with allure.step("Посчитать кнопки и пройти по всем"):
            total = steps.count_undecided_blocks()
            assert total > 0, "Не найдено кнопок Проверить адрес"
            for i in range(1, total + 1):
                with allure.step(f"Кнопка #{i}"):
                    if i == 1:
                        steps.send_form_undecided(i)
                    elif i == 2:
                        steps.button_change_city_undecideds(i)
                        region_page = ChoiceRegionPage(page=page)
                        time.sleep(2)
                        region_page.fill_region_search_new("Воронеж")
                        region_page.verify_first_region_choice("Воронеж")
                        time.sleep(2)
                        region_page.select_first_region()
                        steps.send_form_undecided_second(i)
                    else:
                        # 3-я и далее: чередуем 1/2 вариант
                        if i % 2 == 1:
                            steps.send_form_undecided(i)
                        else:
                            steps.button_change_city_undecideds(i)
                            region_page = ChoiceRegionPage(page=page)
                            time.sleep(2)
                            region_page.fill_region_search_new("Воронеж")
                            region_page.verify_first_region_choice("Воронеж")
                            time.sleep(2)
                            region_page.select_first_region()
                            steps.send_form_undecided_second(i)
                    mts_page.check_sucess()
                    mts_page.close_thankyou_page()

    @allure.title("4.2 Отправка заявки с формы Остались вопросы для ТТК")
    def test_application_undecided_ttk(self, page_fixture, undecided_ttk_url):
        page = page_fixture
        page.goto(undecided_ttk_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Проверка попапа 'Вы находитесь в городе Х' и закрытие при наличии (до 10с)"):
            domru_page = DomRuClass(page=page)
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass

            with allure.step("Заполнить форму"):
                steps.send_form_undecided_third()
                mts_page.check_sucess()

    @allure.title("5.1 Проверка формы Бизнес")
    def test_application_business(self, page_fixture, business_url):
        page = page_fixture
        page.goto(business_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Проверка попапа 'Вы находитесь в городе Х' и закрытие при наличии (до 10с)"):
            domru_page = DomRuClass(page=page)
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass
        with allure.step("Проверка попапа 'Выгодное спецпредложение' и закрытие при наличии (до 50с)"):
            try:
                def strip_xpath(sel: str) -> str:
                    return sel[len("xpath="):] if sel.startswith("xpath=") else sel

                union_xpath = (
                    f"xpath=({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_TEXT)})"
                )
                page.wait_for_selector(union_xpath, state="visible", timeout=60000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass

        steps.click_business_button()
        with allure.step("Посчитать кнопки и пройти по всем"):
            total = steps.count_business_buttons()
            print(f"Найдено кнопок Подробнее: {total}")
        with allure.step("Нажать на каждую кнопку, перейти на новую страницу, нажать на кнопку подключения, заполнить форму и вернуться"):
            assert total > 0, "Не найдено кнопок Подробнее"
            for i in range(1, total + 1):
                with allure.step(f"Кнопка Подробнее #{i}"):
                    steps.click_business_button(i)
                    steps.connect_business_page()
                    steps.send_popup_business()
                    mts_page.check_sucess()
                    mts_page.close_thankyou_page()
                    # Вернуться назад к странице со списком кнопок
                    page.go_back()

    @allure.title("5.2 Проверка формы Бизнес для др. урлов")
    def test_application_business_second(self, page_fixture, business_url_second):
        page = page_fixture
        page.goto(business_url_second)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Проверка попапа 'Вы находитесь в городе Х' и закрытие при наличии (до 10с)"):
            domru_page = DomRuClass(page=page)
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass
        with allure.step("Проверка попапа 'Выгодное спецпредложение' и закрытие при наличии (до 50с)"):
            try:
                def strip_xpath(sel: str) -> str:
                    return sel[len("xpath="):] if sel.startswith("xpath=") else sel

                union_xpath = (
                    f"xpath=({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_TEXT)})"
                )
                page.wait_for_selector(union_xpath, state="visible", timeout=30000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass

        steps.click_business_button()
        with allure.step("Посчитать кнопки и пройти по всем"):
            total = steps.count_business_buttons()
            print(f"Найдено кнопок Подробнее: {total}")
        with allure.step(
                "Нажать на каждую кнопку, перейти на новую страницу, нажать на кнопку подключения, заполнить форму и вернуться"):
            assert total > 0, "Не найдено кнопок Подробнее"
            for i in range(1, total + 1):
                with allure.step(f"Кнопка Подробнее #{i}"):
                    if i >= 2:
                        # Для последующих заходов сначала возвращаемся на страницу бизнеса через хедер
                        steps.click_business_button()
                    steps.click_business_button(i)
                    steps.send_popup_business()
                    mts_page.check_sucess()
                    mts_page.close_thankyou_page()

    @allure.title("6 Форма переезд")
    def test_application_moving(self, page_fixture, moving_url):
        page = page_fixture
        page.goto(moving_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Проверка попапа 'Вы находитесь в городе Х' и закрытие при наличии (до 10с)"):
            domru_page = DomRuClass(page=page)
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass
        with allure.step("Проверка попапа 'Выгодное спецпредложение' и закрытие при наличии (до 50с)"):
            try:
                def strip_xpath(sel: str) -> str:
                    return sel[len("xpath="):] if sel.startswith("xpath=") else sel

                union_xpath = (
                    f"xpath=({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_TEXT)})"
                )
                page.wait_for_selector(union_xpath, state="visible", timeout=10000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass

        with allure.step("Посчитать кнопки и пройти по всем"):
            total = steps.count_moving_popup_buttons()
            assert total > 0, "Не найдено кнопок Проверить адрес"
            for i in range(1, total + 1):
                with allure.step(f"Кнопка #{i}"):
                    steps.click_moving_popup_index(i)
                    if i == 1:
                        steps.send_popup_moving()
                    elif i == 2:
                        steps.button_change_city_moving()
                        region_page = ChoiceRegionPage(page=page)
                        time.sleep(2)
                        region_page.fill_region_search_new("Воронеж")
                        region_page.verify_first_region_choice("Воронеж")
                        time.sleep(2)
                        region_page.select_first_region()
                        steps.send_popup_moving_second()
                    mts_page.check_sucess()
                    mts_page.close_thankyou_page()

    @allure.title("7 Попап Заявка на экспресс подключение")
    def test_application_express_connection(self, page_fixture, example_url):
        page = page_fixture
        page.goto(example_url)
        mts_page = MtsHomeOnlinePage(page=page)
        steps = MainSteps(page=page)
        region_page = ChoiceRegionPage(page=page)
        with allure.step("Проверка попапа 'Вы находитесь в городе Х' и закрытие при наличии (до 10с)"):
            domru_page = DomRuClass(page=page)
            try:
                if page.locator(LocationPopup.YES_BUTTON).count() > 0:
                    domru_page.close_popup_location()
            except Exception:
                pass
        with allure.step("Проверка попапа 'Выгодное спецпредложение' и закрытие при наличии (до 50с)"):
            try:
                def strip_xpath(sel: str) -> str:
                    return sel[len("xpath="):] if sel.startswith("xpath=") else sel

                union_xpath = (
                    f"xpath=({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_HEADER_SECOND)})"
                    f" | ({strip_xpath(MTSHomeOnlineMain.SUPER_OFFER_TEXT)})"
                )
                page.wait_for_selector(union_xpath, state="visible", timeout=50000)
                region_page.close_popup_super_offer_all()
            except Exception:
                pass
        with allure.step("Открыть попап"):
            steps.open_popup_express_connection_button()
        with allure.step("отправить первый вариант по кнопке"):
            steps.send_popup_express_connection()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()
        with allure.step("отправить второй вариант по кнопке"):
            steps.open_popup_express_connection_button()
            steps.button_change_city_express_connection()
            region_page = ChoiceRegionPage(page=page)
            time.sleep(2)
            region_page.fill_region_search_new("Воронеж")
            region_page.verify_first_region_choice("Воронеж")
            time.sleep(2)
            region_page.select_first_region()
            steps.send_popup_express_connection_second()
            mts_page.check_sucess()
            mts_page.close_thankyou_page()




