import pytest
from generators import register_new_courier_and_return_login_password
from api_methods.courier_methods import CourierMethods
from api_methods.order_methods import OrderMethods
from generators import generate_order_payload


@pytest.fixture
def courier_for_test():
    data = register_new_courier_and_return_login_password()

    if not data:
        pytest.fail("Генератор не смог создать курьера (вернул пустой список)")

    login, password, first_name = data
    response = CourierMethods.create_courier(login, password, first_name)
    cid = response.json().get("id")
    courier_info = {"login" : login, 
                    "password" : password,
                    "firstName" : first_name,
                    "id" : cid}
    yield courier_info

    delete_response = CourierMethods.delete_courier(courier_info["id"])

@pytest.fixture
def created_courier():
    data = register_new_courier_and_return_login_password()

    if not data:
        pytest.fail("Генератор не смог создать курьера (вернул пустой список)")

    login, password, first_name = data
    response_create = CourierMethods.create_courier(login, password, first_name)
    response_login = CourierMethods.login_courier(login, password)
    cid = response_login.json().get("id")
    courier_info = {"login" : login, 
                    "password" : password,
                    "firstName" : first_name,
                    "id" : cid}
    yield courier_info

    delete_response = CourierMethods.delete_courier(courier_info["id"])

@pytest.fixture
def created_order(color_value=None):
    payload = generate_order_payload()
    if color_value is not None:
        payload["color"] = color_value

    response = OrderMethods.create_order(payload)
    track = response.json().get("track")

    yield {"response": response, "track": track}

    OrderMethods.cancel_order(track)

@pytest.fixture
def created_order_id():
    payload = generate_order_payload()
    create_response = OrderMethods.create_order(payload)
    track = create_response.json().get("track")
    track_response = OrderMethods.get_order_by_track(track)
    order_id = track_response.json().get("order", {}).get("id")

    yield order_id

    OrderMethods.cancel_order(track)
                                                 