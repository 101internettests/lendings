class MTSHomeOnlineMain:
    SUPER_OFFER_HEADER = "xpath=//h3[contains(text(),'Выгодное спецпредложение!')]"
    SUPER_OFFER_HEADER_SECOND = "xpath=//div[contains(text(),'Выгодное спецпредложение!')]"
    CLOSE_MORE = "xpath=(//button[@class='popup__close'])[7]"
    CLOSE_MORE_SIX = "xpath=(//button[@class='popup__close'])[6]"
    SUPER_OFFER_CLOSE_NEW = "xpath=(//button[@class='popup__close'])[5]"
    SUPER_OFFER_CLOSE = "xpath=(//button[@class='popup__close'])[4]"
    SUPER_OFFER_CLOSE_MORE = "xpath=(//button[@class='popup__close'])[3]"
    SUPER_OFFER_CLOSE_HOME = "xpath=(//button[@class='popup__close'])[2]"
    SUPER_OFFER_CLOSE_MEGA = "xpath=(//button[@class='popup__close'])[1]"
    SUPER_OFFER_CLOSE_SECOND = "xpath=(//button[@class='popup__close'])[2]"
    SUPER_OFFER_TEXT = "xpath=//div[contains(text(),'С экономией в год от 9000 рублей!')]"
    INPUT_OFFER_POPUP_SECOND = "xpath=(//input[@name='Phone'])[2]"
    INPUT_OFFER_POPUP_SOME_PAGE = "xpath=(//input[@name='Phone'])[4]"
    INPUT_OFFER_POPUP = "xpath=(//input[@name='Phone'])[5]"
    INPUT_OFFER_POPUP_SIX = "xpath=(//input[@name='Phone'])[6]"
    INPUT_OFFER_POPUP_SEVEN = "xpath=(//input[@name='Phone'])[7]"
    SEND_BUTTON_OFFER_POPUP = "xpath=(//form[@aria-label='Контактная форма']//input[@value='Отправить'])[2]"
    THANKYOU_TEXT = "xpath=//div[@class='thanks']"
    THANKYOU_TEXT_SECOND = "xpath=//h1[text()='Заявка принята!']"
    THANKYOU_TEXT_MORE = "xpath=//p[text()=' Спасибо! Мы скоро с вами свяжемся!']"
    THANKYOU_HEADER = "xpath=//p[@class='thanks__text']"
    MORE_THANKYOU = "xpath=//h1[contains(@class,'thanks')]"
    RED_BUTTON = "xpath=//button[@class='button-lead-catcher']"
    CLOSE_BUTTON_NEW = "xpath=//a[@class='thanks__close']"
    CLOSE_BUTTON_MEGA = "xpath=//a[@class='back-link']"
    GO_TO_MAIN = "xpath=//a[text()='На главную']"
    CLOSE_BUTTON = "xpath=//a[@class='thanks__close']//img[@alt='Вектор закрытия']"
    THANKYOU_CLOSE = "xpath=//a[@class='page-thanks__close']"
    CLOSE_BUTTON_SECOND = "xpath=(//button[@class='popup__close'])[4]"
    CONNECT_BUTTON = "xpath=(//button[contains(text(),'Подключить')])[1]"
    CONNECTING_BUTTON = "xpath=(//button[contains(text(),'Подключиться')])[1]"
    CONNECT_BUTTON_CONDITIONS = "xpath=(//a[@id='btnup'])[1]"
    CONNECT_BUTTON_SECOND = "xpath=(//a[@id='btnup'])[2]"
    CONNECT_BUTTON_SECOND_CONNECT = "xpath=(//button[@id='btnup'])[2]"
    CONNECT_BUTTON_THIRD = "xpath=(//button[@id='btnup'])[3]"
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
    STREET_BUTTON = "xpath=(//input[@placeholder='Улица'])[4]"
    STREET_BUTTON_THREE = "xpath=(//input[@placeholder='Улица'])[3]"
    STREET_BUTTON_FIRST = "xpath=(//input[@placeholder='Улица'])[1]"
    STREET_BUTTON_SECOND = "xpath=(//input[@placeholder='Улица'])[2]"
    STREET_BUTTON_FIVE = "xpath=(//input[@placeholder='Улица'])[5]"
    HOUSE_BUTTON = "xpath=(//input[@placeholder='Дом'])[4]"
    HOUSE_BUTTON_FIRST = "xpath=(//input[@placeholder='Дом'])[1]"
    HOUSE_BUTTON_THREE = "xpath=(//input[@placeholder='Дом'])[3]"
    HOUSE_BUTTON_SECOND = "xpath=(//input[@placeholder='Дом'])[2]"
    HOUSE_BUTTON_FIVE = "xpath=(//input[@placeholder='Дом'])[5]"
    FIRST_STREET = "xpath=(//div[@class='autocomplete-street'])[1]"
    FIRST_HOUSE = "xpath=(//div[@class='autocomplete-item'])[1]"
    FIRST_HOUSE_SECOND = "xpath=(//div[@id='house-list']//div[@class='autocomplete-item'])[1]"
    SEND_BUTTON = "xpath=(//input[@value='Отправить'])[1]"
    SEND_BUTTON_TWO = "xpath=(//input[@value='Отправить'])[2]"
    ANOTHER_CITY_BUTTON = "xpath=//button[text()='Выбрать город']"
    CHECK_ADDRESS_BUTTON_SECOND = "xpath=(//input[@value='Проверить адрес'])[2]"
    CHECK_ADDRESS_BUTTON_THREE = "xpath=(//input[@value='Проверить адрес'])[3]"
    CHECK_ADDRESS_BUTTON_FOUR = "xpath=(//input[@value='Проверить адрес'])[4]"
    PHONE_INPUT_FIVE = "xpath=(//input[@name='Phone'])[5]"


