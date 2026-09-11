import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие страницы")
    def open(self, url):
        self.driver.get(url)

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

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Ожидание исчезновения элемента")
    def _wait_for_invisibility_of_element_located(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Скролл до элемента с локатором {locator}")
    def scroll_to_element(self, locator, timeout=10):
        element = self._wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ввод данных в элемент с локатором {locator}")
    def send_keys_to_element(self, locator, keys, timeout = 10):
        element = self._wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Выполнить JS-скрипт перетаскивания ингредиента в зону заказа")
    def drag_via_js(self, ingredient_element, order_zone):
        script = """
        (function(source, target) {
            var dragStartEvent = new MouseEvent('dragstart', {
                'view': window, 'bubbles': true, 'cancelable': true
            });
            source.dispatchEvent(dragStartEvent);

            var dropEvent = new DragEvent('drop', {
                'view': window, 'bubbles': true, 'cancelable': true
            });
            target.dispatchEvent(dropEvent);

            var dragEndEvent = new MouseEvent('dragend', {
                'view': window, 'bubbles': true, 'cancelable': false
            });
            source.dispatchEvent(dragEndEvent);
        })(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, ingredient_element, order_zone)

    @allure.step("Ожидание выполнения условия")
    def wait_until(self, condition, timeout=20, poll_frequency=0.5):
        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency)
        return wait.until(condition)

    @allure.step("Поиск элемента по тегу {tag_name} внутри элемента {element}")
    def find_by_tag(self, element, tag_name):
        return element.find_element(By.TAG_NAME, tag_name)

    @allure.step("Поиск элемента по локатору {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step("Поиск списка элементов по локатору {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("JS‑клик по элементу (обход перекрытия слоями)")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)
        