import requests

url = f"https://platform-api.max.ru/messages?chat_id={206956180}"

headers = {
    "Authorization": "f9LHodD0cOLExkjVgFyn_jtkt8t1Kq11tzkBxIdrSnGl5WwxtMa9sqR6FQX_xsIMFUkUEif8ApPfWioDx7MR",
    "Content-Type": "application/json"
}

data = {
    "text": "Это сообщение с кнопкой-ссылкой",
    "attachments": [
        {
            "type": "inline_keyboard",
            "payload": {
                "buttons": [
                    [
                        {
                            "type": "link",
                            "text": "Откройте сайт",
                            "url": "https://example.com"
                        }
                    ]
                ]
            }
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
