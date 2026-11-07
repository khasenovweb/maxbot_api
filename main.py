import requests

# url = "https://platform-api.max.ru/me"
url = "https://platform-api.max.ru/chats"
headers = {
    "Authorization": "f9LHodD0cOLExkjVgFyn_jtkt8t1Kq11tzkBxIdrSnGl5WwxtMa9sqR6FQX_xsIMFUkUEif8ApPfWioDx7MR"
}

response = requests.get(url, headers=headers)

# Проверяем результат
if response.status_code == 200:
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)