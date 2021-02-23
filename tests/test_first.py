from selenium.webdriver.common.by import By


def test_open_main_page(browser, base_url):
    browser.get(base_url)
    assert browser.title == 'Your Store'
    element = browser.find_element(By.CSS_SELECTOR, 'a[href="http://www.opencart.com"]')
    assert element.text == 'OpenCart'
