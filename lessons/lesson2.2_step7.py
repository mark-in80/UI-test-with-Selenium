from selenium import webdriver
import time 
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Alex")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Lyamsev")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("liamka23@inbox.ru")
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
  
    file_py = browser.find_element_by_id("file")
# получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))     
# добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'example.py')           
    file_py.send_keys(file_path)
    button.click()

finally:
    time.sleep(10)
    browser.quit()

# 
