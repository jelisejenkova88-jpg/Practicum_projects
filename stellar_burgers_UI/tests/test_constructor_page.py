import allure
from locators.constructor_locators import ConstructorLocators
from pages.constructor_page import ConstructorPage
from url import MAIN_URL, ORDER_LIST_URL

class TestMainPage:

    @allure.title("Проверка: клик по кнопке «Конструктор» не перенаправляет со стартовой страницы, если пользователь уже на ней")
    @allure.description("Тест проверяет, что при клике на кнопку «Конструктор», когда пользователь уже находится на главной странице, URL не меняется и остаётся равным MAIN_URL.")
    def test_click_constructor_stay_on_main_page_when_already_on_home(self, driver):
        page = ConstructorPage(driver)
        page.open(MAIN_URL)
        page.click_element(ConstructorLocators.CONSTRUCTOR_BUTTON)
        assert page.is_on_page(MAIN_URL)

    @allure.title("Проверка: кнопка «Конструктор» возвращает на главную страницу со страницы списка заказов")
    @allure.description("Тест проверяет, что при переходе на страницу списка заказов и последующем клике на кнопку «Конструктор» пользователь возвращается на главную страницу (MAIN_URL).")    
    def test_click_constructor_returns_to_home_from_other_page(self, driver):
        page = ConstructorPage(driver)
        page.open(MAIN_URL)
        page.click_element(ConstructorLocators.ORDER_LIST_BUTTON)
        page.click_element(ConstructorLocators.CONSTRUCTOR_BUTTON)
        assert page.is_on_page(MAIN_URL)

    @allure.title("Переход по «Лента заказов» ведёт на ожидаемый URL")
    @allure.description("Тест проверяет, что клик по кнопке «Лента заказов» на главной странице корректно перенаправляет пользователя на страницу списка заказов (ORDER_LIST_URL).")
    def test_click_order_list_navigates_to_order_page(self, driver):
        page = ConstructorPage(driver)
        page.open(MAIN_URL)
        page.click_element(ConstructorLocators.ORDER_LIST_BUTTON)
        assert page.is_on_page(ORDER_LIST_URL)

    @allure.title("Клик по «Лента заказов» не меняет URL, если пользователь уже на странице заказов")
    @allure.description("Тест проверяет, что при клике на кнопку «Лента заказов», когда пользователь уже находится на странице списка заказов, URL остаётся неизменным (ORDER_LIST_URL).")
    def test_click_order_list_stay_on_order_page(self, driver):
        page = ConstructorPage(driver)
        page.open(ORDER_LIST_URL)
        page.click_order_list_button()
        assert page.is_on_page(ORDER_LIST_URL)

    @allure.title("Клик по ингредиенту открывает модальное окно с деталями")
    @allure.description("Тест проверяет, что при клике на первый ингредиент в разделе «Соусы» открывается модальное окно с информацией об ингредиенте.")
    def test_click_ingredient_opens_modal(self, driver):
        page = ConstructorPage(driver)
        page.open(MAIN_URL)
        page.scroll_to_element(ConstructorLocators.SAUCES_SECTION)
        page.click_element(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        assert page.check_is_modal_visible(ConstructorLocators.MODAL_WINDOW)

    @allure.title("Модальное окно закрывается по кнопке «Закрыть»")
    @allure.description("Тест проверяет, что модальное окно, открытое при клике на ингредиент, корректно закрывается при нажатии на кнопку закрытия и больше не отображается на странице.")
    def test_modal_closes_with_close_button(self, driver):
        page = ConstructorPage(driver)
        page.open(MAIN_URL)
        page.scroll_to_element(ConstructorLocators.SAUCES_SECTION)
        page.click_element(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        page.close_modal_window()
        assert page.check_is_modal_invisible()

    @allure.title("Повторное открытие модального окна после закрытия")
    @allure.description("Тест проверяет, что модальное окно с деталями ингредиента можно открыть повторно после его закрытия — клик по тому же ингредиенту снова вызывает появление окна.")
    def test_reopen_modal_after_close(self, driver):
        page = ConstructorPage(driver)
        page.open(MAIN_URL)
        page.scroll_to_element(ConstructorLocators.SAUCES_SECTION)
        page.click_element(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        page.close_modal_window()
        page.click_element(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        assert page.check_is_modal_visible(ConstructorLocators.MODAL_WINDOW)

    @allure.title("Счётчик на карточке ингредиента увеличивается при добавлении в заказ")
    @allure.description("Тест проверяет корректность работы счётчика: после добавления ингредиента в заказ значение на его карточке должно увеличиться ровно на 1 (сравнение значений до и после с ожидаемым приростом).")
    def test_counter_on_ingredient_card_increases(self, driver):
        page = ConstructorPage(driver)
        page.open(MAIN_URL)
        page.scroll_to_element(ConstructorLocators.SAUCES_SECTION)
        before = page.get_ingredient_counter_value(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        page.add_ingredient_or_bun(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        after = page.wait_for_counter_increase(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES, before)
        assert after == before + 1

    @allure.title("Счётчик корректно увеличивается при многократном перетаскивании ингредиента")
    @allure.description("Тест проверяет, что при трёхкратном добавлении одного и того же ингредиента в заказ счётчик на его карточке увеличивается ровно на 3 (сравнение значения до и после с ожидаемым приростом).")
    def test_multiple_drag_increases_counter_correctly(self, driver):
        page = ConstructorPage(driver)
        page.open(MAIN_URL)
        page.scroll_to_element(ConstructorLocators.SAUCES_SECTION)
        before = page.get_ingredient_counter_value(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        page.add_ingredient_or_bun(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        page.add_ingredient_or_bun(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        page.add_ingredient_or_bun(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        after = page.wait_for_counter_increase(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES, before)
        assert after == before + 3


    @allure.title("Счётчики ингредиентов независимы друг от друга")
    @allure.description("Тест проверяет, что при добавлении одного ингредиента в заказ счётчик этого ингредиента увеличивается на 1, а счётчики других ингредиентов (в частности, соседнего) остаются без изменений — подтверждая независимость счётчиков для разных карточек.")
    def test_counters_are_independent(self, driver):
        page = ConstructorPage(driver)
        page.open(MAIN_URL)
        page.scroll_to_element(ConstructorLocators.SAUCES_SECTION)
        count_1_before = page.get_ingredient_counter_value(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        count_2_before = page.get_ingredient_counter_value(ConstructorLocators.SECOND_INGREDIENT_IN_SAUCES)
        page.add_ingredient_or_bun(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES)
        count_1_after = page.wait_for_counter_increase(ConstructorLocators.FIRST_INGREDIENT_IN_SAUCES, count_1_before, timeout=15)
        count_2_after = page.get_ingredient_counter_value(ConstructorLocators.SECOND_INGREDIENT_IN_SAUCES)  
        assert count_1_after == count_1_before + 1 and count_2_after == count_2_before
       