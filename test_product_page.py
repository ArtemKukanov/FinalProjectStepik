import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage

"""Тест на возможность положить товар в корзину"""
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

"""Тест на невозможность увидеть ненужное сообщение после добавления товара в корзину"""
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019" # рекомендация из урока https://stepik.org/lesson/201964/step/6?unit=176022 (комментарии)
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) # объяснение в test_guest_can_add_product_to_basket
    page.open() # объяснение в test_guest_can_add_product_to_basket
    page.add_product_to_basket() # объяснение в test_guest_can_add_product_to_basket
    page.solve_quiz_and_get_code() # объяснение в test_guest_can_add_product_to_basket
    page.should_not_be_success_message() # Метод should_not_be_success_message производит действия над page -- смотрит что сообщения об успехе нет

"""Тест на невозможность увидеть ненужное сообщение до добавления товара в корзину (сразу после перехода на сайт)"""
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) # объяснение в test_guest_can_add_product_to_basket
    page.open() # объяснение в test_guest_can_add_product_to_basket
    page.should_not_be_success_message() # Метод should_not_be_success_message производит действия над page -- смотрит что сообщения об успехе нет

"""Тест на то, что сообщение исчезает после добавления товара в корзину"""
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) # объяснение в test_guest_can_add_product_to_basket
    page.open() # объяснение в test_guest_can_add_product_to_basket
    page.add_product_to_basket() # объяснение в test_guest_can_add_product_to_basket
    page.solve_quiz_and_get_code() # объяснение в test_guest_can_add_product_to_basket
    assert page.is_disappeared(*ProductPageLocators.SUCSSESEFUL_MESSAGE),'Сообщение об успехе не исчезло' # Метод s_disappeared производит действия над page -- смотрит что сообщения об успехе исчезло

"""Тест на то, что гость должен видеть ссылку на логин на странице продукта"""
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) # объяснение в test_guest_can_add_product_to_basket
    page.open() # объяснение в test_guest_can_add_product_to_basket
    page.should_be_login_link() # тестируем, есть ли вообще такой линк с помощью селектора

"""Тест на то, что гость должен перейти на страницу логина из продуктовой страницы"""
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) # объяснение в test_guest_can_add_product_to_basket
    page.open() # объяснение в test_guest_can_add_product_to_basket
    page.go_to_login_page() # открываем страницу для логина из страницы продукта 

"""Тест на то, что гость не может увидеть добавленный в корзину продукт из страницы продукта"""
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link) # объяснение в test_guest_can_add_product_to_basket
    page.open() # объяснение в test_guest_can_add_product_to_basket
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url) # стандартный переход, описанный в https://stepik.org/lesson/238819/step/9
    basket_page.basket_is_empty()
    basket_page.message_about_empty_basket_exists()
