import requests

# Запрос всех возможно доступных питомцев
status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})

# Вывод кода ответа запроса
print(res.status_code)

# Создание нового питомца
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

data = {"id": 1686629964416770296, "category": {"id": 0, "name": "string"},
        "name": "Vasya", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}],
        "status": "available"}

res = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, json=data)

# Вывод кода ответа запроса и данных о созданном питомце
print(res.status_code)
print(res.json())

# Изменение данных о питомце
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

data = {"id": 1686629964416770296, "category": {"id": 0, "name": "string"},
        "name": "VaNya", "photoUrls": "string", "tags": {"id": 0, "name": "string"},
        "status": "available"}

# Удаление созданного питомца
res = requests.delete(f'https://petstore.swagger.io/v2/pet/{1686629964416770296}',
                      headers={'accept': 'application/json'})

# Вывод кода ответа запроса и данных об удаленном питомце
print(res.status_code)
print(res.json())

# Запросить всех зверят в available-статусе
status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}',
                   headers={'accept': 'application/json'})

# Вывод кода ответа запроса
print(res.status_code)