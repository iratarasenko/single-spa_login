from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

test_data = [
    ['admin', '12345'],
    ['', '']
]

browser = webdriver.Chrome()


def valid_input():
    page = LoginPage(driver=browser)
    page.go()
    page.username.input(test_data[0][0])
    page.password.input(test_data[0][1])
    page.sign_in.click()
    admin_mark = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, '__BVID__23__BV_button_'))
    )
    assert admin_mark.text == 'admin'
    print('done 1')
    browser.quit()


def empty_fields():
    page = LoginPage(driver=browser)
    page.go()
    page.username.input(test_data[1][0])
    page.password.input(test_data[1][1])
    page.sign_in.click()
    assert page.toast_message.text == 'Invalid credentials'
    print('done 2')
    browser.quit()
