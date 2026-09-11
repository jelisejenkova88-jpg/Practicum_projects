from selenium.webdriver.common.by import By


class LoginLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    EMAIL_FIELD = (By.XPATH,".//div[label[text()='Email']]/input") 
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти')] ")
    ORDER_BUTTON = (By.XPATH, ".//div/button[text()='Оформить заказ']") 
    