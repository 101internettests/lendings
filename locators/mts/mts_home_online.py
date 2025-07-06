class MTSHomeOnlineMain:
    SUPER_OFFER_HEADER = "xpath=//div[contains(text(),'Выгодное спецпредложение!')]"
    SUPER_OFFER_CLOSE = "xpath=(//button[@class='popup__close'])[4]"
    SUPER_OFFER_TEXT = "xpath=//div[contains(text(),'С экономией в год от 9000 рублей!')]"
    INPUT_OFFER_POPUP_SOME_PAGE = "xpath=(//input[@name='Phone'])[4]"
    INPUT_OFFER_POPUP = "xpath=(//input[@name='Phone'])[5]"
    SEND_BUTTON_OFFER_POPUP = "xpath=(//form[@aria-label='Контактная форма']//input[@value='Отправить'])[2]"
    THANKYOU_TEXT = "xpath=//div[@class='thanks']"
    RED_BUTTON = "xpath=//button[@class='button-lead-catcher']"
    CLOSE_BUTTON = "xpath=//a[@class='thanks__close']//img[@alt='Вектор закрытия']"
    CLOSE_BUTTON_SECOND = "xpath=(//button[@class='popup__close'])[4]"
    CONNECT_BUTTON = "xpath=(//button[contains(text(),'Подключить')])[1]"
    CONNECT_BUTTON_FUTER = "xpath=//div[@class='footer__block']//button[contains(text(),'Подключить')]"
    CHECK_ADDRESS_BUTTON = "xpath=(//button[contains(text(),'Проверить адрес')])[1]"
    CHECK_ADDRESS_BUTTON_FUTER = "xpath=(//button[contains(text(),'Проверить адрес')])[3]"
    BANNER = "xpath=//div[@class='banner button-application']"
    # Тарифные карточки
    TARIFF_CARDS = "xpath=//div[@class='konvergent-one__cards']//div[@id='sale']"
    TARIFF_NAMES = "xpath=//h3[contains(text(),'')]"
    TARIFF_CONNECT_BUTTONS = "xpath=//button[@class='button button-red card-one__button  button-application']"
    POPUP_TARIFF_NAME = "xpath=(//div[@class='popup__wrapper']//div[contains(text(),'')])[1]"

    # Ссылки в хедере
    HEADER_LINKS = {
        "home_internet": "xpath=(//a[contains(text(),'Домашний интернет')])[2]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет + ТВ')])[2]",
        "internet_tv_mobile": "xpath=(//a[contains(text(),'Интернет, ТВ и мобильная связь')])[2]",
        "family_tariffs": "xpath=(//a[contains(text(),'Семейные тарифы')])[2]",
        "mobile": "xpath=(//a[contains(text(),'Мобильная связь')])[2]"
    }

    # Ссылки в футере
    FOOTER_LINKS = {
        "cookie_policy": "xpath=//a[contains(text(),'Политики обработки файлов cookie')]",
        "privacy_policy": "xpath=//a[contains(text(),'Политику конфиденциальности')]"
    }

    # Ссылки в форме
    FORM_LINKS = {
        "terms_and_conditions": "xpath=//h1[contains(text(),'Политика в отношении обработки персональных данных Россия')]"
    }


# попап по кнопке подключить Заявка на подключение
class ApplicationPopupWithName:
    NAME_INPUT = "xpath=//input[@name='Name']"
    PHONE_INPUT_ANOTHER = "xpath=(//input[@name='Phone'])[2]"
    PHONE_INPUT_OTHER = "xpath=(//input[@name='Phone'])[3]"
    PHONE_INPUT = "xpath=(//input[@name='Phone'])[4]"
    SEND_BUTTON = "xpath=(//input[@value='Отправить'])[1]"


# попап по кнопке подключить Проверить адрес
class ApplicationPopupCheckConnection:
    ADDRESS_INPUT_SECOND = "xpath=(//input[@placeholder='Адрес'])[2]"
    ADDRESS_INPUT = "xpath=(//input[@placeholder='Адрес'])[3]"
    NAME_INPUT = "xpath=(//input[@placeholder='Имя'])[1]"
    PHONE_INPUT_SECOND = "xpath=(//input[@name='Phone'])[2]"
    PHONE_INPUT = "xpath=(//input[@name='Phone'])[3]"
    CHECK_ADDRESS_BUTTON_SECOND = "xpath=(//input[@value='Проверить адрес'])[2]"
    CHECK_ADDRESS_BUTTON = "xpath=(//input[@value='Проверить адрес'])[3]"


