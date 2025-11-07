from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_btn.click()
    """Функция сравнения названий продукта на странице и в алерте"""
    def verification__product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME), "названия продукта нет на странице" # узнаем есть ли вообще название продукта на странице
        assert self.browser.find_element(*ProductPageLocators.ALERT_NAME), "названия продукта нет в алерте" # узнаем есть ли вообще название продукта в алерте
        name_product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text # текст из селектора PRODUCT_NAME на странице
        name_product_alert = self.browser.find_element(*ProductPageLocators.ALERT_NAME).text # текст из селектора PRODUCT_NAME из алерта
        assert name_product_page == name_product_alert, "названия продукта не совпадают на странице и в алерте" # производим сравнение названий

    """Функция сравнения цен продукта на странице и в алерте"""
    def verification__product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), "цены продукта нет на странице" # узнаем есть ли вообще цена продукта на странице
        assert self.browser.find_element(*ProductPageLocators.ALERT_PRICE), "цены продукта нет в алерте" # узнаем есть ли вообще цена продукта в алерте
        price_product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text # текст из селектора PRODUCT_PRICE на странице
        price_product_alert = self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text # текст из селектора ALERT_PRICE из алерта
        assert price_product_page == price_product_alert, "цены продукта не совпадают на странице и в алерте" # производим сравнение цен
