import configuration
import requests
import data

# Создание нового заказа
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers
                         )


response = create_new_order(data.order_body)
print(response.status_code)
print(response.json())

# Сохранить номер заказа

track = response.json()["track"]
print(track)


# Получить заказ по номеру
def get_order_by_number(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params={'t': track})


response = get_order_by_number(track)
print(response.status_code)
print(response.json())