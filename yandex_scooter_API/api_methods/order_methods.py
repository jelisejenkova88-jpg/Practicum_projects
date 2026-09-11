import requests
import allure
from url import Url

class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        return requests.post(f"{Url.CREATE_ORDER}", json=payload)
    
    @staticmethod
    @allure.step("Отмена заказа с треком {track_id}")
    def cancel_order(track_id):
        params = {"track" : track_id}
        return requests.put(f"{Url.CANCEL_ORDER}", params=params)
    
    @staticmethod
    @allure.step("Получение списка заказов (параметры: {params})")
    def get_order_list(params=None):
        return requests.get(f"{Url.LIST_OF_ORDERS}", params=params)

    @staticmethod
    @allure.step("Принятие заказа id={order_id} курьером cid={cid}")
    def accept_order(order_id, cid):
        params = {"courierId": cid} 
        return requests.put(f"{Url.ACCEPT_ORDER}{order_id}", params=params)

    @staticmethod
    @allure.step("Получение заказа по номеру: {track}")
    def get_order_by_track(track):
        return requests.get(f"{Url.GET_ORDER_BY_TRACK}", params={"t": track})
    