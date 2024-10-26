from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage  # Импортируем базовый класс
from locators import RentPageLocators

class RentPage(BasePage):  # Наследуемся от BasePage
    def __init__(self, driver):
        super().__init__(driver)  # Вызываем конструктор базового класса
        self.scooter_logo = (By.XPATH, ".//img[@alt='Scooter']")
        self.yandex_logo = (By.XPATH, ".//img[@alt='Yandex']")

    def send_rental_date(self, date):
        rental_date_input = self.driver.find_element(*RentPageLocators.RENTAL_DATE_FIELD)
        rental_date_input.send_keys(date)
        rental_date_input.send_keys(Keys.ENTER)
        return self

    def set_rental_time(self):
        self.driver.find_element(*RentPageLocators.RENTAL_TIME_FIELD).click()
        self.driver.find_element(*RentPageLocators.RENTAL_TIME).click()
        return self

    def click_check_box_colour_black_pearl(self):
        self.driver.find_element(*RentPageLocators.CHECK_BOX_COLOUR_BLACK_PEARL).click()
        return self

    def click_check_box_colour_grey_despair(self):
        self.driver.find_element(*RentPageLocators.CHECK_BOX_COLOUR_GREY_DESPAIR).click()
        return self

    def send_comment(self, comment):
        self.driver.find_element(*RentPageLocators.COMMENT_FIELD).send_keys(comment)
        return self

    def click_order_button(self):
        self.driver.find_element(*RentPageLocators.ORDER_BUTTON).click()
        return self

    def click_order_button_yes(self):
        self.driver.find_element(*RentPageLocators.ORDER_BUTTON_YES).click()
        return self

    def is_modal_order_window_displayed(self):
        return self.driver.find_element(*RentPageLocators.MODAL_ORDER_WINDOW).is_displayed()
