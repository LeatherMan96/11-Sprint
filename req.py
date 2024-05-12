# Альберт Шарафеев, 16-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import config
import body


def post_new_courier():
    url = config.URL_SERVICE + config.CREATE_COURIER_PATH
    return requests.post(url, json=body.courier_body)


def post_new_order(order_body):
    url = config.URL_SERVICE + config.CREATE_ORDER_PATH
    return requests.post(url, json=body.order_body)



def get_track(track):
    url = config.URL_SERVICE + config.FIND_TRACK_PATH
    return requests.get(url, params=track)
