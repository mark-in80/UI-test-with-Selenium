from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    text_read = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button_1 = browser.find_element_by_css_selector("[class='btn btn-primary']")
    button_1.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        z = str(math.log(abs(12*math.sin(int(x)))))
        return z
	
    y = calc(x)
    input1 = browser.find_element_by_css_selector("[class='form-control']")
    input1.send_keys(y)

    button_2 = browser.find_element_by_id("solve")
    button_2.click()

finally:
    time.sleep(10)
    browser.quit()

# 
