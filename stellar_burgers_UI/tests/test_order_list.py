import allure
from locators.order_list_locators import OrderListLocators
from locators.constructor_locators import ConstructorLocators
from pages.constructor_page import ConstructorPage
from pages.order_list_page import OrderListPage
from url import MAIN_URL, ORDER_LIST_URL


class TestOrderListPage:

    @allure.title("Счётчик общих заказов увеличивается на 1 после оформления одного заказа")
    @allure.description("Тест проверяет, что после успешного оформления одного заказа (добавление ингредиентов, размещение заказа, подтверждение) значение общего счётчика заказов на странице списка заказов увеличивается ровно на 1 по сравнению с исходным значением.")
    def test_total_orders_counter_increases_by_one_after_single_order(self, authorized_driver):
        driver = authorized_driver
        order_page = OrderListPage(driver)
        constructor_page = ConstructorPage(driver)
        order_page.open(ORDER_LIST_URL)
        before_count = order_page.get_completed_counter(OrderListLocators.LOCATOR_TOTAL_COUNTER)
        constructor_page.open(MAIN_URL)
        constructor_page.add_ingredients_and_place_order()
        constructor_page.wait_order_success_message()
        constructor_page.wait_until_real_order_number_appears(ConstructorLocators.ORDER_NUMBER)
        constructor_page.close_order_modal_window()
        order_page.open(ORDER_LIST_URL)
        order_page._wait_for_element(OrderListLocators.LOCATOR_TOTAL_COUNTER, timeout=30)
        after_count = order_page.get_completed_counter(OrderListLocators.LOCATOR_TOTAL_COUNTER)
        expected_count = before_count + 1
        assert after_count == expected_count

    @allure.title("Счётчик сегодняшних заказов увеличивается на 1 после оформления одного заказа")
    @allure.description("Тест проверяет, что после успешного оформления одного заказа значение счётчика «сегодняшних» заказов на странице списка заказов увеличивается ровно на 1 по сравнению с исходным значением.")
    def test_today_orders_counter_increases_by_one_after_single_order(self, authorized_driver):
        driver = authorized_driver
        order_page = OrderListPage(driver)
        constructor_page = ConstructorPage(driver)
        order_page.open(ORDER_LIST_URL)
        order_page.scroll_to_element(OrderListLocators.LOCATOR_TODAY_COUNTER)
        before_count = order_page.get_completed_counter(OrderListLocators.LOCATOR_TODAY_COUNTER)
        constructor_page.open(MAIN_URL)
        constructor_page.add_ingredients_and_place_order()
        constructor_page.wait_order_success_message()
        constructor_page.wait_until_real_order_number_appears(ConstructorLocators.ORDER_NUMBER)
        constructor_page.close_order_modal_window()
        order_page.open(ORDER_LIST_URL)
        order_page.scroll_to_element(OrderListLocators.LOCATOR_TODAY_COUNTER)
        order_page._wait_for_element(OrderListLocators.LOCATOR_TODAY_COUNTER, timeout=30)
        after_count = order_page.get_completed_counter(OrderListLocators.LOCATOR_TODAY_COUNTER)
        expected_count = before_count + 1
        assert after_count == expected_count

    @allure.title("Заказ отображается в секции «В работе» после оформления")
    @allure.description("Тест проверяет, что после успешного оформления заказа он появляется в секции «В работе» на странице списка заказов — подтверждается наличием соответствующего элемента на странице.")
    def test_order_appears_in_section_in_progress(self, authorized_driver):
        driver = authorized_driver
        order_page = OrderListPage(driver)
        constructor_page = ConstructorPage(driver)
        constructor_page.open(MAIN_URL)
        constructor_page.add_ingredients_and_place_order()
        constructor_page.wait_order_success_message()
        constructor_page.wait_until_real_order_number_appears(ConstructorLocators.ORDER_NUMBER)
        constructor_page.close_order_modal_window()
        order_page.open(ORDER_LIST_URL)
        order_page._wait_for_element(OrderListLocators.ORDER_IN_PROGRESS)
        assert True
