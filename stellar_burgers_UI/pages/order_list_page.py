import allure
from pages.base_page import BasePage


class OrderListPage(BasePage):
    
    @allure.step("Получение значения счётчика выполненных заказов")
    def get_completed_counter(self, locator):
        element = self._wait_for_element(locator)
        text = element.text.strip()
        digits = ''.join(filter(str.isdigit, text))
        return int(digits)
    