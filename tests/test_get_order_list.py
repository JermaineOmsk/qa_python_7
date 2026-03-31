import allure
import requests
import pytest
from data import *


class TestGetOrdersList:
    @allure.title("Получение списка заказов.Проверка кода ответа")
    def test_get_order_list_code(self):
        response = requests.get(f'{Urls.url}{Endpoints.get_orders_list}')
        assert response.status_code == 200
        

    @allure.title("Получение списка заказов. Проверка текста ответа")
    def test_get_order_list_text(self):
        response = requests.get(f'{Urls.url}{Endpoints.get_orders_list}')
        assert Response.orders_list in response.json()
        