from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_elements_by_xpath('//input[@required]')
    input1[0].send_keys("Yefim")
    input1[1].send_keys("Mironyuk")
    input1[2].send_keys("yefimmironyuk@gmail.com")

    # проверим, что полей по прежнему 3
    assert len(input1) == 3

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()