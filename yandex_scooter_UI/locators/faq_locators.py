from selenium.webdriver.common.by import By


class FaqPageLocators():
    FAQ_SECTION = (By.CSS_SELECTOR, ".accordion") # Секция с важными вопросами
    
    QUESTION_COST = (By.ID, "accordion__heading-0") # Вопрос - цена и оплата
    ANSWER_COST = (By.ID, "accordion__panel-0") # Ответ - цена и оплата

    QUESTION_MULTIPLE_ORDERS = (By.ID, "accordion__heading-1") # Вопрос - аренда нескольких самокатов
    ANSWER_MULTIPLE_ORDERS = (By.ID, "accordion__panel-1") # Ответ - аренда нескольких самокатов

    QUESTION_RENTAL_TIME = (By.ID, "accordion__heading-2") # Вопрос - время аренды
    ANSWER_RENTAL_TIME = (By.ID, "accordion__panel-2") # Ответ - время аренды

    QUESTION_ORDER_TODAY = (By.ID, "accordion__heading-3") # Вопрос - заказать сегодня
    ANSWER_ORDER_TODAY = (By.ID, "accordion__panel-3") # Ответ - заказать сегодня

    QUESTION_ORDER_EXTENSION = (By.ID, "accordion__heading-4") # Вопрос - возврат
    ANSWER_ORDER_EXTENSION = (By.ID, "accordion__panel-4") # Ответ - возврат

    QUESTION_CHARGER = (By.ID, "accordion__heading-5") # Вопрос - зарядка
    ANSWER_CHARGER = (By.ID, "accordion__panel-5") # Ответ - зарадка

    QUESTION_ORDER_CANCELLATION = (By.ID, "accordion__heading-6") # Вопрос - отмена заказа
    ANSWER_ORDER_CANCELLATION = (By.ID, "accordion__panel-6") # Ответ - отмена заказа

    QUESTION_DELIVERY_OUTSIDE_MKAD = (By.ID, "accordion__heading-7") # Вопрос - доставка за МКАД
    ANSWER_DELIVERY_OUTSIDE_MKAD = (By.ID, "accordion__panel-7")  # Ответ - доставка за МКАД
