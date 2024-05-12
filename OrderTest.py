# Альберт Шарафеев, 16-я когорта — Финальный проект. Инженер по тестированию плюс
import req
import body
import requests
import pytest



def test_search_order_by_track():
    response = req.post_new_order(body.order_body)
    track = {"t": response.json()["track"]}
    track_report = req.get_track(track)
    assert track_report.status_code == 200