class FormApplicationCheckConnection:
    ADDRESS = "xpath=(//input[@placeholder='Адрес'])[1]"
    PHONE_INPUT = "xpath=(//input[@name='Phone'])[1]"
    CHECK_ADDRESS_BUTTON = "xpath=(//input[@value='Проверить адрес'])[1]"
    ADDRESS_SECOND = "xpath=(//input[@placeholder='Адрес'])[2]"
    PHONE_INPUT_SECOND = "xpath=(//input[@name='Phone'])[2]"
    CHECK_ADDRESS_BUTTON_SECOND = "xpath=(//input[@value='Проверить адрес'])[2]"


class RegionChoice:
    REGION_CHOICE_BUTTON = "xpath=(//a[@id='city'])[1]"
    REGION_CHOICE_BUTTON_FUTER = "xpath=(//a[@id='city'])[2]"
    REGION_CHOICE_BUTTON_THREE = "xpath=(//a[@id='city'])[3]"
    CITY_INPUT = "xpath=//input[@placeholder='Введите название города']"
    FIRST_CHOICE = "xpath=(//a[@class='region_item'])[1]"
    ALL_CHOICES = "xpath=//a[@class='region_item']"
    BUTTON_DONT_CITY = "xpath=//button[@class='region-search__button button button-red']"
    FORM_CITY = "xpath=//input[@placeholder='Город']"


class MskMtsMainWeb:
    BANNER = "xpath=//div[@class='banner  button-application']"
    REGION_CHOICE_BUTTON = "xpath=(//a[@href='/city'])[3]"
    # Ссылки в хедере
    HEADER_LINKS = {
        "home_internet": "xpath=(//a[contains(text(),'Домашний интернет')])[2]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет + ТВ')])[2]",
        "internet_tv_mobile": "xpath=(//a[contains(text(),'Интернет, ТВ и мобильная связь')])[2]",
        "mobile": "xpath=(//a[contains(text(),'Мобильная связь')])[2]",
        "all_tariffs": "xpath=(//a[contains(text(),'Все тарифы')])[2]",
    }
    SUPER_OFFER_HEADER = "xpath=(//div[contains(text(),'Выгодное спецпредложение!')])[1]"
    SUPER_OFFER_TEXT = "xpath=(//div[contains(text(),'С экономией в год от 9000 рублей!')])[1]"
    INPUT_OFFER_POPUP = "xpath=(//input[@name='Phone'])[6]"
    CONNECT_BUTTON = "xpath=(//button[contains(text(),'Подключить')])[2]"
    PHONE_INPUT_OTHER = "xpath=(//input[@name='Phone'])[5]"
    CHECK_ADDRESS_BUTTON = "xpath=(//input[@value='Проверить адрес'])[1]"
    CHECK_ADDRESS_BUTTON_FUTER = "xpath=(//button[contains(text(),'Проверить адрес')])[2]"
    ADDRESS_SECOND = "xpath=(//input[@placeholder='Адрес'])[3]"
    PHONE_INPUT = "xpath=(//input[@name='Phone'])[4]"
    CHECK_ADDRESS_BUTTON_SECOND = "xpath=(//input[@value='Проверить адрес'])[3]"
    HEADER_LINKS_GPON = {
        "home_internet": "xpath=(//a[contains(text(),'Тарифы с домашним интернетом')])[2]",
        "mobile": "xpath=(//a[contains(text(),'Мобильная связь')])[2]"
    }
    REGION_CHOICE_BUTTON_SECOND = "xpath=(//a[@id='city'])[2]"
    REGION_CHOICE_BUTTON_FUTER = "xpath=(//a[@href='/city'])[5]"
    SUPER_OFFER_CLOSE = "xpath=(//button[@class='popup__close'])[3]"
    SUPER_OFFER_CLOSE_NEW = "xpath=(//button[@class='popup__close'])[4]"


class MtsThirdOnline:
    BUTTON_CONFIRM = "xpath=//button[@class=' button-red cookie-btn']"
    TARIFF_BUTTON = "xpath=(//button[@id='btnup'])[4]"
    MORE_INFO_BUTTON = "xpath=(//button[@id='btnup'])[3]"
    HEADER_LINKS = {
        "all_in_one": "xpath=(//a[contains(text(),'Всё в одном')])[1]",
        "mobile": "xpath=(//a[contains(text(),'Мобильная связь')])[1]"
    }
    FOOTER_LINKS = {
        "cookie_policy": "xpath=//a[contains(text(),'Политики обработки файлов cookie')]"
    }


class MtsRuLocators:
    ADDRESS_INPUT = "xpath=(//input[@placeholder='Адрес'])[1]"
    PHONE_INPUT = "xpath=(//input[@name='Phone'])[1]"
    SEND_BUTTON = "xpath=(//input[@value='Проверить адрес'])[1]"
    TARIFF_CONNECT_BUTTONS = "xpath=//div[@class='card-one__buttons']"
    TARIFF_CARDS = "xpath=//div[@class='konvergent-one__cards']//div[@id='sale']"