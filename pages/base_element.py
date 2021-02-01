from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver, by, value):
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator)
        )
        self.web_element = element
        return None

    def input(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        self.web_element = element
        element.send_keys(text)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        self.web_element = element
        element.click()
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text
