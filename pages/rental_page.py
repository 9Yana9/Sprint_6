from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import RentPageLocators

class RentPage:
    def __init__(self, driver):
        self.driver = driver
        self.scooter_logo = (By.XPATH, ".//img[@alt='Scooter']")
        self.yandex_logo = (By.XPATH, ".//img[@alt='Yandex']")

    def send_rental_date(self, date):
        rental_date_input = self.driver.find_element(*RentPageLocators.rental_date_field)
        rental_date_input.send_keys(date)
        rental_date_input.send_keys(Keys.ENTER)
        return self

    def set_rental_time(self):
        self.driver.find_element(*RentPageLocators.rental_time_field).click()
        self.driver.find_element(*RentPageLocators.rental_time).click()
        return self

    def click_check_box_colour_black_pearl(self):
        self.driver.find_element(*RentPageLocators.check_box_colour_black_pearl).click()
        return self

    def click_check_box_colour_grey_despair(self):
        self.driver.find_element(*RentPageLocators.check_box_colour_grey_despair).click()
        return self

    def send_comment(self, comment):
        self.driver.find_element(*RentPageLocators.comment_field).send_keys(comment)
        return self

    def click_order_button(self):
        self.driver.find_element(*RentPageLocators.order_button).click()
        return self

    def click_order_button_yes(self):
        self.driver.find_element(*RentPageLocators.order_button_yes).click()
        return self

    def is_modal_order_window_displayed(self):
        return self.driver.find_element(*RentPageLocators.modal_order_window).is_displayed()
