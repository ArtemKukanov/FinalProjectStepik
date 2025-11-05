import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser): # hook-функция PyTest, вызывается при инициализации pytest (это и есть конфигурация PyTest)
    parser.addoption('--language', action='store', default='en', help="Choose language") # новая опция --language

@pytest.fixture(scope="function") # декоратор/фикстура - настраивает браузер на уровне функции
def browser(request): # обявляем функцию browser в рамках фикстуры (то есть это отдельный объект, который создается и управляется pytest с областью видимости function)
    browser_language = request.config.getoption("language") # считывается значение опции `--language` из конфигурации pytest в addoption
    options = Options() # создается объект настроек для Chrome
    options.add_argument(f"--lang={browser_language}") # в аргументы запуска Chrome, передается параметр `--lang=код_языка`
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    print(f"\nstart browser for test with language={browser_language}")
    browser = webdriver.Chrome(options=options) # Условно: вызови конструктор Chrome, передай туда настройки браузера, которые содержатся в переменной `options`
    yield browser # останавливается работа браузера и сохраняется его локальное состояние 
    print("\nquit browser..")
    browser.quit() # выход из браузера
