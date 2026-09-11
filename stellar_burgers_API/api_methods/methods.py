import requests
import allure
from url import Url

class Methods:

    @staticmethod 
    @allure.step("Создание пользователя")   
    def create_user(email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
            }
        response = requests.post(f"{Url.CREATE_USER}", data=payload)
        return response

    @staticmethod
    @allure.step("Авторизация пользователя") 
    def login_user(email, password):
        payload = {
            "email": email,
            "password": password
            }
        response = requests.post(f"{Url.LOGIN_USER}", data=payload)
        return response

    @staticmethod
    @allure.step("Создание заказа") 
    def create_order(payload : dict, token : str | None = None): 
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"{token}"
        return requests.post(f"{Url.CREATE_ORDER}", json=payload, headers=headers)
    