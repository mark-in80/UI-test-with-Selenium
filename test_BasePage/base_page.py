from selenium import webdriver


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)


name = BasePage(browser=webdriver.Chrome(), url="https://stepik.org/lesson/238819/step/2?unit=211271")
name.open()
