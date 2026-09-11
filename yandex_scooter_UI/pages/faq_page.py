import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url import MAIN_URL
from locators.faq_locators import FaqPageLocators
from pages.base_page import BasePage


class FaqPage(BasePage):

    @allure.step("Получение текста элемента с локатором {locator}")
    def get_text_from_element(self, locator, timeout=10):
        return self._wait_for_element(locator, timeout).text
    
    @allure.step("Проверка, что ответ стал видимым")
    def check_is_answer_visible(self, answer_locator, timeout=10):
        try:
            element = self._wait_for_element(answer_locator, timeout)
            return element.is_displayed()
        except TimeoutError:
            return False

    @allure.step("Проверка открытия вопроса с локатором {question_locator} и ожидания ответа с локатором {answer_locator}")
    def open_question_and_wait_answer(self, question_locator, answer_locator, timeout=10):
        self.click_element(question_locator, timeout)
        return self.check_is_answer_visible(answer_locator, timeout)

