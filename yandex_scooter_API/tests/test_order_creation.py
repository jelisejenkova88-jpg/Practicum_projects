import pytest
import allure


class TestOrderCreation:
    @pytest.mark.parametrize("color_value", [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    @allure.title("Создание заказа с различными вариациями цвета")
    @allure.description("Проверка возможности создания заказа с указанием одного из цветов (BLACK, GREY), "
                        "обоих цветов одновременно или без указания цвета (None). "
                        "Ожидается код ответа 201 и возвращение валидного номера трека (track).")
    def test_create_order_with_color_variations(self, color_value, created_order):
        data = created_order
        response = data["response"]
        track = data["track"]
        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}. Ответ: {response.text}"
        assert "track" in response.json(), "В ответе отсутствует поле 'track'"
        assert track is not None, "Поле 'track' пустое"
