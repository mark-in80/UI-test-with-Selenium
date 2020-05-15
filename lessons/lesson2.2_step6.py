from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element  = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        z = str(math.log(abs(12*math.sin(int(x)))))
        return z
	
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()		
    
    radio_button = browser.find_element_by_id("robotsRule")
    

    button = browser.find_element_by_css_selector("[class='btn btn-primary']")
    # scroll page to 100px
    browser.execute_script("window.scrollBy(0, 100);")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button) - if onlock 
    # this string, them scroll full page browser
    radio_button.click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()

# 
