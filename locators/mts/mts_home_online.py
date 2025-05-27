class MTSHomeOnlineMain:
    SUPER_OFFER_HEADER = "xpath=//div[contains(text(),'Выгодное спецпредложение!')]"
    SUPER_OFFER_TEXT = "xpath=//div[contains(text(),'С экономией в год от 9000 рублей!')]"
    INPUT_OFFER_POPUP = "xpath=(//input[@name='Phone'])[5]"
    SEND_BUTTON_OFFER_POPUP = "xpath=(//form[@aria-label='Контактная форма']//input[@value='Отправить'])[2]"
    THANKYOU_TEXT = "xpath=//div[@class='thanks']"
    RED_BUTTON = "xpath=//button[@class='button-lead-catcher']"
    CLOSE_BUTTON = "xpath=//a[@class='thanks__close']//img[@alt='Вектор закрытия']"

