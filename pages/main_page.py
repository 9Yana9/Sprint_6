from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_site(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        return self

    def click_cookie_button(self):
        self.driver.find_element(*MainPageLocators.cookie_button).click()
        return self

    def click_header_order_button(self):
        self.driver.find_element(*MainPageLocators.header_order_button).click()
        return self

    def click_middle_order_button(self):
        self.driver.find_element(*MainPageLocators.middle_order_button).click()
        return self

    def scroll_page_to_end_of_list(self):
        last_question_arrow = self.driver.find_element(By.ID, MainPageLocators.drop_down_questions_array[7])
        self.driver.execute_script("arguments[0].scrollIntoView();", last_question_arrow)
        return self

    def click_question_arrow(self, question_number):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, MainPageLocators.drop_down_questions_array[question_number])))
        self.driver.find_element(By.ID, MainPageLocators.drop_down_questions_array[question_number]).click()

    def check_text_in_open_panel(self, expected_text, answer_number):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, MainPageLocators.drop_down_answers_array[answer_number])))
        answer_text = self.driver.find_element(By.ID, MainPageLocators.drop_down_answers_array[answer_number]).text
        assert expected_text == answer_text, f"Expected {expected_text}, but got {answer_text}"

    def click_question_button(self, question_locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, question_locator)))
        self.driver.find_element(By.ID, question_locator).click()

    def get_text_in_open_panel(self, i):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, MainPageLocators.drop_down_answers_array[i])))
        return self.driver.find_element(By.ID, MainPageLocators.drop_down_answers_array[i]).text