import pytest
import allure 

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.faq_locators import FaqPageLocators
from pages.faq_page import FaqPage
from pages.base_page import BasePage
from url import MAIN_URL


class TestFaqPage:

    @pytest.mark.parametrize('question_locator,answer_locator, expected_text',
                             [(FaqPageLocators.QUESTION_COST, FaqPageLocators.ANSWER_COST, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
                              (FaqPageLocators.QUESTION_MULTIPLE_ORDERS, FaqPageLocators.ANSWER_MULTIPLE_ORDERS, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
                              (FaqPageLocators.QUESTION_RENTAL_TIME, FaqPageLocators.ANSWER_RENTAL_TIME, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
                              (FaqPageLocators.QUESTION_ORDER_TODAY, FaqPageLocators.ANSWER_ORDER_TODAY, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
                              (FaqPageLocators.QUESTION_ORDER_EXTENSION, FaqPageLocators.ANSWER_ORDER_EXTENSION, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
                              (FaqPageLocators.QUESTION_CHARGER, FaqPageLocators.ANSWER_CHARGER, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
                              (FaqPageLocators.QUESTION_ORDER_CANCELLATION, FaqPageLocators.ANSWER_ORDER_CANCELLATION, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
                              (FaqPageLocators.QUESTION_DELIVERY_OUTSIDE_MKAD, FaqPageLocators.ANSWER_DELIVERY_OUTSIDE_MKAD, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
                              ],
                              ids = [
                                  "cost",
                                  "multiple_orders",
                                  "rental_time",
                                  "order_today",
                                  "order_extension",
                                  "charger",
                                  "order_cancellation",
                                  "delivery_outside_mkad"
                              ]
                              )
    @allure.title("FAQ: ответ на вопрос '{ids}' соответствует ожидаемому")
    @allure.description("Проверка, что при клике на вопрос в разделе FAQ ответ раскрывается и текст ответа точно совпадает с эталонным (из тестовых данных).")       
    def test_faq_question_opens_and_shows_correct_answer(self, driver, question_locator, answer_locator, expected_text):
        faq_page = FaqPage(driver)
        faq_page.open()
        faq_page.accept_cookies()
        faq_page.scroll_to_element(FaqPageLocators.FAQ_SECTION)
        faq_page.open_question_and_wait_answer(question_locator, answer_locator)
        answer_text = faq_page.get_text_from_element(answer_locator)
        assert answer_text == expected_text
    
        