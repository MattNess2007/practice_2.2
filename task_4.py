import requests


def github(endpoint):
    url = f"https://api.github.com{endpoint}"
    headers = {
        'User-Agent': 'Mozilla/5.0',
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response.json()
    except:
        print("Ошибка запроса")
        return None


def user_comment(username):

    data = github(f"/search/issues?q=commenter:{username}")
    if data and isinstance(data, dict):
        return data.get('total_count', 0)
    return 0


def user_info(username):

    print(f"Профиль {username}")
    data = github(f"/users/{username}")
    if data and isinstance(data, dict) and 'login' in data:
        comment = user_comment(username)
        print(f"Имя: {data.get('name', 'Не указано')}")
        print(f"Ссылка: {data.get('html_url')}")
        print(f"Репозитории: {data.get('public_repos')}")
        print(f"Комментарии: {comment}")
        print(f"Подписчики: {data.get('followers')}")
        print(f"Подписки: {data.get('following')}")


def user_reposit(username):

    print(f"Репозитории {username}")
    data = github(f"/users/{username}/repos")

    if isinstance(data, list):
        if not data:
            print("У пользователя нет публичных репозиториев")
            return

        for inf in data:
            if isinstance(inf, dict):
                print(f"\nНазвание: {inf.get('name', 'Не указано')}")
                print(f"Ссылка: {inf.get('html_url', 'Не указана')}")
                print(f"Язык: {inf.get('language', 'Не указан')}")
                print(f"Видимость: {'Публичный' if not inf.get('private', True) else 'Приватный'}")
                print(f"Ветка: {inf.get('default_branch', 'Не указана')}")
    elif isinstance(data, dict) and 'message' in data:
        print(f"Ошибка API: {data.get('message')}")
    else:
        print("Не удалось получить список репозиториев")


def search_reposit(query):

    print(f"Поиск: {query}")
    data = github(f"/search/repositories?q={query}")

    if isinstance(data, dict) and data.get('items'):
        print(f"Найдено: {data['total_count']}")
        for repo in data['items'][:5]:
            if isinstance(repo, dict):
                print(f"\n• {repo.get('full_name', 'Не указано')}")
                print(f"  {repo.get('html_url', 'Не указана')}")
    else:
        print("Ничего не найдено или ошибка запроса")


while True:
    print("1 - Профиль")
    print("2 - Репозитории")
    print("3 - Поиск")
    print("4 - Выход")

    choice = input("Выберите: ")

    if choice == "1":
        name = input("Имя пользователя: ").strip()
        if name: user_info(name)
    elif choice == "2":
        name = input("Имя пользователя: ").strip()
        if name: user_reposit(name)
    elif choice == "3":
        query = input("Поисковый запрос: ").strip()
        if query: search_reposit(query)
    elif choice == "4":
        print("Досвидания")
        break
