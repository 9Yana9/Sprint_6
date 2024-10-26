from selenium.webdriver.common.by import By

class RentPageLocators:
    RENTAL_DATE_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENTAL_TIME_FIELD = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_TIME = (By.XPATH, ".//*[(@role ='option' and text()='трое суток')]")
    CHECK_BOX_COLOUR_BLACK_PEARL = (By.XPATH, ".//input[@id='black']")
    CHECK_BOX_COLOUR_GREY_DESPAIR = (By.XPATH, ".//input[@id='grey']")
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//button[(@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать')]")
    ORDER_BUTTON_YES = (By.XPATH, ".//button[text()='Да']")
    MODAL_ORDER_WINDOW = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")

class OrderPageLocators:
    CLIENT_FIRST_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    CLIENT_LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    DELIVERY_ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    DELIVERY_METRO_STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    DELIVERY_CLIENT_PHONE_NUMBER = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    HEADER_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    MIDDLE_ORDER_BUTTON = (By.CLASS_NAME, "Button_Middle__1CSJM")

    DROP_DOWN_QUESTIONS_ARRAY = [
        "accordion__heading-0", "accordion__heading-1", "accordion__heading-2", "accordion__heading-3",
        "accordion__heading-4", "accordion__heading-5", "accordion__heading-6", "accordion__heading-7"
    ]

    DROP_DOWN_ANSWERS_ARRAY = [
        "accordion__panel-0", "accordion__panel-1", "accordion__panel-2", "accordion__panel-3",
        "accordion__panel-4", "accordion__panel-5", "accordion__panel-6", "accordion__panel-7"
    ]