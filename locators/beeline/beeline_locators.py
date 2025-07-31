class BeelineMain:
    SEND_BUTTON = "xpath=//input[@value='Отправить']"
    COOKIES_CLOSE = "xpath=//div[@id='cookieButton']"
    CONNECT_BUTTON = "xpath=(//button[contains(text(),'Подключиться')])[2]"
    CONNECT_BUTTON_FUTER = "xpath=(//button[contains(text(),'Подключиться')])[3]"
    INPUT_STREET = "xpath=(//input[@placeholder='Улица'])[1]"
    INPUT_HOUSE = "xpath=(//input[@placeholder='Дом'])[1]"
    PHONE_INPUT_FIRST = "xpath=(//input[@name='Phone'])[1]"
    PHONE_INPUT_SECOND = "xpath=(//input[@name='Phone'])[2]"
    PHONE_INPUT_OTHER = "xpath=(//input[@name='Phone'])[3]"
    INPUT_CONNECT = "xpath=(//input[@value='Подключить'])[1]"
    INPUT_ADDRES = "xpath=(//input[@placeholder='Адрес'])[1]"
    INPUT_ADDRES_TWO = "xpath=(//input[@placeholder='Адрес'])[2]"
    CHECK_ADDRESS = "xpath=(//input[@value='Проверить адрес'])[1]"
    CHECK_ADDRESS_TWO = "xpath=(//input[@value='Проверить адрес'])[2]"
    TARIFF_CARDS = "xpath=(//div[@itemtype='http://schema.org/Product'])"
    TARIFF_BUTTON = "xpath=(//button[text()='Подключить'])"
    TARIFF_NAMES = "xpath=(//div[@id='tariffs']//div[@itemprop='name'])"
    POPUP_TARIFF_NAME = "xpath=(//div[@class='popup__title popup-new__title'])[1]"
    HEADER_LINKS = {
        "home_internet": "xpath=(//a[contains(text(),'Домашний интернет')])[1]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет + ТВ')])[1]",
        "family_tariffs": "xpath=(//a[contains(text(),'Семейные тарифы')])[1]",
        "business": "xpath=(//a[contains(text(),'Бизнесу')])[1]"
    }

    # Ссылки в футере
    FOOTER_LINKS = {
        "home_internet": "xpath=(//a[contains(text(),'Домашний интернет')])[2]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет + ТВ')])[2]",
        "family_tariffs": "xpath=(//a[contains(text(),'Семейные тарифы')])[2]",
        "business": "xpath=(//a[contains(text(),'Бизнесу')])[2]"
    }

    OTHER_HEADERS = {
        "return_bonuses": "xpath=//a[contains(text(),'Вернём бонусы на счёт за покупку бронзового номера')]",
        "make_meaningful": "xpath=//a[contains(text(),'	Совершайте важные операции в приложениях банков даже при нуле на счёте')]",
        "beeline_tv": "xpath=//a[contains(text(),'билайн ТВ дарит фильмы, сериалы и телеканалы на 30 дней!')]",

    }
    FOOTER_LINKS_SEC = {
        "privacy_policy": "xpath=(//a[contains(text(),'cookies')])[1]"
    }