from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    summary = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summary))
    button = browser.find_element_by_class_name("btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()