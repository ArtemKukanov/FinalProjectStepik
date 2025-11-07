import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .pages.product_page import ProductPage

"""Параметризация запуска"""
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail), # marks=pytest.mark.xfail -- параметр помечается как ожидающий сбой (xfail — expected failure)
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link) # создается объект page, принадлежащий классу ProductPage (ProductPage -- наследник BasePage), page принимает все "def" из ProductPage в product_page.py
    page.open() # страница (page) открывается с помощью функции (def open) принадлежащей классу BasePage, описанному в base_page.py (но технически def open принадлежит и дочернему классу ProductPage)
    page.add_product_to_basket() # тестоввый метод add_product_to_basket производит действия над page
    page.solve_quiz_and_get_code() # тестоввый метод solve_quiz_and_get_code производит действия над page
    page.verification__product_name() # тестоввый метод verification__product_name производит действия над page
    page.verification__product_price() # тестоввый метод verification__product_price производит действия над page
