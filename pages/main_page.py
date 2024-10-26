from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_cookie_button(self):
        self.driver.find_element(*MainPageLocators.COOKIE_BUTTON).click()
        return self  # Возвращаем self для поддержки цепочек вызовов

    def click_header_order_button(self):
        self.driver.find_element(*MainPageLocators.HEADER_ORDER_BUTTON).click()
        return self  # Возвращаем self для поддержки цепочек вызовов

    def click_middle_order_button(self):
        self.driver.find_element(*MainPageLocators.MIDDLE_ORDER_BUTTON).click()
        return self  # Возвращаем self для поддержки цепочек вызовов

    def scroll_page_to_end_of_list(self):
        last_question_arrow = self.driver.find_element(By.ID, MainPageLocators.DROP_DOWN_QUESTIONS_ARRAY[7])
        self.driver.execute_script("arguments[0].scrollIntoView();", last_question_arrow)
        return self

    def click_question_arrow(self, question_number):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, MainPageLocators.DROP_DOWN_QUESTIONS_ARRAY[question_number])))
        self.driver.find_element(By.ID, MainPageLocators.DROP_DOWN_QUESTIONS_ARRAY[question_number]).click()

    def check_text_in_open_panel(self, expected_text, answer_number):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, MainPageLocators.DROP_DOWN_QUESTIONS_ARRAY[answer_number])))
        answer_text = self.driver.find_element(By.ID, MainPageLocators.DROP_DOWN_QUESTIONS_ARRAY[answer_number]).text
        assert expected_text == answer_text, f"Expected {expected_text}, but got {answer_text}"

    def click_question_button(self, question_locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, question_locator)))
        self.driver.find_element(By.ID, question_locator).click()

    def get_text_in_open_panel(self, i):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, MainPageLocators.DROP_DOWN_QUESTIONS_ARRAY[i])))
        return self.driver.find_element(By.ID, MainPageLocators.DROP_DOWN_QUESTIONS_ARRAY[i]).text

