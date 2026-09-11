import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from locators.order_locators import OrderPageLocators
from locators.main_locators import MainPageLocators
from pages.base_page import BasePage
from url import MAIN_URL, ORDER_URL


class OrderPage(BasePage):

    @allure.step("Переход к форме заказа через кнопку {locator}")
    def open_from_main_page(self, locator, timeout=10):
        self._wait_for_element_to_be_clickable(locator, timeout).click()
        self._wait_for_element(OrderPageLocators.ORDER_FORM)

    @allure.step("Клик по станции метро '{station_name}' в выпадающем списке")
    def set_metro_station_by_click(self, station_name):
        input_field = self._wait_for_element_to_be_clickable(OrderPageLocators.METRO_STATION_FIELD)
        input_field.click()
        options = self._wait_for_visibility_of_all_elements(OrderPageLocators.METRO_OPTIONS)
        target_option = None
        for option in options:
            if station_name.lower() in option.text.lower():
                target_option = option
                break
        if target_option is None:
            raise AssertionError(f"Станция '{station_name}' не найдена в списке")
        
        self.scroll_element(target_option)
        target_option.click()

    @allure.step("Заполнение первой формы заказа: {name} {surname}")
    def fill_first_order_form(self, name, surname, address, station_name, phone_number):
        self.send_keys_to_element(OrderPageLocators.NAME_FIELD, name)
        self.send_keys_to_element(OrderPageLocators.SURNAME_FIELD, surname)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD, address)
        self.set_metro_station_by_click(station_name)
        self._wait_for_element_to_be_clickable(OrderPageLocators.PHONE_NUMBER_FIELD)
        self.send_keys_to_element(OrderPageLocators.PHONE_NUMBER_FIELD, phone_number)

    @allure.step("Ввод даты заказа: {date_str}")
    def set_data_by_input(self, date_str: str):
        element = self._wait_for_element(OrderPageLocators.DATE_FIELD)
        element.clear()
        element.send_keys(date_str)
        element.send_keys(Keys.ENTER)
        self._wait_for_text_in_element_value(OrderPageLocators.DATE_FIELD, date_str, timeout=15)

    @allure.step("Выбор периода аренды: {days_text}")        
    def set_rental_period(self, days_text: str):
        rental_field = self._wait_for_element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_FIELD)
        rental_field.click()

        options = self._wait_for_visibility_of_all_elements(OrderPageLocators.DAYS_OPTIONS, timeout=15)
        target_option = None
        search_text = days_text.strip().lower()

        for option in options:
            if search_text in option.text:
                target_option = option
                break
        if target_option is None:
            raise AssertionError(f"Не найдено значение '{days_text}' в списке")
        
        self.scroll_element(target_option)
        target_option.click()

    @allure.step("Выбор цвера самоката: {color_name}")
    def set_color (self, color_name: str):
        color_locators = {"чёрный жемчуг": OrderPageLocators.COLOR_BLACK,
                          "серая безысходность": OrderPageLocators.COLOR_GREY}
        normalized = color_name.lower().strip()
        element = self._wait_for_element_to_be_clickable(color_locators[normalized])
        if not element.is_selected():
            element.click()

    @allure.step("Заполнение второй формы заказа: {date_str} {days_text}")
    def fill_second_order_form(self, date_str: str, days_text: str, color_name: str, comment_text):
        self.set_data_by_input(date_str)
        self.set_rental_period(days_text)
        self.set_color(color_name)
        self.send_keys_to_element(OrderPageLocators.ORDER_COMMENT, comment_text)

    @allure.step("Подтверждение заказа нажатием на кнопку Да")
    def confirm_order_popup(self):
        confirm_button = self._wait_for_element_to_be_clickable(OrderPageLocators.YES_BUTTON)
        confirm_button.click()

    @allure.step("Ожидание сообщения '{expected_text}' в всплывающем окне")
    def wait_for_success_popup(self, expected_text : str = "Заказ оформлен"):
        self._wait_for_element(OrderPageLocators.SUCCESS_ORDER_MESSAGE)

    @allure.step("Получение сообщения об успешном заказе")
    def get_success_order_message(self):
        element = self._wait_for_element(OrderPageLocators.SUCCESS_ORDER_MESSAGE)
        return element.text.strip()

    @allure.step("Завершение оформления заказа: подтверждение, ожидание и получение сообщения")
    def complete_order_confirmation(self):
        self.confirm_order_popup()
        self.wait_for_success_popup()
        return self.get_success_order_message()
