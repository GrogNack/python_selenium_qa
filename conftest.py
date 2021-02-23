import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox"], default="chrome", help="Browser")
    parser.addoption("--maximized", action="store_true", help="Full screen browser window")
    parser.addoption("--headless", action="store_true", help="Headless")
    parser.addoption("--URL", action="store", default="http://localhost", help="Base url for web site")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    maximized = request.config.getoption("--maximized")
    headless = request.config.getoption("--headless")
    driver = None

    def teardown():
        driver.close()

    request.addfinalizer(teardown)

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(options=options)
    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)

    if maximized:
        driver.maximize_window()

    return driver


@pytest.fixture
def base_url(request):
    return request.config.getoption("--URL")
