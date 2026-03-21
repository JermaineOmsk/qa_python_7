import allure
import requests
import pytest
from data import *


class TestGetOrdersList:
    @allure.title("Получение списка заказов")
    def test_get_order_list(self):
        response = requests.get(f'{Urls.url}{Endpoints.get_orders_list}')
        assert response.status_code == 200
        