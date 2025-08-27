class BeelineMain:
    SEND_BUTTON = "xpath=//input[@value='Отправить']"
    COOKIES_CLOSE = "xpath=//div[@id='cookieButton']"
    CONNECT_BUTTON = "xpath=(//button[contains(text(),'Подключиться')])[2]"
    CONNECT_BUTTON_FUTER = "xpath=(//button[contains(text(),'Подключиться')])[3]"
    INPUT_STREET = "xpath=(//input[@placeholder='Улица'])[1]"
    INPUT_STREET_FIVE = "xpath=(//input[@placeholder='Улица'])[5]"
    INPUT_HOUSE = "xpath=(//input[@placeholder='Дом'])[1]"
    INPUT_HOUSE_FIVE = "xpath=(//input[@placeholder='Дом'])[5]"
    INPUT_STREET_SECOND = "xpath=(//input[@placeholder='Улица'])[2]"
    INPUT_HOUSE_SECOND = "xpath=(//input[@placeholder='Дом'])[2]"
    PHONE_INPUT_FIRST = "xpath=(//input[@name='Phone'])[1]"
    PHONE_INPUT_SECOND = "xpath=(//input[@name='Phone'])[2]"
    PHONE_INPUT_OTHER = "xpath=(//input[@name='Phone'])[3]"
    PHONE_INPUT_FIVE = "xpath=(//input[@name='Phone'])[5]"
    INPUT_CONNECT = "xpath=(//input[@value='Подключить'])[1]"
    INPUT_ADDRES = "xpath=(//input[@placeholder='Адрес'])[1]"
    INPUT_ADDRES_TWO = "xpath=(//input[@placeholder='Адрес'])[2]"
    CHECK_ADDRESS = "xpath=(//input[@value='Проверить адрес'])[1]"
    CHECK_ADDRESS_TWO = "xpath=(//input[@value='Проверить адрес'])[2]"
    CHECK_ADDRESS_THREE = "xpath=(//input[@value='Проверить адрес'])[3]"
    CHECK_ADDRESS_FOUR = "xpath=(//input[@value='Проверить адрес'])[4]"
    TARIFF_CARDS = "xpath=(//div[@itemtype='http://schema.org/Product'])"
    TARIFF_CARDS_SECOND = "xpath=(//div[@id='tariffs']//div[@itemtype='http://schema.org/Product'])"
    TARIFF_BUTTON = "xpath=(//button[text()='Подключить'])"
    TARIFF_NAMES = "xpath=(//div[@id='tariffs']//div[@itemprop='name'])"
    POPUP_TARIFF_NAME = "xpath=(//div[@class='popup__title popup-new__title'])[1]"
    POPUP_NAME = "xpath=(//div[@class='popup__title popup-new__title'])"
    HEADER_LINKS = {
        "home_internet": "xpath=(//a[contains(text(),'Домашний интернет')])[1]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет + ТВ')])[1]",
        "family_tariffs": "xpath=(//a[contains(text(),'Семейные тарифы')])[1]",
        "business": "xpath=(//a[contains(text(),'Бизнесу')])[1]"
    }
    HEADER_LINKS_SECOND = {
        "home_internet": "xpath=(//a[contains(text(),'Домашний интернет')])[1]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет + ТВ')])[1]",
        "family_tariffs": "xpath=(//a[contains(text(),'Семейные тарифы')])[1]",
        "all_tariffs": "xpath=(//a[contains(text(),'Все тарифы')])[1]",
        "business": "xpath=(//a[contains(text(),'Бизнесу')])[1]"
    }
    HEADER_LINKS_THIRD = {
        "home_internet": "xpath=(//a[contains(text(),'домашний интернет')])[1]",
        "internet_tv": "xpath=(//a[contains(text(),'интернет и ТВ')])[1]",
        "for_you_and_house": "xpath=(//a[contains(text(),'для тебя и дома')])[1]",
        "business": "xpath=(//a[contains(text(),'бизнесу')])[1]"
    }
    HEADER_LINKS_FOUR = {
        "home_internet": "xpath=(//a[contains(text(),'Домашний интернет')])[1]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет и ТВ')])[1]",
        "three_in_one": "xpath=(//a[contains(text(),'Тарифы 3 в 1')])[1]",
        "business": "xpath=(//a[contains(text(),'Бизнесу')])[1]"
    }
    HEADER_LINKS_PRO = {
        "home_internet": "xpath=(//a[contains(text(),'домашний интернет')])[1]",
        "internet_tv": "xpath=(//a[contains(text(),'интернет и ТВ')])[1]",
        "for_you_and_home": "xpath=(//a[contains(text(),'для тебя и дома')])[1]"
    }
    HEADER_LINKS_TELE = {
        "tariffs": "xpath=(//a[text()='Тарифы'])[1]",
        "news": "xpath=(//a[text()='Новости'])[1]",
        "check_the_address": "xpath=(//a[text()='Проверить адрес'])[1]"
    }
    # Ссылки в футере
    FOOTER_LINKS = {
        "home_internet": "xpath=(//a[contains(text(),'Домашний интернет')])[2]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет и Телевидение')])[1]",
        "family_tariffs": "xpath=(//a[contains(text(),'Семейные тарифы')])[2]",
        "business": "xpath=(//a[contains(text(),'Бизнесу')])[2]"
    }
    FOOTER_LINKS_SECOND = {
        "home_internet": "xpath=(//a[contains(text(),'Домашний интернет')])[2]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет и Телевидение')])[1]",
        "family_tariffs": "xpath=(//a[contains(text(),'Семейные тарифы')])[2]",
        "all_tariffs": "xpath=(//a[contains(text(),'Все тарифы')])[2]",
        "business": "xpath=(//a[contains(text(),'Бизнесу')])[2]"
    }
    FOOTER_LINKS_THIRD = {
        "home_internet": "xpath=(//a[contains(text(),'домашний интернет')])[2]",
        "internet_tv": "xpath=(//a[contains(text(),'интернет + телевидение')])[1]",
        "family_tariffs": "xpath=(//a[contains(text(),'тарифы для семьи')])[1]"
    }
    FOOTER_LINKS_FOUR = {
        "home_internet": "xpath=(//a[contains(text(),'Домашний интернет')])[2]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет и ТВ')])[1]",
        "three_in_one": "xpath=(//a[contains(text(),'Тарифы 3 в 1')])[2]"
    }
    FUTER_LINKS_TELE = {
        "tariffs": "xpath=(//a[text()='Тарифы'])[2]",
        "check_the_address": "xpath=(//a[text()='Проверить адрес'])[2]",
        "help": "xpath=(//a[text()='Помощь'])[1]"
    }

    OTHER_HEADERS = {
        "return_bonuses": "xpath=//a[contains(text(),'Вернём бонусы на счёт за покупку бронзового номера')]",
        "make_meaningful": "xpath=//a[contains(text(),'	Совершайте важные операции в приложениях банков даже при нуле на счёте')]",
        "beeline_tv": "xpath=//a[contains(text(),'билайн ТВ дарит фильмы, сериалы и телеканалы на 30 дней!')]",

    }
    FOOTER_LINKS_SEC = {
        "privacy_policy": "xpath=(//a[contains(text(),'cookies')])[1]"
    }


