from selenium import webdriver
import time, os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys('Yefim')
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys('Mironyuk')
    first_name = browser.find_element_by_name("email")
    first_name.send_keys('yefimmironyuk@gmail.com')
    sendfile = browser.find_element_by_id("file")
    sendfile.send_keys(file_path)
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
finally:
    time.sleep(5)
    browser.quit()