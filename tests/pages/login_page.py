from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPageLocators:
    LOCATOR_RIGHT_MENU = (By.CSS_SELECTOR, 'aside#column-right')
    LOCATOR_REGISTER_ACCOUNT_BLOCK = (By.CSS_SELECTOR, 'div.row div.col-sm-6:first-child')
    LOCATOR_RETURNING_ACCOUNT_BLOCK = (By.CSS_SELECTOR, 'div.row div.col-sm-6:last-child')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'input[value="Login"]')
    LOCATOR_CONTINUE_BTN = (By.CSS_SELECTOR, 'p + a')


class LoginPage(BasePage):
    path = '/index.php?route=account/login'
