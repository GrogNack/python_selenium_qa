from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPageLocators:
    LOCATOR_MAIN_CAROUSEL = (By.CSS_SELECTOR, 'div.swiper-viewport>div#slideshow0')
    LOCATOR_LOGO = (By.CSS_SELECTOR, 'div#logo')
    LOCATOR_SEARCH_FIELD = (By.CSS_SELECTOR, 'input[name="search"]')
    LOCATOR_HEAD_FEATURED_GOODS = (By.CSS_SELECTOR, 'h3')
    LOCATOR_FEATURED_GOODS = (By.CSS_SELECTOR, 'div.row>div[class^=product-layout]')
    LOCATOR_POWERED_BY_LINK = (By.CSS_SELECTOR, 'a[href="http://www.opencart.com"]')


class MainPage(BasePage):
    path = ''

    def get_title(self):
        return self.driver.title

    def get_link_powered_by_text(self):
        return self.find_elements(MainPageLocators.LOCATOR_POWERED_BY_LINK)[0].text

    def get_main_carousel(self):
        return self.find_elements(MainPageLocators.LOCATOR_MAIN_CAROUSEL)

    def get_logo(self):
        return self.find_elements(MainPageLocators.LOCATOR_LOGO)

    def get_search_field(self):
        return self.find_elements(MainPageLocators.LOCATOR_SEARCH_FIELD)

    def get_head_featured_goods(self):
        return self.find_elements(MainPageLocators.LOCATOR_HEAD_FEATURED_GOODS)

    def get_featured_goods(self):
        return self.find_elements(MainPageLocators.LOCATOR_FEATURED_GOODS)
