import time


def test_items(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(10)
    button = browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    time.sleep(5)
    assert button is not None
