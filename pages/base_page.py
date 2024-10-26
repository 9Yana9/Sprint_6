from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import BASE_URL

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_site(self, url=BASE_URL):
        self.driver.get(url)
        return self  # Возвращаем self для поддержки цепочек вызовов

    def wait_until_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def wait_until_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

