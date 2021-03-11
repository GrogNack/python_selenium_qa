from selenium.webdriver.common.by import By
from base_page import BasePage


class AdminPageLocators:
    LOCATOR_SUBMIT_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')
    LOCATOR_USERNAME_LBL = (By.CSS_SELECTOR, 'label[for="input-username"]')
    LOCATOR_PWD_LBL = (By.CSS_SELECTOR, 'label[for="input-password"]')
    LOCATOR_TITLE_PANEL = (By.CSS_SELECTOR, 'h1.panel-title')
    LOCATOR_FORGOTTEN_LINK = (By.CSS_SELECTOR, 'span.help-block>a')


class AdminPage(BasePage):
    path = '/admin/'
