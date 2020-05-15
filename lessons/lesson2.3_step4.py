from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # dialog windows
    button_1 = browser.find_element_by_css_selector("[class='btn btn-primary']")
    button_1.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        z = str(math.log(abs(12*math.sin(int(x)))))
        return z
	
    y = calc(x)
    input1 = browser.find_element_by_class_name("form-control")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("[class='btn btn-primary']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

# 
