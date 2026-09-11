import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url import MAIN_URL
from locators.main_locators import MainPageLocators


class BasePage():

    def __init__(self, driver):
        self.driver = driver
    
    @allure.step("Открытие страницы")
    def open(self):
        self.driver.get(MAIN_URL)

    @allure.step("Ожидание появления элемента с локатором {locator}")
    def _wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание кликабельности элемента с локатором {locator}")
    def _wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    @allure.step("Кликание по элементу с локатором {locator}")
    def click_element(self, locator, timeout=10):
        self._wait_for_element_to_be_clickable(locator, timeout).click()

    @allure.step("Проверка, что мы на главной странице (URL содержит '{expected_url_substring}')")
    def is_on_main_page(self, expected_url_substring):
        return expected_url_substring in self.driver.current_url
    
    @allure.step("Ввод данных в элемент с локатором {locator}")
    def send_keys_to_element(self, locator, keys, timeout = 10):
        element = self._wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Принятие куки, при наличии")
    def accept_cookies(self):
        try:
            button = self._wait_for_element_to_be_clickable(MainPageLocators.COOKIE_BUTTON)
            button.click()
        except Exception:
            pass
        return self  
    
    @allure.step("Скролл до элемента с локатором {locator}")
    def scroll_to_element(self, locator, timeout=10):
        element = self._wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Скролл до переданного элемента")
    def scroll_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидание видимости всех элементов с локатором {locator}")
    def _wait_for_visibility_of_all_elements(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    @allure.step("Ожидание текста в элементе")
    def _wait_for_text_in_element_value(self, locator, text, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_value(locator, text)
        )

    @allure.step("Ожидание новой вкладки")
    def wait_for_new_tab(self, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda d: len(d.window_handles) > 1,
                   message="После клика не появилась новая вкладка")

    @allure.step("Переключение на последнюю вкладку")
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Содержание подстроки в URL текущей вкладки")
    def wait_url_contains(self, substring, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda d: substring in d.current_url,
                   message=f"URL не содержит '{substring}'")

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url
    