import requests
import allure
import random
import string
from data import *
# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@allure.step('Регистрация нового курьера и возвращения списка с логином,паролем и именем')
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    @allure.step('Генерация случайной строки')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    for attempt in range(5):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(f'{Urls.url}{Endpoints.create_courier}', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)
            break
        
    # возвращаем список
    return login_pass


@allure.step('Удаление курьера по логину и паролю')   
def delete_courier(login, password):
    login_response = requests.post(f'{Urls.url}{Endpoints.login_courier}',data={'login': login, 'password': password})
    courier_id = login_response.json().get('id')
    if courier_id:
        requests.delete(f'{Urls.url}{Endpoints.delete_courier}{courier_id}')    