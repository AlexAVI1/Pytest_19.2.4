import requests
import json
from user_pass import user, password
from body import body_list, body_username
from headers import headers_login, headers_post, headers_put

# GET. Авторизация пользователя
url_login = 'https://petstore.swagger.io/v2/user/login?'

res = requests.get(f'{url_login}{user}&{password}', headers=headers_login)

print('Статус и информация по запросу GET ', res.status_code)
print(res.json())
print(type(res.json()))

# POST. Создаём список
url_list = f'https://petstore.swagger.io/v2/user/createWithList'

res = requests.post(url_list, headers=headers_post, data=json.dumps(body_list))

print('Статус и информация по запросу POST ', res.status_code)
print(res.json())
print(type(res.json()))

# PUT. Изменяем список
username = 'rambler91'
url = f'https://petstore.swagger.io/v2/user/{username}'

res = requests.put(url, headers=headers_put, data=json.dumps(body_username))

print('Статус и информация по запросу PUT ', res.status_code)
print(res.json())
print(type(res.json()))

# Delete
url = f'https://petstore.swagger.io/v2/user/{username}'

res = requests.delete(url, )

print('Статус и информация по запросу Delete ', res.status_code)
print(res.json())
print(type(res.json()))