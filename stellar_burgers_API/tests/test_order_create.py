import allure
from api_methods.methods import Methods
from data import Data


class TestCreateOrder:

    @allure.title("Создание заказа: успешный сценарий с авторизованным пользователем")
    @allure.description(
    "Проверяется успешное создание заказа авторизованным пользователем. "
    "Ожидается статус 200, флаг success=True, а также наличие полей 'name' и 'order' в теле ответа. ")
    def test_create_order_authorized(self, authorized_user_token):
        payload = Data.ingredient_id
        response = Methods.create_order(payload=payload, token=authorized_user_token)
        assert response.status_code == 200
        data = response.json()
        assert data.get("success") is True
        assert "name" in data
        assert "order" in data

    @allure.title("Создание заказа: успешный сценарий с валидными ингредиентами")
    @allure.description("Проверяется успешное создание заказа авторизованным пользователем при передаче валидного списка ingredient_id. "
                        "Ожидается статус 200, подтверждающий, что заказ корректно сформирован и принят системой.")
    def test_create_order_with_ingredients(self, authorized_user_token):
        payload = Data.ingredient_id
        response = Methods.create_order(payload=payload, token=authorized_user_token)
        assert response.status_code == 200

    @allure.title("Создание заказа: попытка без авторизации")
    @allure.description("Проверяется защита эндпоинта создания заказа. Авторизационный токен не передаётся (token=None). "
                        "Ожидается статус 401 Unauthorized, подтверждающий, что система запрещает создавать заказы неавторизованным пользователям.")   
    def test_create_order_unauthorized(self):
        payload = Data.ingredient_id
        response = Methods.create_order(payload=payload, token=None)
        assert response.status_code == 401

    @allure.title("Создание заказа: пустой список ингредиентов")
    @allure.description("Проверяется валидация входных данных: передача пустого списка ингредиентов. "
    "Ожидается ошибка валидации (статус 400) и сообщение, указывающее, что ingredient_id обязательны. ")
    def test_create_order_without_ingredients(self, authorized_user_token):
        payload = Data.ingredient_no_id
        response = Methods.create_order(payload=payload, token=authorized_user_token)
        assert response.status_code == 400
        data = response.json()
        assert data.get("success") is False
        assert data.get ("message") == "Ingredient ids must be provided"

    @allure.title("Создание заказа: невалидный список ингредиентов")
    @allure.description("Тестируется обработка невалидного ingredient_id. Ожидается, что бэкенд вернёт ошибку 500.")
    def test_create_order_with_invalid_ingredient_id(self, authorized_user_token):
        payload = Data.ingredient_wrong_id
        response = Methods.create_order(payload=payload, token=authorized_user_token)
        assert response.status_code == 500
