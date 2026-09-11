import allure
from api_methods.courier_methods import CourierMethods
from data import DataCourier


class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    @allure.description("Проверка успешной авторизации курьера с правильным логином и паролем. "
                        "Ожидается код ответа 200 и возвращение валидного ID курьера.")
    def test_login_courier_success(self, created_courier):
        login = created_courier["login"]
        password = created_courier["password"]
        response = CourierMethods.login_courier(login, password)
        assert response.status_code == 200
        assert "id" in response.json()
        assert response.json()["id"] is not None

    @allure.title("Ошибка авторизации при неверном логине")
    @allure.description("Проверка авторизации курьера с неверно указанным логином. "
                        "Ожидается код ответа 404 и соответствующее сообщение об ошибке.")
    def test_login_courier_wrong_login(self, created_courier):
        password = created_courier["password"]
        response = CourierMethods.login_courier(DataCourier.WRONG_LOGIN_VALUE, password)
        assert response.status_code == 404
        assert response.json()["message"] == DataCourier.LOGIN_ERROR_MESSAGE_ACCOUNT_NOT_FOUND

    @allure.title("Ошибка авторизации при неверном пароле")
    @allure.description("Проверка авторизации курьера с неверно указанным паролем. "
                        "Ожидается код ответа 404 и соответствующее сообщение об ошибке.")
    def test_login_courier_wrong_password(self, created_courier):
        login = created_courier["login"]
        response = CourierMethods.login_courier(login, DataCourier.WRONG_PASSWORD_VALUE)
        assert response.status_code == 404
        assert response.json()["message"] == DataCourier.LOGIN_ERROR_MESSAGE_ACCOUNT_NOT_FOUND

    @allure.title("Ошибка авторизации при пустом поле логина")
    @allure.description("Проверка отправки запроса на авторизацию с пустым значением в поле login. "
                        "Ожидается код ответа 400 и соответствующее сообщение об ошибке.")
    def test_login_courier_empty_login_field(self, created_courier):
        password = created_courier["password"]
        response = CourierMethods.login_courier("", password)
        assert response.status_code == 400
        assert response.json()["message"] == DataCourier.LOGIN_ERROR_MESSAGE_MISSING_DATA

    @allure.title("Ошибка авторизации при пустом поле пароля")
    @allure.description("Проверка отправки запроса на авторизацию с пустым значением в поле password. "
                        "Ожидается код ответа 400 и соответствующее сообщение об ошибке.")
    def test_login_courier_empty_password_field(self, created_courier):
        login = created_courier["login"]
        response = CourierMethods.login_courier(login, "")
        assert response.status_code == 400
        assert response.json()["message"] == DataCourier.LOGIN_ERROR_MESSAGE_MISSING_DATA 

    @allure.title("Ошибка авторизации для несуществующего пользователя")
    @allure.description("Проверка попытки входа несуществующей пары логин/пароль. "
                        "Ожидается код ответа 404 и соответствующее сообщение об ошибке.")
    def test_login_courier_not_exist_user(self):
        response = CourierMethods.login_courier(DataCourier.INVALID_LOGIN, DataCourier.INVALID_PASSWORD)
        assert response.status_code == 404
        assert response.json()["message"] == DataCourier.LOGIN_ERROR_MESSAGE_ACCOUNT_NOT_FOUND
              