from pages.base_page import BasePage  # Импортируем базовый класс
from selenium.webdriver.common.keys import Keys
from locators import OrderPageLocators

class OrderPage(BasePage):  # Наследуемся от BasePage
    def __init__(self, driver):
        super().__init__(driver)  # Вызываем конструктор базового класса

    def send_client_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.CLIENT_FIRST_NAME).send_keys(first_name)
        return self

    def send_client_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.CLIENT_LAST_NAME).send_keys(last_name)
        return self

    def send_delivery_address(self, address):
        self.driver.find_element(*OrderPageLocators.DELIVERY_ADDRESS).send_keys(address)
        return self

    def select_metro_station(self, metro_station):
        metro_input = self.driver.find_element(*OrderPageLocators.DELIVERY_METRO_STATION)
        metro_input.click()
        metro_input.send_keys(metro_station)
        metro_input.send_keys(Keys.DOWN, Keys.ENTER)
        return self

    def send_delivery_client_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.DELIVERY_CLIENT_PHONE_NUMBER).send_keys(phone_number)
        return self

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()
        return self
