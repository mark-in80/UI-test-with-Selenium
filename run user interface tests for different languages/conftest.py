import pytest-3
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language')


@pytest.mark.parametrize('--language')
    def browser(self,language):
        browser = webdriver.Chrome()
        link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        browser.get(link)
    yield browser
        browser.quit()
        
