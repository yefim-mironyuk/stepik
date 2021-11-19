from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    name.send_keys("Yefim")
    last_name = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    last_name.send_keys("Mironyuk")
    email = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    email.send_keys("yefimmironyk@gmail.com")


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()