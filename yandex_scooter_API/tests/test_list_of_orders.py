import allure
import pytest
from api_methods.order_methods import OrderMethods


class TestListOfOrders:
    @allure.title("Успешное получение списка заказов и проверка структуры ответа")
    @allure.description("Проверка того, что запрос на получение списка заказов без параметров "
                        "возвращает код ответа 200, а в теле ответа присутствуют ключевое поле 'orders' со значением типа list.")
    def test_get_order_list_main_structure(self, created_order):
        response = OrderMethods.get_order_list()
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)

    @pytest.mark.parametrize("limit,page", [(5, 0), (10, 1), (30, 0)])
    @allure.title("Получение списка заказов с параметрами пагинации (limit, page)")
    @allure.description("Проверка корректной работы пагинации и ограничения количества возвращаемых заказов. "
                        "Ожидается код ответа 200, а количество элементов в списке 'orders' не должно превышать переданный limit.")
    def test_get_order_list_with_pagination(self, limit, page):
        params = {"limit" : limit, "page" : page}
        response = OrderMethods.get_order_list(params=params)
        assert response.status_code == 200
        assert "orders" in response.json()
        assert len(response.json()["orders"]) <= limit
        