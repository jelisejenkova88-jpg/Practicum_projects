from selenium.webdriver.common.by import By


class ConstructorLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']") 
    ORDER_LIST_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    SAUCES_SECTION = (By.XPATH, "//h2[normalize-space()='Соусы']")
    
    FIRST_INGREDIENT_IN_SAUCES = (By.XPATH, "//h2[normalize-space()='Соусы']/following-sibling::ul[1]//a[1]") 
    SECOND_INGREDIENT_IN_SAUCES = (By.XPATH, "//h2[normalize-space()='Соусы']/following-sibling::ul[1]//a[2]")
    INGREDIENTS_IN_ORDER = (By.CSS_SELECTOR, "section ul li[draggable='true']")
    ORDER_ZONE = (By.CSS_SELECTOR, "ul[class*='basket']")

    MODAL_WINDOW = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    ORDER_MODAL_WINDOW = (By.XPATH, ".//p[text()='идентификатор заказа']")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[@type='button']")

    FIRST_INGREDIENT_IN_FILING = (By.XPATH, "//h2[normalize-space()='Начинки']/following-sibling::ul[1]//a[1]") 
    FIRST_BUN = (By.XPATH, "//h2[normalize-space()='Булки']/following-sibling::ul[1]//a[1]")
    ORDER_SUCCESS_MESSAGE = (By.XPATH, ".//p[text() = 'идентификатор заказа']")
    ORDER_NUMBER = (By.CSS_SELECTOR, "h2.text_type_digits-large")
  