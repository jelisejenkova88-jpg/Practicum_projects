import allure
from api_methods.methods import Methods
from data import Data


class TestLoginUser:

    @allure.title("Логин: проверка структуры ответа и токенов")
    @allure.description("Проверяется успешный логин: статус 200, success=True, наличие accessToken и refreshToken, а также что accessToken не равен null.")
    def test_login_user_structure_and_token_correct(self, create_test_user):
        payload = create_test_user["payload"]
        email = payload["email"]
        password = payload["password"]
        response = Methods.login_user(email, password)
        data = response.json()
        assert response.status_code == 200
        assert data.get("success") is True
        assert "accessToken" in data
        assert data["accessToken"] is not None
        assert "refreshToken" in data 

    @allure.title("Логин: совпадение данных пользователя с зарегистрированными")
    @allure.description("Проверяется, что в ответе после логина поля email и name совпадают с теми, что были указаны при регистрации.")
    def test_login_user_data_match_correct(self, create_test_user):
        payload = create_test_user["payload"]
        email = payload["email"]
        password = payload["password"]
        response = Methods.login_user(email, password)
        data = response.json()
        user_info = data["user"]
        assert user_info.get("email") == payload["email"]
        assert user_info.get("name") == payload["name"]

    @allure.title("Логин: ошибка при неверном email")
    @allure.description("Проверяется обработка попытки входа с неверным email. Ожидается статус 401 и сообщение об ошибке аутентификации.")
    def test_login_user_wrong_email_error(self, create_test_user):
        payload = create_test_user["payload"]
        email = Data.wrong_email
        password = payload["password"]
        response = Methods.login_user(email, password)
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Логин: ошибка при неверном пароле")
    @allure.description("Проверяется обработка попытки входа с неверным паролем. Ожидается статус 401 и сообщение об ошибке аутентификации.")   
    def test_login_user_wrong_password_error(self, create_test_user):
        payload = create_test_user["payload"]
        email = payload["email"]
        password = Data.wrong_password
        response = Methods.login_user(email, password)
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Логин: ошибка при пустом email")
    @allure.description("Проверяется реакция API на попытку входа с пустым email (None). Ожидается статус 401 и сообщение об ошибке аутентификации.")
    def test_login_user_empty_email_field_error(self, create_test_user):
        payload = create_test_user["payload"]
        email = None
        password = payload["password"]
        response = Methods.login_user(email, password)
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Логин: ошибка при пустом пароле")
    @allure.description("Проверяется реакция API на попытку входа с пустым паролем (None). Ожидается статус 401 и сообщение об ошибке аутентификации.")
    def test_login_user_empty_password_field_error(self, create_test_user):
        payload = create_test_user["payload"]
        email = payload["email"]
        password = None
        response = Methods.login_user(email, password)
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"
