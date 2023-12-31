import requests

# Запрос всех возможно доступных питомцев
status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})

# Код ответа запроса и все питомцы
print(res.status_code)
print(res.json())

# Новый питомец
headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}

data = {"id": 1686629964416770296,
        "category": {"id": 0, "name": "string"},
        "name": "Vasya", "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available"
        }

res = requests.post('https://petstore.swagger.io/v2/pet',
                    headers=headers, json=data)

# Код ответа запроса и данные о созданном питомце
print(res.status_code)
print(res.json())

# Изменим данные о питомце
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

data = {"id": 1686629964416770296,
        "category": {"id": 0, "name": "string"},
        "name": "VaNya",
        "photoUrls": "string",
        "tags": {"id": 0, "name": "string"},
        "status": "available"
        }

# Удалим созданного питомца
res = requests.delete(f'https://petstore.swagger.io/v2/pet/{1686629964416770296}',
                      headers={'accept': 'application/json'})

# Код ответа запроса и данные об удаленном питомце
print(res.status_code)
print(res.json())

status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}',
                   headers={'accept': 'application/json'})

# Вывод кода ответа запроса
print(res.status_code)
print(res.json())
