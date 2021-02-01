from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from pages.login_page import LoginPage

credentials = [
    ['admin', '12345'],
    ['', '']
]

browser = webdriver.Chrome()


def test_valid_input():
    page = LoginPage(driver=browser)
    page.go()
    page.username.input(credentials[0][0])
    page.password.input(credentials[0][1])
    page.sign_in.click()
    homeapp = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[class="ng-binding"]'))
    )
    assert homeapp.text == 'Home app'


def test_empty_fields():
    page = LoginPage(driver=browser)
    page.go()
    page.username.input(credentials[1][0])
    page.password.input(credentials[1][1])
    page.sign_in.click()
    assert page.toast_message.text == 'Invalid credentials'
