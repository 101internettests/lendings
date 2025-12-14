class Main:
    CLOSE = "xpath=(//button[@class='popup__close'])[4]"


class Profit:
    STREET = "xpath=(//input[contains(@class,'profit_address_street')])[1]"
    HOUSE = "xpath=(//input[contains(@class,'profit_address_house')])[1]"
    PHONE = "xpath=(//input[contains(@class,'profit_address_phone')])[1]"
    BUTTON_SEND = "xpath=(//input[contains(@class,'profit_address_button_send')])[1]"
    BUTTON_CHANGE_CITY = "xpath=(//span[contains(@class,'profit_address_button_change_city')])[1]"
    BUTTON_CHANGE_CITY_SEC = "xpath=(//div[contains(@class,'profit_address_button_change_city')])[1]"
    BUTTON_FOR_OPEN = "xpath=(//button[@class='button-lead-catcher'])[1]"
    COLORFUL_BUTTON = "xpath=//button[contains(@class,'profit_address_button')]"


class Connection:
    STREET_LAST = "xpath=(//input[contains(@class,'connection_address_street')])"
    HOUSE_LAST = "xpath=(//input[contains(@class,'connection_address_house')])"
    NAME_LAST = "xpath=(//input[contains(@class,'popup__name')])"
    PHONE_LAST = "xpath=(//input[contains(@class,'connection_address_phone')])"
    BUTTON_SEND_LAST = "xpath=(//input[contains(@class,'connection_address_button_send')])"
    STREET = "xpath=(//input[contains(@class,'connection_address_street')])[1]"
    HOUSE = "xpath=(//input[contains(@class,'connection_address_house')])[1]"
    PHONE = "xpath=(//input[contains(@class,'connection_address_phone')])[1]"
    BUTTON_SEND = "xpath=(//input[contains(@class,'connection_address_button_send')])[1]"
    BUTTON_CHANGE_CITY = "xpath=//div[contains(@class,'connection_address_button_change_city')]"
    BUTTON_CHANGE_CITY_SEC = "xpath=//span[contains(@class,'connection_address_button_change_city')]"
    CONNECT_BUTTON = "xpath=(//button[contains(@class,'connection_address_button')])"
    CARDS_BUTTONS = "xpath=(//button[contains(@class,'connection_address_card_button')])"


class Checkaddress:
    STREET = "xpath=//input[contains(@class,'checkaddress_address_street')]"
    HOUSE = "xpath=//input[contains(@class,'checkaddress_address_house')]"
    PHONE = "xpath=//input[contains(@class,'checkaddress_address_phone')]"
    BUTTON_SEND = "xpath=//input[contains(@class,'checkaddress_address_button_send')]"
    BUTTON_CHANGE_CITY = "xpath=//button[contains(@class,'checkaddress_address_button_change_city')]"
    CHECKADDRESS_BUTTON_POPUP = "xpath=(//button[contains(@class,'checkaddress_address_button')])"
    CHECKADDRESS_BLOCK = "xpath=(//div[contains(@class,'checkaddress-block')])"
    BUTTON_CHANGE_CITY_BLOCK = "xpath=//span[contains(@class,'checkaddress_address_button_change_city')]"


class Undecided:
    STREET = "xpath=//input[contains(@class,'undecided_address_street')]"
    HOUSE = "xpath=//input[contains(@class,'undecided_address_house')]"
    PHONE = "xpath=//input[contains(@class,'undecided_address_phone')]"
    BUTTON_SEND = "xpath=//input[contains(@class,'undecided_address_button_send')]"
    BUTTON_CHANGE_CITY = "xpath=//button[contains(@class,'undecided_address_button_change_city')]"
    UNDECIDED_BLOCK = "xpath=//div[contains(@id,'checkaddress-undecided')]"


class Business:
    FULL_ADDRESS = "xpath=//input[contains(@class,'business_no_address_full_address')]"
    PHONE = "xpath=//input[contains(@class,'business_no_address_phone')]"
    BUTTON_SEND = "xpath=//input[contains(@class,'business_no_address_button_send')]"

    MORE_BUTTON = "xpath=//a[contains(@class,'services-business')]"
    MORE_BUTTON_SECOND = "xpath=//button[contains(@class,'services-business')]"
    MORE_BUTTON_ANY = "xpath=//div[contains(@class,'services-business')]//a[contains(@href,'/business')]"

    BUSINESS_BUTTON = "xpath=(//a[@href='/business/business'])[1]"
    BUSINESS_BUTTON_SECOND = "xpath=//a[text()='Для бизнеса']"
    BUSINESS_BUTTON_THIRD = "xpath=(//a[text()='Бизнесу'])[2]"
    BUSINESS_BUTTON_FOUR = "xpath=(//a[text()='Бизнесу'])[1]"
    BUSINESS_BUTTON_BEELINE = "xpath=(//a[text()='бизнесу'])[1]"

    CONNECT_BUTTON = "xpath=//a[contains(@class,'business_no_address_button')]"
    CONNECT_BUTTON_SECOND = "xpath=//button[contains(@class,'business_no_address_button')]"


class Moving:
    STREET = "xpath=//input[contains(@class,'moving_address_street')]"
    HOUSE = "xpath=//input[contains(@class,'moving_address_house')]"
    PHONE = "xpath=//input[contains(@class,'moving_address_phone')]"
    BUTTON_SEND = "xpath=//input[contains(@class,'moving_address_button_send')]"
    BUTTON_CHANGE_CITY = "xpath=//span[contains(@class,'moving_address_button_change_city')]"

    MOVING_BUTTON = "xpath=//button[contains(@class,'moving_address_button')]"


class ExpressConnection:
    STREET = "xpath=(//input[contains(@class,'express-connection_address_street')])[1]"
    HOUSE = "xpath=(//input[contains(@class,'express-connection_address_house')])[1]"
    PHONE = "xpath=(//input[contains(@class,'express-connection_address_phone')])[1]"
    BUTTON_SEND = "xpath=(//input[contains(@class,'express-connection_address_button_send')])[1]"
    BUTTON_CHANGE_CITY = "xpath=(//div[contains(@class,'express-connection_address_button_change_city')])[1]"

    FORM_BUTTON = "xpath=(//button[contains(@class,'connection_address_button')])[1]"


