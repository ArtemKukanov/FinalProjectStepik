import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# объявляется текстовый класс TestOfLanding
class TestOfLanding:
    def test_of_button(self, browser): # объявляется тестовый метод test_of_button
        browser.get(link) # браузер получает ссылку из link (браузер объявляется в фикстуре browser и передавается в тест как параметр)
        time.sleep(30) # браузер тормозит на 30 секунд
        button_add = WebDriverWait(browser, 10). until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))) # браузер ждет элемент 10 секунд или пока элемент не станет видимым
        assert button_add is not None # выполняется проверка, что переменная button_add не равна значению None, если button_add действительно содержит какой-либо объект (то есть не является None), то программа продолжит работу без ошибок
