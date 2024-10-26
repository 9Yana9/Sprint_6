from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.rental_page import RentPage

class TestOrdering:

    def test_ordering_by_header_order_button(self, setup):
        driver = setup  # Получаем драйвер из фикстуры
        main_page = MainPage(driver)
        main_page.open_site()\
                  .click_cookie_button()\
                  .click_header_order_button()

        order_page = OrderPage(driver)
        order_page.send_client_first_name("аааа")\
                  .send_client_last_name("ааааа")\
                  .send_delivery_address("Москва, Образцова, 11")\
                  .select_metro_station("Лубянка")\
                  .send_delivery_client_phone_number("88888888888")\
                  .click_next_button()

        rent_page = RentPage(driver)
        is_displayed = rent_page.send_rental_date("24.10.2024")\
                                 .set_rental_time()\
                                 .click_check_box_colour_black_pearl()\
                                 .send_comment("ааааа")\
                                 .click_order_button()\
                                 .click_order_button_yes()\
                                 .is_modal_order_window_displayed()

        assert is_displayed, "Окно заказа не отображается, не удалось оформить заказ."

    def test_samokat_ordering_by_middle_order_button(self, setup):
        driver = setup  # Получаем драйвер из фикстуры
        main_page = MainPage(driver)
        main_page.open_site()\
                  .click_cookie_button()\
                  .click_middle_order_button()

        order_page = OrderPage(driver)
        order_page.send_client_first_name("ббббб")\
                  .send_client_last_name("ббббб")\
                  .send_delivery_address("Москва, Дербеневская, 16")\
                  .select_metro_station("Павелецкая")\
                  .send_delivery_client_phone_number("88888888888")\
                  .click_next_button()

        rent_page = RentPage(driver)
        is_displayed = rent_page.send_rental_date("07.01.2023")\
                                 .set_rental_time()\
                                 .click_check_box_colour_grey_despair()\
                                 .send_comment("ббббб")\
                                 .click_order_button()\
                                 .click_order_button_yes()\
                                 .is_modal_order_window_displayed()

        assert is_displayed, "Окно заказа не отображается, не удалось оформить заказ."









