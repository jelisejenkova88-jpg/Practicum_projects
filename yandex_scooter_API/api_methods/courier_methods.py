import requests
import allure
from url import Url


class CourierMethods():
    @staticmethod
    @allure.step("Создание курьера с логином {login}")
    def create_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
            }
        response = requests.post(f"{Url.CREATE_COURIER}", data=payload)
        return response

    @staticmethod
    @allure.step("Логин курьера с логином {login}")
    def login_courier(login, password):
        payload = {"login": login, "password": password}
        response = requests.post(f"{Url.LOGIN_COURIER}", data=payload)
        return response
    
    @staticmethod
    @allure.step("Удаление курьера с id={cid}")
    def delete_courier(cid):
        response = requests.delete(f"{Url.DELETE_COURIER}{cid}")
        return response