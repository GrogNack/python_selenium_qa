from selenium.webdriver.common.by import By
from base_page import BasePage


class CatalogPageLocators:
    LOCATOR_GOODS = (By.CSS_SELECTOR, 'div.row>div[class^=product-layout]')
    LOCATOR_TEXT_OF_GOODS = (By.CSS_SELECTOR, 'div.row>div[class~=text-right]')
    LOCATOR_COPYRIGHT_TEXT = (By.CSS_SELECTOR, 'footer p')
    LOCATOR_BTN_VIEW = (By.CSS_SELECTOR, 'div.row button[id$=view]')


class CatalogPage(BasePage):
    path = '/index.php?route=product/category&path=20'

