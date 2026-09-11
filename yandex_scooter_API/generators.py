import requests
import random
import string


def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass 


def generate_order_payload():
    rand_num = random.randint(1000, 9999)
    return {"firstName": f"Naruto_{rand_num}",
            "lastName": f"Uchiha_{rand_num}",
            "address": f"Konoha, 142 apt. {rand_num}",
            "metroStation": 4,
            "phone": f"+7 999 000 00 {rand_num:02d}",
            "rentTime": 5,
            "deliveryDate": "2026-08-10",
            "comment": f"Saske come back to Konoha {rand_num}"
            }
