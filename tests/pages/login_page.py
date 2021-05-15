from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPageLocators:
    LOCATOR_RIGHT_MENU = (By.CSS_SELECTOR, 'aside#column-right')
    LOCATOR_REGISTER_ACCOUNT_BLOCK = (By.CSS_SELECTOR, 'div.row div.col-sm-6:first-child')
    LOCATOR_RETURNING_ACCOUNT_BLOCK = (By.CSS_SELECTOR, 'div.row div.col-sm-6:last-child')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'input[value="Login"]')
    LOCATOR_CONTINUE_BTN = (By.CSS_SELECTOR, 'p + a')


class LoginPage(BasePage):
    path = '/index.php?route=account/login'

    def get_right_menu(self):
        return self.find_elements(LoginPageLocators.LOCATOR_RIGHT_MENU)

    def get_register_account_block(self):
        return self.find_elements(LoginPageLocators.LOCATOR_REGISTER_ACCOUNT_BLOCK)

    def get_returning_account_block(self):
        return self.find_elements(LoginPageLocators.LOCATOR_RETURNING_ACCOUNT_BLOCK)

    def get_login_btn(self):
        return self.find_elements(LoginPageLocators.LOCATOR_LOGIN_BTN)

    def get_continue_btn(self):
        return self.find_elements(LoginPageLocators.LOCATOR_CONTINUE_BTN)
