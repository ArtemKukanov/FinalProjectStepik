from selenium.webdriver.common.by import By

"""Класс локаторов, относящихся к URL логина"""
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

"""Класс локаторов, относящихся к странице регистрации"""
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

"""Класс локаторов, относящихся к странице продукта"""
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket") # кнопка добавления товара в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 h1") # название со страницы
    ALERT_NAME = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong") # название из алерта
    PRODUCT_PRICE = (By.CSS_SELECTOR,"p.price_color") # цена из со страницы
    ALERT_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong") # цена из алерта
