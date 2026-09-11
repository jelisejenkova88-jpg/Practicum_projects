from selenium.webdriver.common.by import By


class OrderListLocators:
    LOCATOR_TOTAL_COUNTER = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p[1]")
    LOCATOR_TODAY_COUNTER = (By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[1]")
    ORDER_IN_PROGRESS = (By.XPATH, "//div/p[text() = 'В работе:']/following-sibling::ul[2]/li")
