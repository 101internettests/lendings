class Rostelecom:
    CONNECT_PURPLE_BUTTON = "xpath=//button[@class='button-lead-catcher']"
    PHONE_BUTTON_FIRST = "xpath=(//input[@name='Phone'])[1]"
    PHONE_BUTTON_SECOND = "xpath=(//input[@name='Phone'])[2]"
    PHONE_BUTTON_THREE = "xpath=(//input[@name='Phone'])[3]"
    PHONE_BUTTON_FOUR = "xpath=(//input[@name='Phone'])[4]"
    PHONE_BUTTON = "xpath=(//input[@name='Phone'])[5]"
    SEND_BUTTON_CONNECT = "xpath=(//input[@value='Отправить'])[1]"
    SEND_BUTTON_OFFER_POPUP = "xpath=(//input[@value='Отправить'])[3]"
    STREET_INPUT = "xpath=(//input[@placeholder='Улица'])[3]"
    STREET_INPUT_FIRST = "xpath=(//input[@placeholder='Улица'])[1]"
    STREET_INPUT_SECOND = "xpath=(//input[@placeholder='Улица'])[2]"
    STREET_INPUT_FOUR = "xpath=(//input[@placeholder='Улица'])[4]"
    INPUT_STREET_FIVE = "xpath=(//input[@placeholder='Улица'])[5]"
    FIRST_STREET = "xpath=(//div[@class='autocomplete-street'])[1]"
    HOUSE_INPUT_FIRST = "xpath=(//input[@placeholder='Дом'])[1]"
    HOUSE_INPUT_SECOND = "xpath=(//input[@placeholder='Дом'])[2]"
    HOUSE_INPUT_FOUR = "xpath=(//input[@placeholder='Дом'])[4]"
    HOUSE_INPUT = "xpath=(//input[@placeholder='Дом'])[3]"
    INPUT_HOUSE_FIVE = "xpath=(//input[@placeholder='Дом'])[5]"
    FIRST_HOUSE = "xpath=(//div[@class='autocomplete-item'])[1]"
    CONNECTION_BUTTON = "xpath=(//button[@id='btnup'])[3]"
    CONNECTION_BUTTON_MIDDLE = "xpath=(//button[@id='btnup'])[4]"
    CHECK_THE_ADDRESS_BUTTON = "xpath=(//input[@value='Проверить адрес'])[1]"
    CHECK_THE_ADDRESS_BUTTON_SECOND = "xpath=(//input[@value='Проверить адрес'])[2]"
    TARIFF_CARDS = "xpath=(//div[@id='sale'])"
    TARIFF_CONNECT_BUTTONS = "xpath=//div[@class='card__container']//button"
    TARIFF_NAMES = "xpath=(//h4)"
    POPUP_TARIFF_NAME = "xpath=(//div[@class='popup__title'])[2]"
    NAME_INPUT = "xpath=//input[@name='Name']"
    SEND_BUTTON_SECOND = "xpath=(//input[@value='Отправить'])[2]"
    HEADER_LINKS = {
        "home_imternet": "xpath=(//a[contains(text(),'Домашний интернет')])[1]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет  ТВ')])[1]",
        "all_in_one": "xpath=(//a[contains(text(),'Все в одном')])[1]",
        "all_tariffs": "xpath=(//a[contains(text(),'Все тарифы')])[1]",
        "for_business": "xpath=(//a[contains(text(),'Бизнесу')])[1]",
    }
    FOOTER_LINKS = {
        "home_imternet": "xpath=(//a[contains(text(),'Домашний интернет')])[3]",
        "internet_tv": "xpath=(//a[contains(text(),'Интернет Телевидение')])[1]",
        "family_tariffs": "xpath=(//a[contains(text(),'Тарифы для семьи')])[1]",
        "all_tariffs": "xpath=(//a[contains(text(),'Все тарифы')])[3]",
        "bonuses": "xpath=(//a[contains(text(),'Бонусы')])[1]",
        "for_business": "xpath=(//a[contains(text(),'Бизнесу')])[3]",
    }
    FOOTER_LINKS_SECOND = {
        "news": "xpath=(//a[contains(text(),'Новости')])[1]",
        "check_address": "xpath=(//a[contains(text(),'Проверить адрес подключения')])[1]",
        "map": "xpath=(//a[contains(text(),'Карта сайта')])[1]",
        "policy": "xpath=(//a[contains(text(),'Политика обработки cookie')])[1]",
        "abonent": "xpath=(//a[contains(text(),'Как стать абонентом Ростелеком')])[1]",
        "feedback": "xpath=(//a[contains(text(),'Форма обратной связи')])[1]",
        "help": "xpath=(//a[contains(text(),'Помощь')])[1]",
        "applience": "xpath=(//a[contains(text(),'Оборудование')])[1]",
    }
    REGION_CHOICE_BUTTON_FUTER = "xpath=()"