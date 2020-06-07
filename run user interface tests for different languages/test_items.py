from selenium import webdriver

class TestLanguage(browser):
    
    def test_language():
        button = browser.find_element_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
        button.click()
        
        x_element = browser.find_element_by_id("input_value")
        x = x_element.text

    assert x == " был добавлен в вашу карзину." 
