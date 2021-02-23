from selenium.webdriver.common.by import By


def test_open_main_page(browser, base_url):
    browser.get(base_url)
    assert browser.title == 'Your Store'
    element = browser.find_element(By.CSS_SELECTOR, 'a[href="http://www.opencart.com"]')
    assert element.text == 'OpenCart'


def test_main_page(browser, base_url):
    browser.get(base_url)
    main_carousel = browser.find_elements(By.CSS_SELECTOR, 'div.swiper-viewport>div#slideshow0')
    assert len(main_carousel) == 1
    logo = browser.find_elements(By.CSS_SELECTOR, 'div#logo')
    assert len(logo) == 1
    search_field = browser.find_elements(By.CSS_SELECTOR, 'input[name="search"]')
    assert len(search_field) == 1
    head_featured_goods = browser.find_elements(By.CSS_SELECTOR, 'h3')
    assert len(head_featured_goods) == 1
    featured_goods = browser.find_elements(By.CSS_SELECTOR, 'div.row>div[class^=product-layout]')
    assert len(featured_goods) == 4


def test_catalog_page(browser, base_url):
    browser.get(base_url + '/index.php?route=product/category&path=20')
    goods = browser.find_elements(By.CSS_SELECTOR, 'div.row>div[class^=product-layout]')
    assert len(goods) == 12
    text_of_goods = browser.find_elements(By.CSS_SELECTOR,'div.row>div[class~=text-right]')
    assert len(text_of_goods) == 1
    text_of_goods = text_of_goods[0].text.split(" ")
    assert int(text_of_goods[5]) == len(goods)
    copyright_text = browser.find_elements(By.CSS_SELECTOR, 'footer p')
    assert copyright_text[0].text == 'Powered By OpenCart\nYour Store © 2021'
    button_view = browser.find_elements(By.CSS_SELECTOR, 'div.row button[id$=view]')
    assert len(button_view) == 2


def test_goods_page(browser, base_url):
    browser.get(base_url + '/index.php?route=product/product&path=57&product_id=49')
    goods_title = browser.find_elements(By.CSS_SELECTOR, 'div#content h1')
    assert len(goods_title) == 1
    thumbnails = browser.find_elements(By.CSS_SELECTOR, 'ul.thumbnails')
    assert len(thumbnails) == 1
    goods_name_breadcrumb = browser.find_elements(By.CSS_SELECTOR, 'ul.breadcrumb li:last-child>a')
    assert len(goods_name_breadcrumb) == 1
    assert goods_name_breadcrumb[0].text == goods_title[0].text
    tooltip_btn = browser.find_elements(By.CSS_SELECTOR, 'button[data-toggle="tooltip"]')
    assert len(tooltip_btn) == 2
    nav_tabs = browser.find_elements(By.CSS_SELECTOR, 'ul[class$="nav-tabs"]')
    assert len(nav_tabs) == 1


def test_login_page(browser, base_url):
    browser.get(base_url + '/index.php?route=account/login')
    right_menu = browser.find_elements(By.CSS_SELECTOR, 'aside#column-right')
    assert len(right_menu) == 1
    register_account_block = browser.find_elements(By.CSS_SELECTOR, 'div.row div.col-sm-6:first-child')
    assert len(register_account_block) == 1
    returning_account_block = browser.find_elements(By.CSS_SELECTOR, 'div.row div.col-sm-6:last-child')
    assert len(returning_account_block) == 1
    login_button = browser.find_elements(By.CSS_SELECTOR, 'input[value="Login"]')
    assert len(login_button) == 1
    continue_button = browser.find_elements(By.CSS_SELECTOR, 'p + a')
    assert len(continue_button) == 1


def test_admin_page(browser, base_url):
    browser.get(base_url + '/admin/')
    submit_btn = browser.find_elements(By.CSS_SELECTOR, 'button[type="submit"]')
    assert len(submit_btn) == 1
    label_username = browser.find_elements(By.CSS_SELECTOR, 'label[for="input-username"]')
    assert len(label_username) == 1
    label_password = browser.find_elements(By.CSS_SELECTOR, 'label[for="input-password"]')
    assert len(label_password) == 1
    title_panel = browser.find_elements(By.CSS_SELECTOR, 'h1.panel-title')
    assert len(title_panel) == 1
    forgotten_link = browser.find_elements(By.CSS_SELECTOR, 'span.help-block>a')
    assert len(forgotten_link) == 1
