# locators.py

from selenium.webdriver.common.by import By

class RentPageLocators:
    rental_date_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    rental_time_field = (By.CLASS_NAME, "Dropdown-placeholder")
    rental_time = (By.XPATH, ".//*[(@role ='option' and text()='трое суток')]")
    check_box_colour_black_pearl = (By.XPATH, ".//input[@id='black']")
    check_box_colour_grey_despair = (By.XPATH, ".//input[@id='grey']")
    comment_field = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, ".//button[(@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать')]")
    order_button_yes = (By.XPATH, ".//*[@id='root']/div/div[2]/div[5]/div[2]/button[2]")
    modal_order_window = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")

class OrderPageLocators:
    client_first_name = (By.XPATH, ".//input[@placeholder='* Имя']")
    client_last_name = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    delivery_address = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    delivery_metro_station = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    delivery_client_phone_number = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, ".//button[(@class ='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее')]")

class MainPageLocators:
    cookie_button = (By.ID, "rcc-confirm-button")
    header_order_button = (By.CLASS_NAME, "Button_Button__ra12g")
    middle_order_button = (By.CLASS_NAME, "Button_Middle__1CSJM")

    drop_down_questions_array = [
        "accordion__heading-0", "accordion__heading-1", "accordion__heading-2", "accordion__heading-3",
        "accordion__heading-4", "accordion__heading-5", "accordion__heading-6", "accordion__heading-7"
    ]

    drop_down_answers_array = [
        "accordion__panel-0", "accordion__panel-1", "accordion__panel-2", "accordion__panel-3",
        "accordion__panel-4", "accordion__panel-5", "accordion__panel-6", "accordion__panel-7"
    ]