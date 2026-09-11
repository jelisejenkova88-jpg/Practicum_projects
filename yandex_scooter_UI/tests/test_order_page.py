import pytest
import allure

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_locators import OrderPageLocators
from locators.main_locators import MainPageLocators
from url import MAIN_URL, ORDER_URL, DZEN_URL
from pages.base_page import BasePage
from pages.order_page import OrderPage


class TestOrderPage:


    @pytest.mark.parametrize("name,surname,address,station_name,phone_number,date_str, days_text, color_name, comment_text",
                             [("Анна", "Смирнова", "пр. Мира, 10", "Проспект Мира", "89999999999", "30.07.2026", "семеро суток", "чёрный жемчуг", "Позвонить перед приездом"),
                              ("Иван", "Сидоров", "ул. Ленинский проспект, 25", "Тропарёво", "89991110000", "15.08.2026", "сутки", "серая безысходность", "Не звонить и не писать")])
    @allure.title("Позитивный сценарий: заказ через верхнюю кнопку 'Заказать'")
    @allure.description("Проверяет заполнение формы и появление всплывающего окна об успешном заказе.")
    def test_order_via_top_button(self, driver, name, surname, address, station_name, phone_number, date_str, days_text, color_name, comment_text):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.accept_cookies()
        order_page.open_from_main_page(MainPageLocators.HEADER_ORDER_BUTTON)
        order_page.fill_first_order_form(name, surname, address, station_name, phone_number)
        order_page.click_element(OrderPageLocators.SUBMIT_BUTTON)
        order_page.fill_second_order_form(date_str, days_text, color_name, comment_text)
        order_page.click_element(OrderPageLocators.ORDER_BUTTON_IN_FORM)
        message = order_page.complete_order_confirmation()

        assert "Заказ оформлен" in message


    @pytest.mark.parametrize("name,surname,address,station_name,phone_number,date_str, days_text, color_name, comment_text",
                             [("Петр", "Петров", "ул. Профсоюзная, 58", "Профсоюзная", "89995555555", "31.07.2026", "четверо суток", "чёрный жемчуг", "Привезти вечером"),
                              ("Семён", "Семёнов", "ул. Островитяного, 66", "Калужская", "89992222222", "22.08.2026", "двое суток", "серая безысходность", "")])
    @allure.title("Позитивный сценарий: заказ через нижнюю кнопку 'Заказать'")
    @allure.description("Проверяет заполнение формы и появление всплывающего окна об успешном заказе.")
    def test_order_via_bottom_button(self, driver, name, surname, address, station_name, phone_number, date_str, days_text, color_name, comment_text):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.accept_cookies()
        order_page.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        order_page.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        order_page.fill_first_order_form(name, surname, address, station_name, phone_number)
        order_page.click_element(OrderPageLocators.SUBMIT_BUTTON)
        order_page.fill_second_order_form(date_str, days_text, color_name, comment_text)
        order_page.click_element(OrderPageLocators.ORDER_BUTTON_IN_FORM)
        message = order_page.complete_order_confirmation()

        assert "Заказ оформлен" in message


    @allure.title("Проверка клика по логотипу 'Самокат'")
    @allure.description("При клике по логотипу 'Самокат' на главной странице происходит переход на главную страницу сервиса.")
    def test_click_scooter_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.accept_cookies()
        order_page.click_element(MainPageLocators.SCOOTER_LOGO)

        assert order_page.is_on_main_page(MAIN_URL), (f"Ожидался переход на {MAIN_URL}, но текущий URL: {order_page.get_current_url()}")


    @allure.title("Проверка клика по логотипу 'Яндекс'")
    @allure.description("При клике по логотипу 'Яндекс' открывается Дзен в новой вкладке.")
    def test_click_yandex_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.accept_cookies()
        order_page.click_element(MainPageLocators.YANDEX_LOGO)
        order_page.wait_for_new_tab()
        order_page.switch_to_last_tab()
        order_page.wait_url_contains("dzen.ru")

        assert "dzen.ru" in order_page.get_current_url()
