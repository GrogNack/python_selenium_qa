class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url, path=''):
        self.driver.get(url + path)
