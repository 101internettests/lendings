class ThankYouPage:
    CRUSIFIX_CLOSE = "xpath=(//img)[3]"


class CheckConnectApplicationForms:
    FIRST_CITY = "xpath=(//input[@placeholder='Город'])[1]"
    FIRST_ADDRESS = "xpath=(//input[@placeholder='Адрес'])[1]"
    FIRST_PHONE_INPUT = "xpath=(//input[@name='Phone'])[1]"
    FIRST_CHECK_ADDRESS_BUTTON = "xpath=(//input[@value='Проверить адрес'])[2]"

    TARIFF_CITY = "xpath=(//input[@placeholder='Город'])[2]"
    TARIFF_ADDRESS = "xpath=(//input[@placeholder='Адрес'])[2]"
    TARIFF_PHONE_INPUT = "xpath=(//input[@name='Phone'])[2]"
    TARIFF_CHECK_ADDRESS_BUTTON = "xpath=(//input[@value='Проверить адрес'])[4]"

    SECOND_CITY = "xpath=(//input[@placeholder='Город'])[3]"
    SECOND_ADDRESS = "xpath=(//input[@placeholder='Адрес'])[3]"
    SECOND_PHONE_INPUT = "xpath=(//input[@name='Phone'])[3]"
    SECOND_CHECK_ADDRESS_BUTTON = "xpath=(//input[@value='Проверить адрес'])[6]"

    POPUP_SEND_BUTTON = "xpath=(//input[@value='Отправить'])[2]"

    HOME_MEGA_CITY = "xpath=//input[@placeholder='Адрес (город, улица, дом, кв)*']"

class ClarifyPopUp:
    CLARIFY_BUTTON = "xpath=(//button[@id='btnup'])[2]"


class MainPageLocs:
    TARIFFS_CARDS = "xpath=//div[@class='card-new__wrapper-bottom']"
    TARIFFS_CARDS_TWO = "xpath=//div[@class='uc-BLOCK-INTERNET']//div[@class='card__container']"
    TARIFF_CONNECT_BUTTONS = "xpath=//div[@class='card-new__wrapper-bottom']//button[contains(text(),'Подключить')]"
    TARIFF_CONNECT_BUTTONS_TWO = "xpath=//div[@class='uc-BLOCK-INTERNET']//div[@class='card__container']//div[@style='display: block;']"
    HEADER_LINKS = {
        "home_internet": "xpath=(//a[contains(text(),'Домашний интернет')])[1]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет и ТВ')])[1]",
        "family_tariffs": "xpath=(//a[contains(text(),'Тарифы для семьи')])[1]"
    }

    # Ссылки в футере
    FOOTER_LINKS = {
        "home_internet": "xpath=(//a[contains(text(),'Домашний интернет')])[2]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет и ТВ')])[2]",
        "family_tariffs": "xpath=(//a[contains(text(),'Тарифы для семьи')])[2]"
    }
    POPUP_LINKS = {
        "cookie_policy": "xpath=//a[contains(text(),'Политики обработки файлов cookie')]",
        "privacy_policy": "xpath=//a[contains(text(),'Политику конфиденциальности')]"
    }
    BUTTON_DONT_FIND_BUTTON = "xpath=//button[@class='region-search__button button button-green']"


class ApplicationConnection:
    NAME_INPUT = "xpath=//input[@name='Name']"
    POPUP_SEND_BUTTON = "xpath=(//input[@value='Отправить'])[1]"
