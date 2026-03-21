import allure
import requests
import pytest
from data import *


class TestLoginCourier:
    @allure.title("Проверка кода ответа при успешном логине курьера") 
    def test_login_courier_success_status_code(self,create_courier):
        payload ={'login': create_courier['login'],
            'password': create_courier['password']}
        response = requests.post(f'{Urls.url}{Endpoints.login_courier}', data=payload)
        assert response.status_code == 200

    @allure.title("Проверка текста ответа при успешном логине курьера") 
    def test_login_courier_success_status_text(self,create_courier):
        payload ={'login': create_courier['login'],
            'password': create_courier['password']}
        response = requests.post(f'{Urls.url}{Endpoints.login_courier}', data=payload)
        assert  Response.created_id in response.text

    @allure.title("Проверка кода ответа при использовании неправильного логина") 
    def test_invalid_login_status_code(self,  create_courier):
        payload ={'login': f"{create_courier['login']}+InvalidDataCourier.login",
            'password': create_courier['password']}
        response = requests.post(f'{Urls.url}{Endpoints.login_courier}', data=payload)
        assert response.status_code == 404

    @allure.title("Проверка текста ответа при использовании неправильного логина") 
    def test_invalid_login_status_text(self,  create_courier):
        payload ={'login': f"{create_courier['login']}+InvalidDataCourier.login",
            'password': create_courier['password']}
        response = requests.post(f'{Urls.url}{Endpoints.login_courier}', data=payload)
        assert Response.not_found_login in response.text

    @allure.title("Проверка кода ответа при использовании неправильного пароля") 
    def test_invalid_password_status_code(self,  create_courier):
        payload ={'login': create_courier['login'],
            'password': f"{create_courier['password']}+InvalidDataCourier.password"}
        response = requests.post(f'{Urls.url}{Endpoints.login_courier}', data=payload)
        assert response.status_code == 404

    @allure.title("Проверка текста ответа при использовании неправильного пароля") 
    def test_invalid_password_status_text(self,  create_courier):
        payload ={'login': create_courier['login'],
            'password': f"{create_courier['password']}+InvalidDataCourier.password"}
        response = requests.post(f'{Urls.url}{Endpoints.login_courier}', data=payload)
        assert Response.not_found_login in response.text

    @allure.title("Параметризованный тест.Проверка кода ответа при логине курьера с отсутствующим логином или паролем")    
    @pytest.mark.parametrize("empty", [
        ('login'),
        ('password')
    ])
    def test_one_required_field_empty_login(self, empty, create_courier):
        payload = {'login': create_courier['login'], 'password': create_courier['password']}
        payload.pop(empty)
        response = requests.post(f'{Urls.url}{Endpoints.login_courier}', data=payload)
        assert response.status_code == 400
#На этом тесте происходит фейл при отправке запроса с пустым паролем. Ошибка 504. В пачке обсуждали этот вопрос, проблема с самим сервером.
    
 