class OnlineBeeline:
    CHOOSE_YOUR_CITY_HEADER = "xpath=//p[text()=' Уточните ваш город']"
    CHOOSE_YOUR_CITY_BUTTON =  "xpath=//button[text()='Выбрать город']"
    CLOSE_CITY_POPUP = "xpath=(//button[@class='popup__close'])[2]"
    FILL_THE_ADDRESS = "xpath=(//input[@placeholder='введите адрес'])[1]"
    FILL_THE_ADDRESS_SECOND = "xpath=(//input[@placeholder='введите адрес'])[2]"
    BUTTON_FIND_TARIFFS ="xpath=(//input[@value='найти тарифы'])[1]"
    BUTTON_FIND_TARIFFS_SECOND = "xpath=(//input[@value='найти тарифы'])[2]"
    CONNECT_BUTTON_FUTER = "xpath=(//button[contains(text(),'подключиться')])[2]"
    CONNECT_BUTTON_FUTER_FR = "xpath=(//button[contains(text(),'подключиться')])[1]"
    CONNECT_BUTTON_FUTER_TH = "xpath=(//button[contains(text(),'подключиться')])[3]"
    BUTTON_FAST_CONNECTION  = "xpath=//button[contains(text(),'быстрое подключение')]"
    BUTTON_DONT_CITY = "xpath=//button[@class='region-search__button button button-yellow']"
    CITY_INPUT = "xpath=//input[@placeholder='Город']"
    STREET_HOME_INPUT = "xpath=//input[@placeholder='Улица, дом']"
    CONNECT_BANNER = "xpath=(//a[@id='btnup'])[1]"
    GET_CONSULTATION = "xpath=(//button[@id='btnup'])[3]"
    TARIFF_BUTTON = "xpath=(//button[text()='подключить'])"
    TARIFF_BUTTON_NEW = "xpath=(//button[text()='подключить'])"


class OnlineBeelineNew:
    ADRESS_INPUT = "xpath=(//input[@placeholder='Адрес'])[1]"
    STREET_INPUT = "xpath=(//input[@placeholder='Улица'])[1]"
    STREET_INPUT_SECOND = "xpath=(//input[@placeholder='Улица'])[2]"
    FIRST_CHOICE = "xpath=(//div[@class='autocomplete-item'])[1]"
    HOUSE_INPUT = "xpath=(//input[@placeholder='Дом'])[1]"
    HOUSE_INPUT_SECOND = "xpath=(//input[@placeholder='Дом'])[2]"
    PHONE_BUTTON = "xpath=(//input[@placeholder='+7(999)-999-99-99'])[1]"
    PHONE_BUTTON_SECOND = "xpath=(//input[@placeholder='+7(999)-999-99-99'])[2]"
    PHONE_BUTTON_THREE = "xpath=(//input[@placeholder='+7(999)-999-99-99'])[3]"
    SEND_BUTTON_CONNECT_FIRST = "xpath=(//input[@value='Проверить адрес'])[1]"
    SEND_BUTTON_CONNECT = "xpath=(//input[@value='Проверить адрес'])[2]"
    SEND_BUTTON_CONNECT_ONE = "xpath=(//input[@value='Проверить адрес'])[3]"