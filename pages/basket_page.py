from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_PRODUCTS), "корзина не пустая"

    def message_about_empty_basket_exists(self):
        assert self.is_element_present(*BasePageLocators.MESSAGE_EMPTY_BASKET), "текста о пустой корзине нет" 