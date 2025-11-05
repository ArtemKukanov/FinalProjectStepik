class BasePage():
    def __init__(self, browser, url):
        # Конструктор класса
        self.browser = browser
        self.url = url

    def open(self):
        # метод open открывает нужную страницу
        self.browser.get(self.url)