from selenium.webdriver.common.by import By
from .base_page import BasePage


class AdminPageLocators:
    LOCATOR_SUBMIT_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')
    LOCATOR_USERNAME_LBL = (By.CSS_SELECTOR, 'label[for="input-username"]')
    LOCATOR_USERNAME_FIELD = (By.CSS_SELECTOR, '#input-username')
    LOCATOR_PWD_LBL = (By.CSS_SELECTOR, 'label[for="input-password"]')
    LOCATOR_PWD_FIELD = (By.CSS_SELECTOR, '#input-password')
    LOCATOR_TITLE_PANEL = (By.CSS_SELECTOR, 'h1.panel-title')
    LOCATOR_FORGOTTEN_LINK = (By.CSS_SELECTOR, 'span.help-block>a')
    LOCATOR_CATALOG_ITEM = (By.CSS_SELECTOR, '#menu-catalog')
    LOCATOR_PRODUCTS_ITEM = (By.LINK_TEXT, 'Products')
    LOCATOR_INFO_TEXT = (By.CSS_SELECTOR, 'div.row>div.text-right')
    LOCATOR_ADD_NEW_BTN = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    LOCATOR_PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, '#input-name1')
    LOCATOR_PRODUCT_META_FIELD = (By.CSS_SELECTOR, '#input-meta-title1')
    LOCATOR_PRODUCT_DATA_TAB = (By.CSS_SELECTOR, '[href="#tab-data"]')
    LOCATOR_PRODUCT_MODEL_FIELD = (By.CSS_SELECTOR, '[name="model"]')
    LOCATOR_PRODUCT_SAVE_BTN = (By.CSS_SELECTOR, '.fa-save')
    LOCATOR_FILTER_FIELD = (By.CSS_SELECTOR, '[name="filter_name"]')
    LOCATOR_FILTER_BTN = (By.CSS_SELECTOR, '#button-filter')
    LOCATOR_PRODUCTS_ROW = (By.CSS_SELECTOR, '.table>tbody>tr')


class AdminPage(BasePage):
    path = '/admin/'

    def get_submit_btn(self):
        return self.find_elements(AdminPageLocators.LOCATOR_SUBMIT_BTN)

    def get_lbl_username(self):
        return self.find_elements(AdminPageLocators.LOCATOR_USERNAME_LBL)

    def get_lbl_pwd(self):
        return self.find_elements(AdminPageLocators.LOCATOR_PWD_LBL)

    def get_title_panel(self):
        return self.find_elements(AdminPageLocators.LOCATOR_TITLE_PANEL)

    def get_forgotten_link(self):
        return self.find_elements(AdminPageLocators.LOCATOR_FORGOTTEN_LINK)

    def login(self, user, pwd):
        username_field = self.find_element(AdminPageLocators.LOCATOR_USERNAME_FIELD)
        pwd_field = self.find_element(AdminPageLocators.LOCATOR_PWD_FIELD)
        username_field.clear()
        username_field.send_keys(user)
        pwd_field.clear()
        pwd_field.send_keys(pwd)
        btn = self.find_element(AdminPageLocators.LOCATOR_SUBMIT_BTN)
        btn.click()

    def open_catalog_section(self):
        self.find_element(AdminPageLocators.LOCATOR_CATALOG_ITEM).click()
        self.find_element(AdminPageLocators.LOCATOR_PRODUCTS_ITEM).click()

    def get_count_of_goods(self):
        text = self.find_element(AdminPageLocators.LOCATOR_INFO_TEXT).text
        result = text.split(' ')[5]
        return result

    def add_new_product(self, name):
        self.find_element(AdminPageLocators.LOCATOR_ADD_NEW_BTN).click()
        name_field = self.find_element(AdminPageLocators.LOCATOR_PRODUCT_NAME_FIELD)
        meta_field = self.find_element(AdminPageLocators.LOCATOR_PRODUCT_META_FIELD)
        name_field.clear()
        name_field.send_keys(name)
        meta_field.clear()
        meta_field.send_keys(name + '_tag')
        self.find_element(AdminPageLocators.LOCATOR_PRODUCT_DATA_TAB).click()
        model_field = self.find_element(AdminPageLocators.LOCATOR_PRODUCT_MODEL_FIELD)
        model_field.clear()
        model_field.send_keys(name + '_model')
        self.find_element(AdminPageLocators.LOCATOR_PRODUCT_SAVE_BTN).click()

    def filter_products(self, name):
        product_name_field = self.find_element(AdminPageLocators.LOCATOR_FILTER_FIELD)
        product_name_field.clear()
        product_name_field.send_keys(name)
        self.find_element(AdminPageLocators.LOCATOR_FILTER_BTN).click()

    def get_products_row(self):
        return self.find_elements(AdminPageLocators.LOCATOR_PRODUCTS_ROW)

    def get_prod_name_from_table_row(self):
        element = self.find_element(AdminPageLocators.LOCATOR_PRODUCTS_ROW)
        list_test_tr = element.text.split(' ')
        prod_name = list_test_tr[0] + ' ' + list_test_tr[1]
        return prod_name
