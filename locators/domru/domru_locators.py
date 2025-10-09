class LocationPopup:
        POPUP_HEADER = "xpath=//p[text()='Вы находитесь в Москве?']"
        YES_BUTTON = "xpath=//button[@id='yesButton']"
        NO_BUTTON = "xpath=//button[@id='noButton']"
        NEW_BUTTON_NO = "xpath=//button[@class='popup-select-region__button city']"
        NEW_BUTTON_NO_SECOND = "xpath=(//button[@class='popup-select-region__button city'])[1]"
        SEND_BUTTON_OFFER_POPUP = "xpath=(//form[@aria-label='Контактная форма']//input[@value='Отправить'])[2]"
        INPUT_OFFER_POPUP = "xpath=(//input[@name='Phone'])[7]"
        CLOSE_BUTTON = "xpath=//a[@class='thanks__close']//img"
        CLOSE_POPUP = "xpath=//button[@class='popup__close ']"
        TARIFF_CARDS = "xpath=//div[@id='sale']"
        TARIFF_CONNECT_BUTTONS = "xpath=//button[@class='button button-blue card__button  button-application']"
        # Ссылки в хедере
        HEADER_LINKS = {
                "internet": "xpath=(//a[contains(text(),'Интернет')])[1]",
                "internet_tv": "xpath=(//a[contains(text(),'Интернет + ТВ')])[1]"
        }

        # Ссылки в футере
        FOOTER_LINKS = {
                "privacy_policy": "xpath=//a[contains(text(),'условия обработки данных')]"
        }
        FOOTER_LINKS_SEC = {
                "privacy_policy": "xpath=(//a[contains(text(),'cookies')])[1]"
        }
        PDF_DOW = {
                "check_conection1": "xpath=(//a[contains(text(),'скачать PDF')])[1]",
                "check_conection2": "xpath = (//a[contains(text(),'скачать PDF')])[2]",
                "free_test_drive": "xpath = (//a[contains(text(),'скачать PDF')])[3]",
                "free_test_drive2": "xpath = (//a[contains(text(),'скачать PDF')])[4]",
                "free_test_drive_three": "xpath = (//a[contains(text(),'скачать PDF')])[5]",
                "free_test_drive_three2": "xpath = (//a[contains(text(),'скачать PDF')])[6]",
                "speed_int1": "xpath = (//a[contains(text(),'скачать PDF')])[7]",
                "speed_int2": "xpath = (//a[contains(text(),'скачать PDF')])[8]",
        }
        NAME_INPUT = "xpath=//input[@name='Name']"
        BUTTON_SEND = "xpath=(//input[@value='Отправить'])[1]"
        MAIN_LOGO = "xpath=//div[@class='header__logo']"
        MAIN_LOGO_BEELINE = "xpath=(//img[@alt='Логотип компании билайн'])[1]"


class PopUps:
        INPUT_NUM_POPUP = "xpath=(//input[@name='Phone'])[1]"
        INPUT_NUM_POPUP_SEC = "xpath=(//input[@name='Phone'])[2]"
        INPUT_NUM_POPUP_THR = "xpath=(//input[@name='Phone'])[3]"
        INPUT_NUM_POPUP_FOU = "xpath=(//input[@name='Phone'])[4]"
        INPUT_NUM_POPUP_FIV = "xpath=(//input[@name='Phone'])[5]"
        INPUT_NUM_POPUP_SIX = "xpath=(//input[@name='Phone'])[6]"
        BUTTON_NEW_INTERNET = "xpath=//input[@value='Хочу новый интернет']"
        BUTTON_CHECK_ADDRESS = "xpath=(//input[@value='Проверить адрес'])[2]"
        BUTTON_CONNECT = "xpath=(//input[@value='Подключить'])[1]"
        BUTTON_CONNECT_SEC = "xpath=(//input[@value='Подключить'])[2]"
        BUTTON_CONNECT_THI = "xpath=(//input[@value='Подключить'])[3]"
        INPUT_ADDRESS = "xpath=//input[@placeholder='Адрес (город, улица, дом, кв)*']"
        BUTTON_CONNECT_INTERNET = "xpath=(//button[@id='btnup'])[4]"
        BUTTON_CONNECT_INTERNET_SECOND = "xpath=(//button[@id='btnup'])[5]"
        BUTTON_CONNECT_INTERNET_THIRD = "xpath=(//button[@id='btnup'])[6]"


class CardsPopup:
        INPUT_NAME = "xpath=//input[@placeholder='Имя']"
        INPUT_NUM= "xpath=(//input[@name='Phone'])[6]"
        SEND_BUTTON = "xpath=(//input[@value='Отправить'])[1]"
