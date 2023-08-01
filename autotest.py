# Туршукова Ксения, 7-я когорта - Финальный проект. Инженер по тестированию плюс.

import sender_stand_request

# Проверка кода 200
def positive_200(track):
    response = sender_stand_request.get_order_by_number(track)
    assert response.status_code == 200
    print(sender_stand_request.track)


# Запрос на существующий номер заказа
def test_get_order_by_number_success_response():
    positive_200(sender_stand_request.track)
    print(sender_stand_request.track)