import allure
from api_methods.courier_methods import CourierMethods
from data import DataCourier


class TestCourierDelete:
    @allure.title("Успешное удаление курьера")
    @allure.description("Проверка того, что существующий курьер успешно удаляется по его ID. "
                        "Ожидается код ответа 200 и {'ok': true} в теле ответа.")
    def test_delete_courier_success(self, created_courier):
        cid = created_courier["id"]
        response = CourierMethods.delete_courier(cid)
        assert response.status_code == 200
        assert "ok" in response.json()
        assert response.json()["ok"] is True

    @allure.title("Ошибка при удалении курьера без передачи ID")
    @allure.description("Проверка отправки запроса на удаление курьера с пустым ID. "
                        "Ожидается код ответа 400 и соответствующее сообщение об ошибке.")
    def test_delete_courier_no_id(self, created_courier):
        response = CourierMethods.delete_courier("") 
        assert response.status_code == 400
        assert response.json()['message'] == DataCourier.DELETE_ERROR_MESSAGE_MISSING_ID

    @allure.title("Ошибка при удалении курьера с несуществующим ID")
    @allure.description("Проверка отправки запроса на удаление курьера с несуществующим ID. "
                        "Ожидается код ответа 404 и соответствующее сообщение об ошибке.")
    def test_delete_courier_invalid_id(self):
        not_existent_id = DataCourier.INVALID_ID
        response = CourierMethods.delete_courier(not_existent_id)
        assert response.status_code == 404
        assert response.json()['message'] == DataCourier.DELETE_ERROR_MESSAGE_INVALID_ID

    @allure.title("Ошибка при повторном удалении уже удаленного курьера")
    @allure.description("Проверка отправки повторного запроса на удаление курьера после успешного первого удаления. "
                        "Второй запрос должен вернуть код 404 и соответствующее сообщение об ошибке.")
    def test_delete_courier_already_deleted(self, created_courier):
        cid = created_courier["id"]
        first_response = CourierMethods.delete_courier(cid)
        assert first_response.status_code == 200
        assert first_response.json()["ok"] is True
        second_response = CourierMethods.delete_courier(cid)
        assert second_response.status_code == 404
        assert second_response.json()["message"] == DataCourier.DELETE_ERROR_MESSAGE_INVALID_ID
