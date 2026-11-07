import requests

url = "https://platform-api.max.ru/subscriptions"
headers = {
    "Authorization": "f9LHodD0cOLExkjVgFyn_jtkt8t1Kq11tzkBxIdrSnGl5WwxtMa9sqR6FQX_xsIMFUkUEif8ApPfWioDx7MR"
}

data = {
    "url": "https://lead-widget.ru/api/v1/main/max/webhook/",
    "update_types": ["message_created", "bot_started"],
    "secret": "PQstAqw5xGHjj0mCuXuaBWfUcPFjkkbHq0HREuv1SWZ"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Webhook успешно установлен!")
    print(response.json())
else:
    print(f"Ошибка {response.status_code}: {response.text}")
