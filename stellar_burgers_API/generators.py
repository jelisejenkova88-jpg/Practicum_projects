from faker import Faker


faker = Faker()

def generate_registration_data():
    email_prefix = f"qa_user_{faker.random_int(min=1000, max=9999)}"
    return {"email" : f"{email_prefix}@yandex-test-qa.ru",
            "password" : faker.password(length=12, special_chars=True, digits=True),
            "name" : faker.name()
            }
