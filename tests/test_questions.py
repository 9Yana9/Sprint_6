import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from parameterized import parameterized
from pages.main_page import MainPage

class DropDownListParamTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.main_page = MainPage(self.driver)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand([
        ("accordion__heading-0", "accordion__panel-0", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        ("accordion__heading-1", "accordion__panel-1", "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        ("accordion__heading-2", "accordion__panel-2", "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        ("accordion__heading-3", "accordion__panel-3", "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        ("accordion__heading-4", "accordion__panel-4", "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        ("accordion__heading-5", "accordion__panel-5", "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        ("accordion__heading-6", "accordion__panel-6", "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        ("accordion__heading-7", "accordion__panel-7", "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    def test_drop_down_list(self, question_locator, answer_locator, expected_answer):
        self.main_page.open_site()
        self.main_page.click_cookie_button()
        self.main_page.scroll_page_to_end_of_list()
        self.main_page.click_question_button(question_locator)

        actual_answer_text = self.driver.find_element(By.ID, answer_locator).text
        self.assertEqual(expected_answer, actual_answer_text, "Текст в ответе не соответствует ожидаемому тексту.")

if __name__ == '__main__':
    unittest.main()
