from selenium.webdriver.common.by import By
from .base_page import BasePage


class CatalogPageLocators:
    LOCATOR_GOODS = (By.CSS_SELECTOR, 'div.row>div[class^=product-layout]')
    LOCATOR_TEXT_OF_GOODS = (By.CSS_SELECTOR, 'div.row>div[class~=text-right]')
    LOCATOR_COPYRIGHT_TEXT = (By.CSS_SELECTOR, 'footer p')
    LOCATOR_BTN_VIEW = (By.CSS_SELECTOR, 'div.row button[id$=view]')


class CatalogPage(BasePage):
    path = '/index.php?route=product/category&path=20'

    def get_goods(self):
        return self.find_elements(CatalogPageLocators.LOCATOR_GOODS)

    def get_text_of_goods(self):
        return self.find_elements(CatalogPageLocators.LOCATOR_TEXT_OF_GOODS)

    def get_copyright_text(self):
        return self.find_elements(CatalogPageLocators.LOCATOR_COPYRIGHT_TEXT)

    def get_btn_view(self):
        return self.find_elements(CatalogPageLocators.LOCATOR_BTN_VIEW)
