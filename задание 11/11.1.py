import json
import requests
username = 'NixOS'
url = f'https://api.github.com/users/{username}'
user_data = requests.get(url).json()
dict_with_info = {
    'company': user_data.get('company'),
    'created_at': user_data.get('created_at'),
    'email': user_data.get('email'),
    'id': user_data.get('id'),
    'name': user_data.get('name'),
    'url': user_data.get('url')
}
with open('Вывод_информации_с_гитхаба.txt', 'w') as info:
    for key, value in dict_with_info.items():
        info.write("'{}':'{}'\n".format(key, value))