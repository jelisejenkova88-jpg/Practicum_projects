import allure
from generators import generate_random_string
from api_methods.courier_methods import CourierMethods
from data import DataCourier


class TestCourierCreation:
    @allure.title("Успешное создание курьера")
    @allure.description("Проверка успешного создания курьера при передаче всех валидных полей (login, password, firstName). "
                        "Ожидается код ответа 201 и {'ok': true} в теле ответа.")
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        response = CourierMethods.create_courier(login, password, first_name)
        assert response.status_code == 201
        assert response.json().get("ok") is True

    @allure.title("Ошибка при создании курьера с уже существующим логином")
    @allure.description("Проверка отправки запроса на создание курьера с логином, который уже зарегистрирован в системе. "
                        "Ожидается код ответа 409 и соответствующее сообщение об ошибке.")
    def test_cannot_create_duplicate_login(self, courier_for_test):
        existing_login = courier_for_test["login"]
        new_password = generate_random_string(10)
        new_first_name = generate_random_string(10)
        response = CourierMethods.create_courier(existing_login, new_password, new_first_name)
        assert response.status_code == 409
        assert response.json()["message"] == DataCourier.CREATE_ERROR_MESSAGE_DUPLICATE_LOGIN

    @allure.title("Ошибка при создании курьера с пустым логином")
    @allure.description("Проверка отправки запроса на создание курьера с пустым значением в поле login. "
                        "Ожидается код ответа 400 и соответствующее сообщение об ошибке.")
    def test_create_courier_empty_login_field(self):
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        response = CourierMethods.create_courier("", password, first_name) 
        assert response.status_code == 400
        assert response.json()["message"] == DataCourier.CREATE_ERROR_MESSAGE_MISSING_FIELDS

    @allure.title("Ошибка при создании курьера с пустым паролем")
    @allure.description("Проверка отправки запроса на создание курьера с пустым значением в поле password. "
                        "Ожидается код ответа 400 и соответствующее сообщение об ошибке.")
    def test_create_courier_empty_password_field(self):
        login = generate_random_string(10)
        first_name = generate_random_string(10)
        response = CourierMethods.create_courier(login, "", first_name)        
        assert response.status_code == 400
        assert response.json()["message"] == DataCourier.CREATE_ERROR_MESSAGE_MISSING_FIELDS

    @allure.title("Ошибка при создании курьера с пустым именем")
    @allure.description("Проверка отправки запроса на создание курьера с пустым значением в поле firstName. "
                        "Ожидается код ответа 400 и соответствующее сообщение об ошибке.")
    def test_create_courier_empty_first_name_field(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        response = CourierMethods.create_courier(login, password, "")        
        assert response.status_code == 400
        assert response.json()["message"] == DataCourier.CREATE_ERROR_MESSAGE_MISSING_FIELDS
        