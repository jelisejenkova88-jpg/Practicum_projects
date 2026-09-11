import pytest
import requests
from generators import generate_registration_data
from api_methods.methods import Methods
from url import Url

@pytest.fixture
def create_test_user():
    payload = generate_registration_data()
    response = Methods.create_user(email=payload["email"],
                                       password=payload["password"],
                                       name=payload["name"])

    yield {
        "payload": payload,
        "response": response
    }

    data = response.json()
    access_token = data.get("accessToken")
    resp = requests.delete(f"{Url.DELETE_USER}", headers={"Authorization": f"Bearer {access_token}"})


@pytest.fixture
def authorized_user_token(create_test_user):
    response = create_test_user["response"]
    data = response.json()
    if response.status_code != 200:
        raise Exception(f"Не удалось получить токен. Статус: {response.status_code}, Ответ: {data}")
    return data.get("accessToken")
   
     