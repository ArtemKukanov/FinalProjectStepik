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
    PRODUCT_PRICE = (By.CSS_SELECTOR,"p.price_color") # цена из со страницы
    ALERT_NAME = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong") # конкретно само название из алерта
    ALERT_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong") # цена из алерта
    SUCSSESEFUL_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child") # сам алерт

"""Класс базовых локаторов"""
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_BASKET = (By.CSS_SELECTOR, ".btn-group > .btn.btn-default")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
