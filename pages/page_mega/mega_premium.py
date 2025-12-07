import time
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from locators.mega.mega_premium_locators import ThankYouPage, CheckConnectApplicationForms, ClarifyPopUp, MainPageLocs
from locators.mega.mega_premium_locators import ApplicationConnection
from urllib.parse import urlparse


class MegaPremiumOnline(BasePage):
    @allure.title("Закрыть страницу благодарности")
    def close_thankyou_page(self):
        try:
            self.page.locator(ThankYouPage.CRUSIFIX_CLOSE).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось закрыть страницу благодарности.\n"
                "Возможно, кнопка закрытия недоступна, перекрыта или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу первый")
    def send_popup_application_check_connection_first(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(CheckConnectApplicationForms.FIRST_CITY).fill("Тестгород")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести город в форму проверки адреса (первый блок).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(CheckConnectApplicationForms.FIRST_ADDRESS).fill("Тестулица")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести адрес в форму проверки адреса (первый блок).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(CheckConnectApplicationForms.FIRST_PHONE_INPUT).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форму проверки адреса (первый блок).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(CheckConnectApplicationForms.FIRST_CHECK_ADDRESS_BUTTON).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' (первый блок).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу второй")
    def send_popup_application_check_connection_second(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(CheckConnectApplicationForms.SECOND_CITY).fill("Тестгород")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести город в форму проверки адреса (второй блок).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(CheckConnectApplicationForms.SECOND_ADDRESS).fill("Тестулица")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести адрес в форму проверки адреса (второй блок).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(CheckConnectApplicationForms.SECOND_PHONE_INPUT).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форму проверки адреса (второй блок).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(CheckConnectApplicationForms.SECOND_CHECK_ADDRESS_BUTTON).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' (второй блок).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Отправить заявку в форму Не определились с тарифом?")
    def send_popup_application_tariff_form(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(CheckConnectApplicationForms.TARIFF_CITY).fill("Тестгород")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести город в форму 'Не определились с тарифом?'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(CheckConnectApplicationForms.TARIFF_ADDRESS).fill("Тестулица")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести адрес в форму 'Не определились с тарифом?'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(CheckConnectApplicationForms.TARIFF_PHONE_INPUT).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форму 'Не определились с тарифом?'.\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(CheckConnectApplicationForms.TARIFF_CHECK_ADDRESS_BUTTON).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось отправить форму 'Не определились с тарифом?'.\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )

    @allure.title("Кликнуть по кнопке Уточнить")
    def click_clarify_button(self):
        try:
            self.page.locator(ClarifyPopUp.CLARIFY_BUTTON).click()
        except Exception as e:
            raise AssertionError(
                "Не удалось нажать кнопку 'Уточнить'.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(MainPageLocs.TARIFFS_CARDS).all()

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        try:
            self.page.locator(MainPageLocs.TARIFF_CONNECT_BUTTONS).nth(card_index).click()
        except Exception as e:
            raise AssertionError(
                f"Не удалось нажать кнопку 'Подключить' на карточке тарифа #{card_index}.\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Проверить ссылку и убедиться, что страница существует")
    def check_link(self, locator, link_name):
        """
        Упрощённая проверка ссылки: видимость, href, клик, отсутствие 404
        :param locator: локатор ссылки
        :param link_name: название ссылки для отчета
        """
        with allure.step(f"Проверка ссылки {link_name}"):
            link = self.page.locator(locator)
            expect(link).to_be_visible()
            href = link.get_attribute('href')
            if not href:
                allure.attach(f"Ссылка {link_name} не имеет атрибута href", "warning")
                return
            link.scroll_into_view_if_needed()
            time.sleep(1)
            with self.page.context.expect_page() as new_page_info:
                link.click(modifiers=["Control"])
            new_page = new_page_info.value
            new_page.wait_for_load_state("networkidle", timeout=15000)
            expect(new_page).not_to_have_url("**/404")
            new_page.close()

    @allure.title("Проверить все ссылки на странице")
    def check_header_links(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in MainPageLocs.HEADER_LINKS.items():
                self.check_link(locator, f"Header: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Проверить все ссылки на странице")
    def check_footer_links(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in MainPageLocs.POPUP_LINKS.items():
                self.check_link(locator, f"Header: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Проверить все ссылки на странице")
    def check_header_links_mega(self):
        """
        Проверяет, что клики по ссылкам хедера (//li[@class='list__item-header']) c якорями
        действительно прокручивают страницу к соответствующей области (якорю) на этой же странице.
        Нехэширные ссылки пропускаются.
        """
        header_items = self.page.locator("xpath=//li[@class='list__item-header']")
        total = header_items.count()
        if total == 0:
            raise AssertionError("Не найдено элементов хедера: //li[@class='list__item-header']")

        for i in range(total):
            item = header_items.nth(i)
            anchor = item.locator("a").first
            if anchor.count() == 0:
                continue
            href = anchor.get_attribute("href") or ""
            if not href:
                continue

            parsed = urlparse(href)
            target_id = ""
            if href.startswith("#"):
                target_id = href[1:]
            elif parsed.fragment:
                # Ссылка вида /path#id — считаем якорём, если ведёт на ту же страницу
                current = urlparse(self.page.url)
                if (parsed.scheme in ("", current.scheme)
                        and parsed.netloc in ("", current.netloc)
                        and (parsed.path in ("", current.path))):
                    target_id = parsed.fragment
            if not target_id:
                # Это не якорная ссылка — пропускаем
                continue

            # Разрешаем возможные дубликаты id: выбираем первый найденный элемент
            css_target = self.page.locator(f"#{target_id}")
            xpath_target = self.page.locator(f"xpath=//*[@id='{target_id}' or @name='{target_id}']")
            total_css = css_target.count()
            total_xpath = xpath_target.count()
            if total_css > 0:
                target_locator = css_target.first
            elif total_xpath > 0:
                target_locator = xpath_target.first
            else:
                raise AssertionError(f"Целевой якорь #{target_id} не найден на странице")

            # Кликаем без ожидания новой вкладки — переход внутри страницы
            anchor.scroll_into_view_if_needed()
            anchor.click(force=True)

            # Пытаемся дождаться появления хэша в URL (если он должен появиться)
            try:
                expect(self.page).to_have_url(f"**#{target_id}", timeout=3000)
            except Exception:
                # Если хэш не проявился, допустимо — проверим скролл к элементу
                pass

            # Проверяем, что цель попала в видимую область
            box = target_locator.bounding_box()
            if box is None:
                # Как минимум элемент должен стать видимым
                expect(target_locator).to_be_visible(timeout=2000)
            else:
                try:
                    viewport = self.page.viewport_size or {"height": 800}
                    vh = viewport.get("height", 800)
                    assert 0 <= box["y"] < vh + 10, f"Якорь #{target_id} не прокручен в видимую область (y={box['y']})"
                except Exception:
                    # Фолбэк на видимость
                    expect(target_locator).to_be_visible(timeout=2000)

    @allure.title("Проверить все ссылки на странице")
    def check_footer_links_mega(self):
        """
        Проверяет, что клики по ссылкам хедера (//li[@class='list__item-header']) c якорями
        действительно прокручивают страницу к соответствующей области (якорю) на этой же странице.
        Нехэширные ссылки пропускаются.
        """
        header_items = self.page.locator("xpath=//li[@class='list__item-footer']")
        total = header_items.count()
        if total == 0:
            raise AssertionError("Не найдено элементов хедера")

        for i in range(total):
            item = header_items.nth(i)
            anchor = item.locator("a").first
            if anchor.count() == 0:
                continue
            href = anchor.get_attribute("href") or ""
            if not href:
                continue

            parsed = urlparse(href)
            target_id = ""
            if href.startswith("#"):
                target_id = href[1:]
            elif parsed.fragment:
                # Ссылка вида /path#id — считаем якорём, если ведёт на ту же страницу
                current = urlparse(self.page.url)
                if (parsed.scheme in ("", current.scheme)
                        and parsed.netloc in ("", current.netloc)
                        and (parsed.path in ("", current.path))):
                    target_id = parsed.fragment
            if not target_id:
                # Это не якорная ссылка — пропускаем
                continue

            # Разрешаем возможные дубликаты id: выбираем первый найденный элемент
            css_target = self.page.locator(f"#{target_id}")
            xpath_target = self.page.locator(f"xpath=//*[@id='{target_id}' or @name='{target_id}']")
            total_css = css_target.count()
            total_xpath = xpath_target.count()
            if total_css > 0:
                target_locator = css_target.first
            elif total_xpath > 0:
                target_locator = xpath_target.first
            else:
                raise AssertionError(f"Целевой якорь #{target_id} не найден на странице")

            # Кликаем без ожидания новой вкладки — переход внутри страницы
            anchor.scroll_into_view_if_needed()
            anchor.click(force=True)

            # Пытаемся дождаться появления хэша в URL (если он должен появиться)
            try:
                expect(self.page).to_have_url(f"**#{target_id}", timeout=3000)
            except Exception:
                # Если хэш не проявился, допустимо — проверим скролл к элементу
                pass

            # Проверяем, что цель попала в видимую область
            box = target_locator.bounding_box()
            if box is None:
                # Как минимум элемент должен стать видимым
                expect(target_locator).to_be_visible(timeout=2000)
            else:
                try:
                    viewport = self.page.viewport_size or {"height": 800}
                    vh = viewport.get("height", 800)
                    assert 0 <= box["y"] < vh + 10, f"Якорь #{target_id} не прокручен в видимую область (y={box['y']})"
                except Exception:
                    # Фолбэк на видимость
                    expect(target_locator).to_be_visible(timeout=2000)


    @allure.title("Проверить все ссылки на странице")
    def check_popup_links(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in MainPageLocs.POPUP_LINKS.items():
                self.check_link(locator, f"Header: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Проверить все ссылки на странице")
    def check_popup_links_moskva(self):
        """Проверяет все ссылки в хедере и футере"""
        try:
            # Проверяем ссылки в хедере
            for name, locator in MainPageLocs.MEGA_HEADER.items():
                self.check_link(locator, f"Header: {name}")

            for name, locator in MainPageLocs.MEGA_FUTER.items():
                self.check_link(locator, f"Header: {name}")

            for name, locator in MainPageLocs.POPUP_LINKS.items():
                self.check_link(locator, f"Header: {name}")
        except Exception:
            raise AssertionError("Не все ссылки были проверены, возможно попап перекрыл экран или ссылки пропали")

    @allure.title("Нажать на кнопку Не смогли найти город")
    def click_button_dont_find_city(self):
        self.page.locator(MainPageLocs.BUTTON_DONT_FIND_BUTTON).click()
        time.sleep(2)

    @allure.title("Отправить заявку в попап и проверить успешность")
    def send_popup_super_offer(self):
        with allure.step("Заполнить попап и отправить заявку"):
            expect(self.page.locator(CheckConnectApplicationForms.SECOND_PHONE_INPUT)).to_be_visible(timeout=65000)
            self.page.locator(CheckConnectApplicationForms.SECOND_PHONE_INPUT).fill("99999999999")
            self.page.locator(CheckConnectApplicationForms.POPUP_SEND_BUTTON).click()
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            self.page.locator(ApplicationConnection.NAME_INPUT).fill("Тестимя")
            time.sleep(1)
            self.page.locator(CheckConnectApplicationForms.TARIFF_PHONE_INPUT).fill("99999999999")
            time.sleep(1)
            self.page.locator(ApplicationConnection.POPUP_SEND_BUTTON).click()
            time.sleep(4)


class MegaHomeInternet(BasePage):

    @allure.title("Отправить заявку в форму Проверьте возможность подключения по вашему адресу первый")
    def send_popup_application_check_connection_first(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(CheckConnectApplicationForms.HOME_MEGA_CITY).fill("Тестулица")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести адрес/город в форму проверки адреса (домашний интернет, первый блок).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(2)
            try:
                self.page.locator(CheckConnectApplicationForms.FIRST_PHONE_INPUT).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в форму проверки адреса (домашний интернет, первый блок).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(CheckConnectApplicationForms.FIRST_CHECK_ADDRESS_BUTTON).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку 'Проверить адрес' (домашний интернет, первый блок).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Отправить заявку в попап с названием Заявка на подключение")
    def send_popup_application_connection(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationConnection.NAME_INPUT).fill("Тестимя")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести имя в попапе 'Заявка на подключение' (домашний интернет).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(CheckConnectApplicationForms.TARIFF_PHONE_INPUT).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе 'Заявка на подключение' (домашний интернет).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(1)
            try:
                self.page.locator(ApplicationConnection.POPUP_SEND_BUTTON).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось нажать кнопку отправки в попапе 'Заявка на подключение' (домашний интернет).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)

    @allure.title("Получить список всех тарифных карточек")
    def get_tariff_cards(self):
        return self.page.locator(MainPageLocs.TARIFFS_CARDS_TWO).all()

    @allure.title("Нажать кнопку Подключить на тарифной карточке")
    def click_tariff_connect_button(self, card_index):
        try:
            self.page.locator(MainPageLocs.TARIFF_CONNECT_BUTTONS_TWO).nth(card_index).click()
        except Exception as e:
            raise AssertionError(
                f"Не удалось нажать кнопку 'Подключить' на карточке тарифа #{card_index} (домашний интернет).\n"
                "Возможно, элемент недоступен, перекрыт или изменился селектор."
                f"\nТехнические детали: {e}"
            )

    @allure.title("Отправить заявку на подключение тарифа")
    def send_tariff_connection_request(self):
        with allure.step("Заполнить попап и отправить заявку"):
            try:
                self.page.locator(ApplicationConnection.NAME_INPUT).fill("Тестимя")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести имя в попапе подключения тарифа (домашний интернет).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            try:
                self.page.locator(CheckConnectApplicationForms.TARIFF_PHONE_INPUT).fill("99999999999")
            except Exception as e:
                raise AssertionError(
                    "Не удалось ввести телефон в попапе подключения тарифа (домашний интернет).\n"
                    "Возможно, поле недоступно, скрыто или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            try:
                self.page.locator(ApplicationConnection.POPUP_SEND_BUTTON).click()
            except Exception as e:
                raise AssertionError(
                    "Не удалось отправить попап подключения тарифа (домашний интернет).\n"
                    "Возможно, кнопка недоступна, перекрыта или изменился селектор."
                    f"\nТехнические детали: {e}"
                )
            time.sleep(4)
