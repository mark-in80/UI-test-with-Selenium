from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element_by_css_selector("[class='trollface btn btn-primary']")
    button_1.click()
    # working with open new "window"
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
