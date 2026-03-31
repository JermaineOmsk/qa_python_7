import allure
import requests
import pytest
from data import *


class TestCreateCourier:
    @allure.title("Проверка кода ответа при удачном создании курьера")
    def test_create_courier_success_status_code(self,check_create_courier):
        response = requests.post(f'{Urls.url}{Endpoints.create_courier}', data=check_create_courier)
        assert response.status_code == 201

    @allure.title("Проверка текста ответа при удачном создании курьера")   
    def test_create_courier_success_text(self,check_create_courier):
        response = requests.post(f'{Urls.url}{Endpoints.create_courier}', data=check_create_courier)
        assert response.json() == Response.successful_registration

    @allure.title("Проверка кода ответа при создании курьера с существующим логином")    
    def test_cannot_create_duplicate_courier_status_code(self,check_create_courier):
        response_one = requests.post(f'{Urls.url}{Endpoints.create_courier}', data=check_create_courier)
        response_two = requests.post(f'{Urls.url}{Endpoints.create_courier}', data=check_create_courier)
        assert response_two.status_code == 409
    
    @allure.title("Проверка текста ответа при создании курьера с существующим логином")    
    def test_cannot_create_duplicate_courier_text(self,check_create_courier):
        response_one = requests.post(f'{Urls.url}{Endpoints.create_courier}', data=check_create_courier)
        response_two = requests.post(f'{Urls.url}{Endpoints.create_courier}', data=check_create_courier)
        assert response_two.json()['message'] == Response.login_already_inuse['message']

    @allure.title("Параметризованный тест.Проверка кода ответа при создании курьера с отсутствующим логином или паролем")    
    @pytest.mark.parametrize("empty", [
        ('login'),
        ('password'),])
    def test_one_required_field_empty_status_code(self,empty, check_create_courier):
        payload = check_create_courier
        payload.pop(empty)
        response = requests.post(f'{Urls.url}{Endpoints.create_courier}', data=payload)
        assert response.status_code == 400

    @allure.title("Параметризованный тест.Проверка текста ответа при создании курьера с отсутствующим логином или паролем") 
    @pytest.mark.parametrize("empty", [
        ('login'),
        ('password'),])
    def test_one_required_field_empty_text(self,empty, check_create_courier):
        payload = check_create_courier
        payload.pop(empty)
        response = requests.post(f'{Urls.url}{Endpoints.create_courier}', data=payload)
        assert  response.json()['message'] == Response.bad_request_registration['message']