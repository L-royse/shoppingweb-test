from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Sauce Demo 登录页"""

    URL = "https://www.saucedemo.com/"

    # 元素定位符
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def open_login_page(self):
        self.open(self.URL)
        return self

    def login(self, username, password):
        self.input_text(self.USERNAME, username)
        self.input_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        return self

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)

    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MSG)