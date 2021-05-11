from pages import MainPage, AdminPage, CatalogPage, GoodsPage, LoginPage
import allure

ADMIN_USER = 'user'
ADMIN_PWD = 'bitnami'


def test_open_main_page(browser, base_url, generate_env):
    mp = MainPage(browser)
    with allure.step("Открываем главную страницу"):
        mp.open(base_url, mp.path)
    mp.logger.info("Сравниваем заголовок страницы с эталоном")
    with allure.step("Проверяем заголовок"):
        assert mp.get_title() == 'Your Store'
    with allure.step("Проверяем ссылку на OpenCart"):
        assert mp.get_link_powered_by_text() == 'OpenCart'


def test_main_page(browser, base_url):
    mp = MainPage(browser)
    with allure.step("Открываем главную страницу"):
        mp.open(base_url, mp.path)
    with allure.step("Проверяем наличие карусели товаров"):
        assert mp.get_main_carousel()
    with allure.step("Проверяем наличие логотипа"):
        assert mp.get_logo()
    with allure.step("Проверяем наличие строки поиска"):
        assert mp.get_search_field()
    with allure.step("Проверяем наличие заголовка товаров"):
        assert mp.get_head_featured_goods()
    with allure.step("Проверяем наличие товаров"):
        assert mp.get_featured_goods()


def test_catalog_page(browser, base_url):
    cp = CatalogPage(browser)
    with allure.step(f"Открываем страницу каталога по адресу {cp.path}"):
        cp.open(base_url, cp.path)
    cp.logger.info("Запоминаем количество товаров")
    with allure.step("Получаем товары со страницы"):
        goods = cp.get_goods()
    with allure.step("Проверяем кол-во товаров на странице"):
        assert len(cp.get_goods()) == 12
    with allure.step("Проверяем отображение кол-ва товаров"):
        assert cp.get_text_of_goods()
    with allure.step("Проверяем корректность отображения"):
        text_of_goods = cp.get_text_of_goods()[0].text.split(" ")
        assert int(text_of_goods[5]) == len(goods)
    with allure.step("Проверяем копирайт"):
        copyright_text = cp.get_copyright_text()
        assert copyright_text[0].text == 'Powered By OpenCart\nYour Store © 2021'
    with allure.step("Проверяем наличие кнопок отображения"):
        button_view = cp.get_btn_view()
        assert len(button_view) == 2


def test_goods_page(browser, base_url):
    gp = GoodsPage(browser)
    with allure.step("Открываем страницу товара"):
        gp.open(base_url, gp.path)
    with allure.step("Проверяем название товара"):
        goods_title = gp.get_goods_title()
        assert goods_title
    with allure.step("Проверяем наличие эскизов"):
        assert gp.get_thumbnails()
    with allure.step("Проверяем \"Хлебные крошки\""):
        goods_name_breadcrumb = gp.get_goods_name_breadcrumb()
        assert gp.get_goods_name_breadcrumb()
        assert goods_name_breadcrumb[0].text == goods_title[0].text
    with allure.step("Проверяем кнопки подсказки"):
        tooltip_btn = gp.get_tooltip_btn()
        assert len(tooltip_btn) == 2
    with allure.step("Проверяем навигационные вкладки"):
        assert gp.get_nav_tabs()


def test_login_page(browser, base_url):
    lp = LoginPage(browser)
    with allure.step("Открываем страницу с формой входа"):
        lp.open(base_url, lp.path)
    with allure.step("Проверяем наличие правого меню"):
        assert lp.get_right_menu()
    with allure.step("Проверяем форму для регистрации нового пользователя"):
        assert lp.get_register_account_block()
    with allure.step("Проверяем форму авторизации"):
        assert lp.get_returning_account_block()
    with allure.step("Проверяем кнопку \"Login\""):
        assert lp.get_login_btn()
    with allure.step("Проверяем кнопку \"Continue\""):
        assert lp.get_continue_btn()


def test_admin_page(browser, base_url):
    ap = AdminPage(browser)
    with allure.step("Открываем страницу авторизации в админку"):
        ap.open(base_url, ap.path)
    with allure.step("Проверяем кнопку \"Войти\""):
        assert ap.get_submit_btn()
    with allure.step("Проверяем подпись для поля Юзернейм"):
        assert ap.get_lbl_username()
    with allure.step("Проверяем подпись для поля Пароль"):
        assert ap.get_lbl_pwd()
    with allure.step("Проверяем заголовок формы"):
        assert ap.get_title_panel()
    with allure.step("Проверяем линк на восстановление забытого пароля"):
        assert ap.get_forgotten_link()


def test_add_goods(browser, base_url):
    product_name = 'test_product_01'
    ap = AdminPage(browser)
    with allure.step("Открываем страницу авторизации в админку"):
        ap.open(base_url, ap.path)
    with allure.step("Авторизуемся"):
        ap.login(ADMIN_USER, ADMIN_PWD)
    with allure.step("Переходим на страницу редактирования каталога"):
        ap.open_catalog_section()
    before_count_goods = ap.get_count_of_goods()
    with allure.step("Проверяем отображение товаров в таблице"):
        assert ap.get_products_row()
    with allure.step("Добавляем новый товар"):
        ap.add_new_product(product_name)
    after_count_goods = ap.get_count_of_goods()
    with allure.step("Проверяем, что товар добавился"):
        assert int(after_count_goods) == int(before_count_goods) + 1


def test_filter_list_of_products(browser, base_url):
    product_name = 'Product 8'
    ap = AdminPage(browser)
    with allure.step("Открываем страницу авторизации в админку"):
        ap.open(base_url, ap.path)
    with allure.step("Авторизуемся"):
        ap.login(ADMIN_USER, ADMIN_PWD)
    with allure.step("Переходим на страницу редактирования каталога"):
        ap.open_catalog_section()
    with allure.step("Проверяем отображение товаров в таблице"):
        assert ap.get_products_row()
    with allure.step(f"Фильтруем товары по имени: {product_name}"):
        ap.filter_products(product_name)
    with allure.step("Проверяем что найден один товар"):
        prod_name = ap.get_prod_name_from_table_row()
        assert prod_name == product_name
        count_of_goods = len(ap.get_products_row())
        assert count_of_goods == 1
