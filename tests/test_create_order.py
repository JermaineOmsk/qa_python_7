import allure
import requests
import pytest
from data import *
import json
class TestCreateOrder:
    @allure.title("Параметризованный тест.Создание заказа с разными цветами самоката ")
    @pytest.mark.parametrize("color_value", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []  
    ])
    def test_create_order_with_different_colors(self, color_value):
        
        payload = { "firstName": User.firstName,
                    "lastName": User.lastName,
                    "address": User.address,
                    "metroStation": User.metroStation,
                    "phone": User.phone,
                    "rentTime": User.rentTime,
                    "deliveryDate": User.deliveryDate,
                    "comment":User.comment,
                    "color": color_value}
        payload_string = json.dumps(payload)
        response = requests.post(f'{Urls.url}{Endpoints.create_order}', data=payload_string)
        assert response.status_code == 201  
        assert 'track' in response.json()