from selenium import webdriver
import time
import unittest


class Testing(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_bibos(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration2.html")
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_bibos2(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration1.html")
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()