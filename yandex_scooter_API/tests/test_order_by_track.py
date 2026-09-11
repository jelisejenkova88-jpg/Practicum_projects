import allure
from data import DataOrder
from api_methods.order_methods import OrderMethods


class TestGetListByNumber:
    @allure.title("Успешное получение заказа по существенному номеру трека")
    @allure.description("Проверка того, что при запросе с валидным номером трека возвращается код ответа 200 "
                        "и объект заказа (dict) в ключе 'order'.")
    def test_get_order_by_number_success(self, created_order):
        track = created_order["track"]
        response = OrderMethods.get_order_by_track(track)
        assert response.status_code == 200
        assert "order" in response.json()
        assert isinstance(response.json()["order"], dict)

    @allure.title("Ошибка при запросе заказа без указания номера трека")
    @allure.description("Проверка отправки запроса на получение заказа без номера трека (track=None). "
                        "Ожидается код ответа 400 и соответствующее сообщение об ошибке.")
    def test_get_order_by_number_without_track(self):
        response = OrderMethods.get_order_by_track(None)
        assert response.status_code == 400
        assert response.json()["message"] == DataOrder.ORDER_BY_NUMBER_ERROR_MESSAGE_NO_TRACK

    @allure.title("Ошибка при запросе заказа с несуществующим номером трека")
    @allure.description("Проверка отправки запроса с несуществующим номером трека. "
                        "Ожидается код ответа 404 и соответствующее сообщение об ошибке.")
    def test_get_order_by_number_invalid_track(self):
        non_existent_track = DataOrder.ORDER_BY_NUMBER_INVALID_TRACK
        response = OrderMethods.get_order_by_track(non_existent_track)
        assert response.status_code == 404
        assert response.json()["message"] == DataOrder.ORDER_BY_NUMBER_ERROR_MESSAGE_INVALID_TRACK
