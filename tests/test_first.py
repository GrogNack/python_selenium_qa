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
    assert mp.get_main_carousel()
    assert mp.get_logo()
    assert mp.get_search_field()
    assert mp.get_head_featured_goods()
    assert mp.get_featured_goods()


def test_catalog_page(browser, base_url):
    cp = CatalogPage(browser)
    cp.open(base_url, cp.path)
    goods = cp.get_goods()
    assert len(cp.get_goods()) == 12
    assert cp.get_text_of_goods()
    text_of_goods = cp.get_text_of_goods()[0].text.split(" ")
    assert int(text_of_goods[5]) == len(goods)
    copyright_text = cp.get_copyright_text()
    assert copyright_text[0].text == 'Powered By OpenCart\nYour Store © 2021'
    button_view = cp.get_btn_view()
    assert len(button_view) == 2


def test_goods_page(browser, base_url):
    gp = GoodsPage(browser)
    gp.open(base_url, gp.path)
    goods_title = gp.get_goods_title()
    assert goods_title
    assert gp.get_thumbnails()
    goods_name_breadcrumb = gp.get_goods_name_breadcrumb()
    assert gp.get_goods_name_breadcrumb()
    assert goods_name_breadcrumb[0].text == goods_title[0].text
    tooltip_btn = gp.get_tooltip_btn()
    assert len(tooltip_btn) == 2
    assert gp.get_nav_tabs()


def test_login_page(browser, base_url):
    lp = LoginPage(browser)
    lp.open(base_url, lp.path)
    assert lp.get_right_menu()
    assert lp.get_register_account_block()
    assert lp.get_returning_account_block()
    assert lp.get_login_btn()
    assert lp.get_continue_btn()


def test_admin_page(browser, base_url):
    ap = AdminPage(browser)
    ap.open(base_url, ap.path)
    assert ap.get_submit_btn()
    assert ap.get_lbl_username()
    assert ap.get_lbl_pwd()
    assert ap.get_title_panel()
    assert ap.get_forgotten_link()


def test_add_goods(browser, base_url):
    product_name = 'test_product_01'
    ap = AdminPage(browser)
    ap.open(base_url, ap.path)
    ap.login(ADMIN_USER, ADMIN_PWD)
    ap.open_catalog_section()
    before_count_goods = ap.get_count_of_goods()
    assert ap.get_products_row()
    ap.add_new_product(product_name)
    after_count_goods = ap.get_count_of_goods()
    assert int(after_count_goods) == int(before_count_goods) + 1


def test_filter_list_of_products(browser, base_url):
    product_name = 'Product 8'
    ap = AdminPage(browser)
    ap.open(base_url, ap.path)
    ap.login(ADMIN_USER, ADMIN_PWD)
    ap.open_catalog_section()
    assert ap.get_products_row()
    ap.filter_products(product_name)
    prod_name = ap.get_prod_name_from_table_row()
    assert prod_name == product_name
    count_of_goods = len(ap.get_products_row())
    assert count_of_goods == 1
