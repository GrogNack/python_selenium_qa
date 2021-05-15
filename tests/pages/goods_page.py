from selenium.webdriver.common.by import By
from .base_page import BasePage


class GoodsPageLocators:
    LOCATOR_GOODS_TITLE = (By.CSS_SELECTOR, 'div#content h1')
    LOCATOR_THUMBNAILS = (By.CSS_SELECTOR, 'ul.thumbnails')
    LOCATOR_GOODS_NAME_BREADCRUMB = (By.CSS_SELECTOR, 'ul.breadcrumb li:last-child>a')
    LOCATOR_TOOLTIP_BTN = (By.CSS_SELECTOR, 'button[data-toggle="tooltip"]')
    LOCATOR_NAV_TABS = (By.CSS_SELECTOR, 'ul[class$="nav-tabs"]')


class GoodsPage(BasePage):
    path = '/index.php?route=product/product&path=57&product_id=49'

    def get_goods_title(self):
        return self.find_elements(GoodsPageLocators.LOCATOR_GOODS_TITLE)

    def get_thumbnails(self):
        return self.find_elements(GoodsPageLocators.LOCATOR_THUMBNAILS)

    def get_goods_name_breadcrumb(self):
        return self.find_elements(GoodsPageLocators.LOCATOR_GOODS_NAME_BREADCRUMB)

    def get_tooltip_btn(self):
        return self.find_elements(GoodsPageLocators.LOCATOR_TOOLTIP_BTN)

    def get_nav_tabs(self):
        return self.find_elements(GoodsPageLocators.LOCATOR_NAV_TABS)
