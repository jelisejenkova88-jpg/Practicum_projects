import pytest
import allure
from api_methods.methods import Methods
from generators import generate_registration_data
from data import Data


class TestUserCreate:
    @allure.title("Регистрация: проверка структуры ответа и наличия токенов")
    @allure.description("Проверяется успешный ответ (200) при регистрации: наличие success=True, accessToken и refreshToken, а также что accessToken не равен null.")
    def test_create_user_structure_and_token_correct(self, create_test_user):
        payload = create_test_user["payload"]
        response = create_test_user["response"]
        data = response.json()
        assert response.status_code == 200
        assert data.get("success") is True
        assert "accessToken" in data
        assert data["accessToken"] is not None
        assert "refreshToken" in data

    @allure.title("Регистрация: совпадение данных пользователя с отправленными")
    @allure.description("Проверяется, что в ответе сервера поля email и name совпадают с теми, что были переданы в payload при регистрации.")
    def test_create_user_data_match_correct(self, create_test_user):
        payload = create_test_user["payload"]
        response = create_test_user["response"]
        data = response.json()
        user_info = data["user"]
        assert user_info.get("email") == payload["email"]
        assert user_info.get("name") == payload["name"]

    @allure.title("Регистрация: ошибка при дублировании email")
    @allure.description("Проверяется реакция API на попытку регистрации с уже существующим email."
                        "Ожидается статус 403 и сообщение об ошибке, указывающее, что пользователь уже существует.")
    def test_create_user_duplicate_email_error(self):
        email = Data.existing_email
        password = Data.existing_password
        name = Data.existing_name
        response = Methods.create_user(email, password, name)
        data = response.json()
        assert response.status_code == 403
        assert data.get("success") is False
        assert data.get ("message") == "User already exists"

    @allure.title("Регистрация: ошибка при отсутствии обязательного поля (email/password/name)")
    @allure.description("Проверяется валидация обязательных полей при регистрации: поочерёдно убирается одно из полей (email, password, name)."
                         "Ожидается статус 403 и сообщение о том, что все поля обязательны.")  
    @pytest.mark.parametrize('field_name', ["email", "password", "name"])
    def test_create_user_missing_field(self, field_name):
        payload = generate_registration_data()
        bad_payload = {"email":payload["email"],
                       "password":payload["password"],
                       "name":payload["name"]
                       }
        bad_payload[field_name] = None
        response = Methods.create_user(**bad_payload)
        data = response.json()
        assert response.status_code == 403
        assert data.get("success") is False
        assert data.get ("message") == "Email, password and name are required fields"
