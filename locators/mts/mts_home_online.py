class MTSHomeOnlineMain:
    SUPER_OFFER_HEADER = "xpath=//div[contains(text(),'Выгодное спецпредложение!')]"
    SUPER_OFFER_TEXT = "xpath=//div[contains(text(),'С экономией в год от 9000 рублей!')]"
    INPUT_OFFER_POPUP = "xpath=(//input[@name='Phone'])[5]"
    SEND_BUTTON_OFFER_POPUP = "xpath=(//form[@aria-label='Контактная форма']//input[@value='Отправить'])[2]"
    THANKYOU_TEXT = "xpath=//div[@class='thanks']"
    RED_BUTTON = "xpath=//button[@class='button-lead-catcher']"
    CLOSE_BUTTON = "xpath=//a[@class='thanks__close']//img[@alt='Вектор закрытия']"
    CONNECT_BUTTON = "xpath=(//button[contains(text(),'Подключить')])[1]"
    CHECK_ADDRESS_BUTTON = "xpath=(//button[contains(text(),'Проверить адрес')])[1]"
    BANNER = "xpath=//div[@class='banner button-application']"
    # Тарифные карточки
    TARIFF_CARDS = "xpath=//div[contains(@class, 'tariff-card')]"
    TARIFF_NAMES = "xpath=//div[contains(@class, 'tariff-card')]//div[contains(@class, 'tariff-name')]"
    TARIFF_CONNECT_BUTTONS = "xpath=//div[contains(@class, 'tariff-card')]//button[contains(text(), 'Подключить')]"
    POPUP_TARIFF_NAME = "xpath=//div[contains(@class, 'popup-title')]//span[@class='tariff-name']"

# попап по кнопке подключить Заявка на подключение
class ApplicationPopupWithName:
    NAME_INPUT = "xpath=//input[@name='Name']"
    PHONE_INPUT = "xpath=(//input[@name='Phone'])[4]"
    SEND_BUTTON = "xpath=(//input[@value='Отправить'])[1]"


# попап по кнопке подключить Проверить адрес
class ApplicationPopupCheckConnection:
    ADDRESS_INPUT = "xpath=(//input[@placeholder='Адрес'])[3]"
    PHONE_INPUT = "xpath=(//input[@name='Phone'])[3]"
    CHECK_ADDRESS_BUTTON = "xpath=(//input[@value='Проверить адрес'])[3]"


class FormApplicationCheckConnection:
    ADDRESS = "xpath=(//input[@placeholder='Адрес'])[1]"
    PHONE_INPUT = "xpath=(//input[@name='Phone'])[1]"
    CHECK_ADDRESS_BUTTON = "xpath=(//input[@value='Проверить адрес'])[1]"
    ADDRESS_SECOND = "xpath=(//input[@placeholder='Адрес'])[2]"
    PHONE_INPUT_SECOND = "xpath=(//input[@name='Phone'])[2]"
    CHECK_ADDRESS_BUTTON_SECOND = "xpath=(//input[@value='Проверить адрес'])[2]"


