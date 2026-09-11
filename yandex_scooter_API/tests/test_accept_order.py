import allure
from api_methods.order_methods import OrderMethods
from data import DataOrder


class TestAcceptOrder:
    @allure.title("Успешное принятие заказа курьером")
    @allure.description("Проверка того, что курьер может успешно принять существующий заказ. "
                        "Ожидается код ответа 200 и {'ok': true} в теле ответа.")
    def test_accept_order_success(self, created_courier, created_order_id):
        order_id = created_order_id
        cid = created_courier["id"]
        response = OrderMethods.accept_order(order_id, cid)
        assert response.status_code == 200
        assert "ok" in response.json()
        assert response.json()["ok"] is True

    @allure.title("Ошибка при принятии заказа с несуществующим ID курьера")
    @allure.description("Проверка отправки запроса с несуществующим ID курьера. "
                        "Ожидается код ответа 404 и соответствующее сообщение об ошибке.")
    def test_accept_order_invalid_courier_id(self, created_order_id):
        order_id = created_order_id
        invalid_cid = DataOrder.INVALID_CID
        response = OrderMethods.accept_order(order_id, invalid_cid)
        assert response.status_code == 404
        assert response.json()["message"] == DataOrder.ACCEPT_ERROR_MESSAGE_COURIER_NOT_FOUND

    @allure.title("Ошибка при принятии заказа с несуществующим ID заказа")
    @allure.description("Проверка отправки запроса с несуществующим ID заказа. "
                        "Ожидается код ответа 404 и соответствующее сообщение об ошибке.")
    def test_accept_order_invalid_order_id(self, created_courier):
        cid = created_courier["id"]
        invalid_order_id = DataOrder.INVALID_ORDER_ID
        response = OrderMethods.accept_order(invalid_order_id, cid)
        assert response.status_code == 404
        assert response.json()["message"] == DataOrder.ACCEPT_ERROR_MESSAGE_ORDER_NOT_FOUND

    @allure.title("Ошибка при принятии заказа без передачи ID курьера")
    @allure.description("Проверка отправки запроса на принятие заказа без указания параметров курьера (cid=None). "
                        "Ожидается код ответа 400 и соответствующее сообщение об ошибке.")
    def test_accept_order_without_courier_id(self, created_order_id):
        order_id = created_order_id
        response = OrderMethods.accept_order(order_id, cid=None)
        assert response.status_code == 400
        assert response.json()["message"] == DataOrder.ACCEPT_ERROR_MESSAGE_NO_ID

    @allure.title("Ошибка при принятии заказа без передачи ID заказа")
    @allure.description("Проверка отправки запроса на принятие заказа с пустым ID заказа. "
                        "Ожидается код ответа 400 и соответствующее сообщение об ошибке.")
    def test_accept_order_without_order_id(self, created_courier):
        cid = created_courier["id"]
        response = OrderMethods.accept_order("", cid)
        assert response.status_code == 400
        assert response.json()["message"] == DataOrder.ACCEPT_ERROR_MESSAGE_NO_ID
