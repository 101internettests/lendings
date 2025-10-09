class InternetMTSHomeOnlineMain:
    SUPER_OFFER_HEADER = "xpath=(//div[contains(text(),'Выгодное спецпредложение!')])[1]"
    SUPER_OFFER_TEXT = "xpath=(//div[contains(text(),'С экономией в год от 9000 рублей!')])[1]"
    ACCEPT_COOKIES = "xpath=//button[@id='cookieAccept']"
    BANNER = "xpath=//button[contains(text(),'Подобрать тариф')]"
    HEADER_LINKS = {
        "home": "xpath=(//a[contains(text(),'Домашний интернет')])[1]",
        "all_internet": "xpath=(//a[contains(text(),'Всё в одном')])[1]",
        "mobile": "xpath=(//a[contains(text(),'Мобильная связь')])[1]"
    }
    FOOTER_LINKS = {
        "cookie_policy": "xpath=//a[contains(text(),'Политики обработки файлов cookie')]"
    }