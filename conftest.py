import pytest
from data import *
from functions import *

@pytest.fixture
def check_create_courier():
    courier = register_new_courier_and_return_login_password()
    delete_courier(courier[0], courier[1])
    yield {
        'login': courier[0],
        'password': courier[1],
        'firstName': courier[2]
    }

    # Очистка после теста
    delete_courier(courier[0], courier[1])

@pytest.fixture
def create_courier():
    courier = register_new_courier_and_return_login_password()
    yield {
        'login': courier[0],
        'password': courier[1],
        'firstName': courier[2]
    }

    # Очистка после теста
    delete_courier(courier[0], courier[1])
  