import requests

urls = [
    "https://github.com/",
    "https://www.binance.com/en",
    "https://tomtit.tomsk.ru/",
    "https://jsonplaceholder.typicode.com/",
    "https://moodle.tomtit-tomsk.ru/"
]


for url in urls:
    try:

        response = requests.get(url)
        code = response.status_code

        if code == 200:
            status = "доступен"
        elif code == 403:
            status = "вход запрещен"
        elif code == 404:
            status = "не найден"
        elif code >= 500:
            status = "ошибка сервера"
        else:
            status = f"код {code}"

    except requests.exceptions.ConnectionError:
        status = "не доступен"
        code = "ошибка соединения"
    except Exception:
        status = "ошибка"
        code = "неизвестная ошибка"


    print(f"{url} – {status} – {code}")