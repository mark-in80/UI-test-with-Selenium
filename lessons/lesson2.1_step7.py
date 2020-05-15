from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element  = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")

    def calc(x):
        z = str(math.log(abs(12*math.sin(int(x)))))
        return z
	
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()		
    
    radio_button = browser.find_element_by_id("robotsRule")
    radio_button.click()

    button = browser.find_element_by_css_selector("[class='btn btn-default']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
