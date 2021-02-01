from selenium.webdriver.common.by import By
from pages.base_element import BaseElement


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://single-spa-with-npm-packages.herokuapp.com/login'

    def go(self):
        self.driver.get(self.url)

    @property
    def username(self):
        locator = (By.CSS_SELECTOR, 'input[type="text"]')
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )

    @property
    def password(self):
        locator = (By.CSS_SELECTOR, 'input[type="password"]')
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )

    @property
    def sign_in(self):
        locator = (By.CSS_SELECTOR, 'form button')
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )
    @property
    def toast_message(self):
        locator = (By.CSS_SELECTOR, 'div[class="toast-message"]')
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )
