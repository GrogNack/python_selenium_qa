from pages import MainPage, AdminPage, CatalogPage, GoodsPage, LoginPage

ADMIN_USER = 'user'
ADMIN_PWD = 'bitnami'


def test_open_main_page(browser, base_url):
    mp = MainPage(browser)
    mp.open(base_url, mp.path)
    assert mp.get_title() == 'Your Store'
    assert mp.get_link_powered_by_text() == 'OpenCart'


def test_main_page(browser, base_url):
    mp = MainPage(browser)
    mp.open(base_url, mp.path)
    main_carousel = mp.get_main_carousel()
    assert len(main_carousel) == 1
    logo = mp.get_logo()
    assert len(logo) == 1
    search_field = mp.get_search_field()
    assert len(search_field) == 1
    head_featured_goods = mp.get_head_featured_goods()
    assert len(head_featured_goods) == 1
    featured_goods = mp.get_featured_goods()
    assert len(featured_goods) == 4


def test_catalog_page(browser, base_url):
    cp = CatalogPage(browser)
    cp.open(base_url, cp.path)
    goods = cp.get_goods()
    assert len(goods) == 12
    text_of_goods = cp.get_text_of_goods()
    assert len(text_of_goods) == 1
    text_of_goods = text_of_goods[0].text.split(" ")
    assert int(text_of_goods[5]) == len(goods)
    copyright_text = cp.get_copyright_text()
    assert copyright_text[0].text == 'Powered By OpenCart\nYour Store © 2021'
    button_view = cp.get_btn_view()
    assert len(button_view) == 2


def test_goods_page(browser, base_url):
    gp = GoodsPage(browser)
    gp.open(base_url, gp.path)
    goods_title = gp.get_goods_title()
    assert len(goods_title) == 1
    thumbnails = gp.get_thumbnails()
    assert len(thumbnails) == 1
    goods_name_breadcrumb = gp.get_goods_name_breadcrumb()
    assert len(goods_name_breadcrumb) == 1
    assert goods_name_breadcrumb[0].text == goods_title[0].text
    tooltip_btn = gp.get_tooltip_btn()
    assert len(tooltip_btn) == 2
    nav_tabs = gp.get_nav_tabs()
    assert len(nav_tabs) == 1


def test_login_page(browser, base_url):
    lp = LoginPage(browser)
    lp.open(base_url, lp.path)
    right_menu = lp.get_right_menu()
    assert len(right_menu) == 1
    register_account_block = lp.get_register_account_block()
    assert len(register_account_block) == 1
    returning_account_block = lp.get_returning_account_block()
    assert len(returning_account_block) == 1
    login_button = lp.get_login_btn()
    assert len(login_button) == 1
    continue_button = lp.get_continue_btn()
    assert len(continue_button) == 1


def test_admin_page(browser, base_url):
    ap = AdminPage(browser)
    ap.open(base_url, ap.path)
    submit_btn = ap.get_submit_btn()
    assert len(submit_btn) == 1
    label_username = ap.get_lbl_username()
    assert len(label_username) == 1
    label_password = ap.get_lbl_pwd()
    assert len(label_password) == 1
    title_panel = ap.get_title_panel()
    assert len(title_panel) == 1
    forgotten_link = ap.get_forgotten_link()
    assert len(forgotten_link) == 1


def test_add_goods(browser, base_url):
    product_name = 'test_product_01'
    ap = AdminPage(browser)
    ap.open(base_url, ap.path)
    ap.login(ADMIN_USER, ADMIN_PWD)
    ap.open_catalog_section()
    before_count_goods = ap.get_count_of_goods()
    assert len(ap.get_products_row()) != 0
    ap.add_new_product(product_name)
    after_count_goods = ap.get_count_of_goods()
    assert int(after_count_goods) == int(before_count_goods) + 1


def test_filter_list_of_products(browser, base_url):
    product_name = 'Product 8'
    ap = AdminPage(browser)
    ap.open(base_url, ap.path)
    ap.login(ADMIN_USER, ADMIN_PWD)
    ap.open_catalog_section()
    assert len(ap.get_products_row()) != 0
    ap.filter_products(product_name)
    prod_name = ap.get_prod_name_from_table_row()
    assert prod_name == product_name
    count_of_goods = len(ap.get_products_row())
    assert count_of_goods == 1
