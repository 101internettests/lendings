class MTSHomeOnlineSecondMain:
    SUPER_OFFER_HEADER = "xpath=(//div[contains(text(),'Выгодное спецпредложение!')])[1]"
    SUPER_OFFER_TEXT = "xpath=(//div[contains(text(),'С экономией в год от 9000 рублей!')])[1]"
    INPUT_OFFER_POPUP = "xpath=(//input[@name='Phone'])[6]"
    CONNECT_BUTTON = "xpath=(//button[contains(text(),'Подключить')])[2]"
    CHECK_ADDRESS_BUTTON_FUTER = "xpath=(//button[contains(text(),'Проверить адрес')])[2]"
    ADDRESS_INPUT = "xpath=(//input[@placeholder='Адрес'])[6]"


class ApplicationPopupWithNameS:
    NAME_INPUT = "xpath=(//input[@name='Name'])[1]"
    PHONE_INPUT = "xpath=(//input[@name='Phone'])[5]"
    SEND_BUTTON = "xpath=(//input[@value='Отправить'])[1]"


class FormApplicationCheckConnectionSecond:
    PHONE_INPUT_SECOND = "xpath=(//input[@name='Phone'])[3]"


class ApplicationPopupCheckConnectionSecond:
    ADDRESS_INPUT_SECOND = "xpath=(//input[@placeholder='Адрес'])[3]"
    ADDRESS_INPUT_FOUR = "xpath=(//input[@placeholder='Адрес'])[4]"
    PHONE_INPUT_SECOND = "xpath=(//input[@name='Phone'])[4]"
    CHECK_ADDRESS_BUTTON = "xpath=(//input[@value='Проверить адрес'])[3]"
# Ссылки в хедере
    HEADER_LINKS = {
        "home_internet": "xpath=(//a[contains(text(),'Тарифы с домашним интернетом')])[2]",
        "mobile": "xpath=(//a[contains(text(),'Мобильная связь')])[2]",
        "business": "xpath=(//a[contains(text(),'Бизнесу')])[2]"
    }
    FOOTER_LINKS = {
        "cookie_policy": "xpath=//a[contains(text(),'Политики обработки файлов cookie')]"
    }


class RegionChoiceSecond:
    REGION_CHOICE_BUTTON_FUTER = "xpath=(//a[@id='city'])[3]"
    PHONE_INPUT = "xpath=(//input[@name='Phone'])[3]"
    SEND_BUTTON = "xpath=(//input[@value='Отправить'])[2]"
    NEW_HEADER_BUTTON = "xpath=(//span[@id='city'])[2]"
    NEW_FUTER_BUTTON = "xpath=(//span[@id='city'])[3]"