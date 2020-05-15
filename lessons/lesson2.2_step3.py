from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

# run browser
try:
    # open browser Chrome
    browser = webdriver.Chrome()
    # jump to link
    browser.get(link)
    # assignment x,y selector by id element
    x = browser.find_element_by_id("num1")
    z = browser.find_element_by_id("num2")
    # assignment "one" and "two" read text from selector id element
    one = x.text
    two = z.text
    # sum variable in string type
    s = str(int(one) + int(two))
    # call class in libraty
    select = Select(browser.find_element_by_tag_name("select"))
    # search selector by value, where s -  #sum variable "one" and "two" in str type
    select.select_by_value(s)
    # search selector button 
    button = browser.find_element_by_css_selector("[class='btn btn-default']")
    button.click()

# close browser
finally:
    #page browser open 10s.
    time.sleep(10)
    #close browser
    browser.quit()

# null string for run script to python 
