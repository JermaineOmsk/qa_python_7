class Urls:
    url = 'https://qa-scooter.praktikum-services.ru/'

class Endpoints:
    create_courier = '/api/v1/courier' #post    
    login_courier = '/api/v1/courier/login' #post
    delete_courier = '/api/v1/courier/' #delete
    count_of_orders = '/api/v1/courier/:id/ordersCount' #get
    create_order = '/api/v1/orders' #post
    accept_order = '/api/v1/orders/accept/:id' #put
    get_order_by_number = '/api/v1/orders/track' #get
    get_orders_list = '/api/v1/orders' #get
    cancel_order = '/api/v1/orders/cancel' #put
    finish_order ='/api/v1/orders/finish/:id' #put


class InvalidDataCourier:
    login = 'TrustInMe'
    password = 'WhatAreYouWaitingFor'
    firstName = 'ИванДраго'

class User: 
    firstName = "Рокки"
    lastName = "Бальбоа"	
    address = "3-я ул. Строителей 25, кв.12"
    metroStation = 	4
    phone = "89000000000"	
    rentTime = 5	
    deliveryDate = "2020-06-06"	
    comment = "Привет"
     

class Response:
    successful_registration = {'ok':True}
    bad_request_registration= {"message": "Недостаточно данных для создания учетной записи"}
    login_already_inuse = {"message": "Этот логин уже используется. Попробуйте другой."}
    created_track = "track"
    orders_list = "orders"
    created_id = "id"
    bad_request_login = "Недостаточно данных для входа"
    not_found_login = "Учетная запись не найдена"    