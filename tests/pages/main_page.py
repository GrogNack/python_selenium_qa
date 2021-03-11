from selenium.webdriver.common.by import By
from base_page import BasePage


class MainPageLocators:
    LOCATOR_MAIN_CAROUSEL = (By.CSS_SELECTOR, 'div.swiper-viewport>div#slideshow0')
    LOCATOR_LOGO = (By.CSS_SELECTOR, 'div#logo')
    LOCATOR_SEARCH_FIELD = (By.CSS_SELECTOR, 'input[name="search"]')
    LOCATOR_HEAD_FEATURED_GOODS = (By.CSS_SELECTOR, 'h3')
    LOCATOR_FEATURED_GOODS = (By.CSS_SELECTOR, 'div.row>div[class^=product-layout]')


class MainPage(BasePage):
    path = ''
