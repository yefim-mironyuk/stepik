from selenium import webdriver
import time
import math
import pytest


@pytest.fixture(scope='function')
def browser():
    print('\nStarting browser...')
    browser = webdriver.Chrome()
    yield browser
    print('\nQuitting browser...')
    browser.quit()



@pytest.mark.parametrize('links', ['895', '896', '897', '898', '899', '903', '904', '905'])
def test_message_finder(browser, links):
        link = f'https://stepik.org/lesson/236{links}/step/1'
        browser.get(link)
        answer = str(math.log(int(time.time())))
        browser.implicitly_wait(10)
        input1 = browser.find_element_by_tag_name('textarea')
        input1.send_keys(answer)
        button = browser.find_element_by_class_name('submit-submission')
        button.click()
        browser.implicitly_wait(10)
        output1 = browser.find_element_by_class_name("smart-hints__hint")
        assert output1.text == 'Correct!', 'ERROR!'

