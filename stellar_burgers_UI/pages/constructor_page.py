import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators
from locators.login_locators import LoginLocators


class ConstructorPage(BasePage):

    @allure.step("Проверка, что модальное окно отображается на экране")
    def check_is_modal_visible(self, locator):
        element = self._wait_for_element(locator, timeout = 10)
        return element.is_displayed()

    @allure.step("Проверка, что мы на странице (URL содержит '{expected_url_substring}')")
    def is_on_page(self, expected_url_substring):
        current_url = self.get_current_url()
        return expected_url_substring in current_url
    
    @allure.step("Закрытие модальное окно")
    def close_modal_window(self):
        self.click_element(ConstructorLocators.MODAL_CLOSE_BUTTON)
        self._wait_for_invisibility_of_element_located(ConstructorLocators.MODAL_WINDOW)

    @allure.step("Проверка, что модальное окно исчезло")
    def check_is_modal_invisible(self):
        self._wait_for_invisibility_of_element_located(ConstructorLocators.MODAL_WINDOW)
        return True   

    @allure.step("Перетаскивание ингредиента в зону заказа с помощью JS")
    def drag_ingredient_via_js(self, ingredient_element, order_zone):
        self.drag_via_js(ingredient_element, order_zone)    

    @allure.step("Скролл до зоны заказа")
    def get_order_zone(self):
        self.scroll_to_element(ConstructorLocators.ORDER_ZONE)
        return self._wait_for_element_to_be_clickable(ConstructorLocators.ORDER_ZONE)

    @allure.step("Ожидание увеличения счётчика ингредиентов")
    def wait_for_counter_increase(self, locator, old_count, timeout=15):
        def condition(_):
            return self.get_ingredient_counter_value(locator) > old_count
        self.wait_until(condition, timeout=timeout)
        return self.get_ingredient_counter_value(locator)

    @allure.step("Добавление ингредиента/булки в заказ")
    def add_ingredient_or_bun(self, locator):
        ingredient_element = self._wait_for_element_to_be_clickable(locator)
        order_zone = self.get_order_zone()
        self.drag_ingredient_via_js(ingredient_element, order_zone)

    @allure.step("Получение текущего значения счётчика ингредиентов")
    def get_ingredient_counter_value(self, locator):
        card = self._wait_for_element_to_be_clickable(locator)
        counter_p = self.find_by_tag(card, "p")
        return int(counter_p.text.strip())
    
    @allure.step("Добавление ингредиентов и оформление заказа")
    def add_ingredients_and_place_order(self):
        self.add_ingredient_or_bun(ConstructorLocators.FIRST_BUN)
        self.add_ingredient_or_bun(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        self.add_ingredient_or_bun(ConstructorLocators.FIRST_INGREDIENT_IN_FILING)
        self.click_element(LoginLocators.ORDER_BUTTON)

    @allure.step("Ожидание появления сообщения об успешном оформлении заказа")
    def wait_order_success_message(self, timeout=15):
        self._wait_for_element(ConstructorLocators.ORDER_SUCCESS_MESSAGE) 

    @allure.step("Ожидание появления реального номера заказа")
    def wait_until_real_order_number_appears(self, locator, timeout=20):
        def is_real_number(driver):
            elements = self.find_elements(locator)
            if not elements:
                return False
            return elements[0].text.strip() != "9999"

        self.wait_until(is_real_number, timeout=timeout) 
        return self.find_element(locator).text.strip()
    
    @allure.step("Закрытие модального окна с заказом (JS‑клик для обхода перекрытия)")
    def close_order_modal_window(self):
        close_btn = self._wait_for_element_to_be_clickable(ConstructorLocators.MODAL_CLOSE_BUTTON)
        self.js_click(close_btn)
        self._wait_for_invisibility_of_element_located(ConstructorLocators.ORDER_MODAL_WINDOW, timeout=15)

    @allure.step("Клик по кнопке «Лента заказов» (JS‑клик для обхода перекрытия)")
    def click_order_list_button(self):
        btn = self._wait_for_element_to_be_clickable(ConstructorLocators.ORDER_LIST_BUTTON)
        self.js_click(btn) 
