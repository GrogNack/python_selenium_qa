import allure
import pytest, logging

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

FORMAT = '%(name)s : %(asctime)-15s : %(filename)s : %(levelname)s : %(message)s'
logging.basicConfig(level=logging.INFO, filename="logs/test.log", format=FORMAT)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--bver", action="store", default="89.0")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--maximized", action="store_true", default=False)
    parser.addoption("--URL", action="store", default="http://demo-opencart.ru", help="Base url for web site")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bver")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    maximized = request.config.getoption("--maximized")

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": browser,
        "browserVersion": version,
        "screenResolution": "1280x720",
        "name": "mkazantsev",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs
        },
        'acceptSslCerts': True,
        'acceptInsecureCerts': True,
        'timeZone': 'Europe/Moscow',
        'goog:chromeOptions': {
            'args': []
        }
    }

    driver = EventFiringWebDriver(webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps
    ), ExceptionListener())

    def fin():
        driver.quit()

    if maximized:
        driver.maximize_window()

    request.addfinalizer(fin)
    return driver


@pytest.fixture
def base_url(request):
    return request.config.getoption("--URL")


@pytest.fixture(scope="session")
def generate_env(request):
    with open("allure-results/environment.properties", "w") as f:
        f.writelines("Browser=" + request.config.getoption("--browser") + "\n")
        f.writelines("Browser.Version=" + request.config.getoption("--bver") + "\n")
        f.writelines("Stand=" + request.config.getoption("--URL") + "\n")


class ExceptionListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        allure.attach(driver.get_screenshot_as_png(), name="Скриншот ошибки.png", attachment_type=AttachmentType.PNG)
        logging.error(exception)

    def after_navigate_to(self, url, driver):
        allure.attach(driver.get_screenshot_as_png(), name=f"Переход на {url}", attachment_type=AttachmentType.PNG)
