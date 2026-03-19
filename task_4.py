import requests


def github(username):
    url = f"https://api.github.com{username}"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Authorization': 'token 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'
    }
    try:
        response = requests.get(url, headers=headers)
        return response.json()
    except:
        print("Ошибка запроса")
        return None


def user_comments(username):

    data = github(f"/search/issues?q=commenter:{username}")
    return data.get('total_count', 0)


def user_profile(username):

    print(f"\nАккаунт {username}")
    data = github(f"/users/{username}")
    if data:
        comments = user_comments(username)

        print(f"Имя: {data.get('name', 'Не указано')}")
        print(f"Ссылка: {data.get('html_url')}")
        print(f"Репозитории: {data.get('public_repos')}")
        print(f"Обсуждения (комментарии): {comments}")
        print(f"Подписчики: {data.get('followers')}")
        print(f"Подписки: {data.get('following')}")


def user_reposit(username):
    print(f"\nРепозитории {username}")
    data = github(f"/users/{username}/repos")
    if data:
        for inf in data:
            print(f"\nНазвание: {inf['name']}")
            print(f"Ссылка: {inf['html_url']}")
            print(f"Язык: {inf.get('language', 'Не указан')}")
            print(f"Видимость: {'Публичный' if not inf['private'] else 'Приватный'}")
            print(f"Ветка по умолчанию: {inf.get('default_branch', 'Не указана')}")


def search_reposit(comment):
    print(f"\n--- Поиск: {comment} ---")
    data = github(f"/search/repositories?q={comment}")
    if data and 'items' in data and data['items']:
        print(f"Найдено: {data['total_count']}")
        for inf in data['items'][:7]:
            print(f"\n{inf['full_name']}")
            print(f"{inf['html_url']}")
    else:
        print("Ничего не найдено")


while True:
    print("1 Профиль")
    print("2 Репозитории")
    print("3 Поиск")
    print("4 Выход")

    choice = input("Выберите: ")

    if choice == "1":
        name = input("Имя пользователя: ").strip()
        if name: user_profile(name)
    elif choice == "2":
        name = input("Имя пользователя: ").strip()
        if name: user_reposit(name)
    elif choice == "3":
        query = input("Поисковый запрос: ").strip()
        if query: search_reposit(query)
    elif choice == "4":
        print("Досвидания")
        break