# попап по кнопке подключить Заявка на подключение
class ApplicationPopupWithName:
    NAME_INPUT = "xpath=//input[@name='Name']"
    PHONE_INPUT_ANOTHER = "xpath=(//input[@name='Phone'])[2]"
    PHONE_INPUT_OTHER = "xpath=(//input[@name='Phone'])[3]"
    PHONE_INPUT = "xpath=(//input[@name='Phone'])[4]"
    SEND_BUTTON = "xpath=(//input[@value='Отправить'])[1]"
    ADDRESS_INPUT = "xpath=(//input[@placeholder='Адрес'])[4]"
    ADDRESS_INPUT_FIVE = "xpath=(//input[@placeholder='Адрес'])[5]"


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
    ADDRESS_THIRD = "xpath=(//input[@placeholder='Адрес'])[3]"
    PHONE_INPUT_SECOND = "xpath=(//input[@name='Phone'])[2]"
    CHECK_ADDRESS_BUTTON_SECOND = "xpath=(//input[@value='Проверить адрес'])[2]"


class RegionChoice:
    CITY_LOC = "xpath=(//a[@class='region_item region_link'])"
    RANSOM_CITY_BUTTON = "xpath=(//table[@class='city_list']//tbody//tr//td//a)"
    UPDATED_REGION_BUTTON = "xpath=//div[@class='header__wrapper-middle']//span[@id='city']"
    NEW_REGION_CHOICE_BUTTON = "xpath=(//span[@id='city'])[1]"
    NEW_REGION_CHOICE_BUTTON_MTS = "xpath=(//span[@id='city'])[2]"
    TELE_REGION_CHOICE_BUTTON = "xpath=(//a[@id='city'])[1]"
    HEADER_BUTTON_NEW = "xpath=(//span[@id='city'])[1]"
    NEW_REGION_CHOICE_BUTTON_HEADER = "xpath=(//span[@id='city'])[2]"
    NEW_REGION_CHOICE_BUTTON_FUTER = "xpath=(//span[@id='city'])[3]"
    REGION_CHOICE_BUTTON = "xpath=(//a[@id='city'])[1]"
    REGION_CHOICE_BUTTON_FUTER = "xpath=(//a[@id='city'])[2]"
    REGION_CHOICE_BUTTON_THREE = "xpath=(//a[@id='city'])[3]"
    FOOTER_BUTTON = "xpath=//div[@class='footer__city']//a"
    FOOTER_SECOND_TIME = "xpath=(//div[@class='footer__city']//span)[1]"
    FUTER_CHOICE = "xpath=(//span[@id='city'])[2]"
    FUTER_MTS_NEW = "xpath=(//a[@class='city'])[2]"
    CITY_INPUT = "xpath=//input[@placeholder='Введите название города']"
    NEW_CITY_INPUT = "xpath=//input[@id='city-input']"
    RTK_CITY_INPUT = "xpath=//input[@placeholder='Поиск города']"
    FIRST_CHOICE = "xpath=(//a[@class='region_item'])[1]"
    FIRST_CHOICE_RTK = "xpath=//div[@class='city-coverage__capital']//a"
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
        "mobile": "xpath=(//a[contains(text(),'Мобильная связь')])[2]",
        "business": "xpath=(//a[contains(text(),'Бизнесу')])[2]"
    }
    REGION_CHOICE_BUTTON_SECOND = "xpath=(//a[@id='city'])[2]"
    REGION_CHOICE_GPON = "xpath=(//a[@id='city'])[3]"
    REGION_CHOICE_BUTTON_FUTER = "xpath=(//a[@href='/city'])[5]"
    SUPER_OFFER_CLOSE = "xpath=(//button[@class='popup__close'])[3]"
    SUPER_OFFER_CLOSE_NEW = "xpath=(//button[@class='popup__close'])[4]"
    ADDRESS_FIVE = "xpath=(//input[@placeholder='Адрес'])[5]"


class MtsThirdOnline:
    BUTTON_CONFIRM = "xpath=//button[@class=' button-red cookie-btn']"
    TARIFF_BUTTON = "xpath=(//button[@id='btnup'])[4]"
    MORE_INFO_BUTTON = "xpath=(//button[@id='btnup'])[3]"
    HEADER_LINKS = {
        "all_in_one": "xpath=(//a[contains(text(),'Всё в одном')])[1]",
        "mobile": "xpath=(//a[contains(text(),'Мобильная связь')])[1]",
        "home": "xpath=(//a[contains(text(),'Домашний интернет')])[1]",
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