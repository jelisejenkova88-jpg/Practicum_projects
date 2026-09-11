from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button") # Куки
    HEADER_ORDER_BUTTON = (By.XPATH, './/div[contains(@class, "Header_Nav")]//button[contains(text(), "Заказать")]') # Верхняя кнопка "Закаать"
    BOTTOM_ORDER_BUTTON = (By.XPATH, './/div[contains(@class, "Home_FinishButton")]//button[contains(text(), "Заказать")]') # Нижняя кнопка "Заказать"

    SCOOTER_LOGO = (By.XPATH, './/a[@href="/"]') # Лого Самокат
    YANDEX_LOGO = (By.XPATH, './/a[@href ="//yandex.ru"]') # Лого Яндекс
    