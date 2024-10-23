from selenium.webdriver.common.keys import Keys
from locators import OrderPageLocators

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def send_client_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.client_first_name).send_keys(first_name)
        return self

    def send_client_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.client_last_name).send_keys(last_name)
        return self

    def send_delivery_address(self, address):
        self.driver.find_element(*OrderPageLocators.delivery_address).send_keys(address)
        return self

    def select_metro_station(self, metro_station):
        metro_input = self.driver.find_element(*OrderPageLocators.delivery_metro_station)
        metro_input.click()
        metro_input.send_keys(metro_station)
        metro_input.send_keys(Keys.DOWN, Keys.ENTER)
        return self

    def send_delivery_client_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.delivery_client_phone_number).send_keys(phone_number)
        return self

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()
        return self