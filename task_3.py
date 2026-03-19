import requests
import json
import os

URL = "https://www.cbr-xml-daily.ru/daily_json.js"
file = "valute.json"


def loading_valute():
    
    data = requests.get(URL).json()
    return data.get("Valute", {})


def load_groups():
    
    if not os.path.exists(file):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False)
        return []

    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_groups(groups):
    
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(groups, f, ensure_ascii=False)
    print("Сохранено!")


groups = load_groups()

while True:

    print("1 - Все курсы")
    print("2 - Курс по коду")
    print("3 - Мои группы")
    print("4 - Выйти")

    choice = input("Выберите: ")

    if choice == "1":
        data = loading_valute()
        for code, v in data.items():
            print(f"{code}: {v['Value']} руб за {v['Nominal']} {v['Name']}")

    elif choice == "2":
        code = input("Введите код валюты: ").lower()
        data = loading_valute()
        code_upper = code.upper()
        if code_upper in data:
            pl = data[code_upper]
            print(f"{code_upper}: {pl['Value']} руб за {pl['Nominal']} {pl['Name']}")
        else:
            print("Код не найден")

    elif choice == "3":
        while True:

            print("1 - Создать группу")
            print("2 - Добавить валюту")
            print("3 - Удалить валюту")
            print("4 - Показать группы")
            print("5 - Назад")

            choice_move = input("Выберите: ")

            if choice_move == "1":
                name = input("Название группы: ").strip()

                try:
                    for place in groups:
                        if place['name'] == name:
                            raise Exception("данная группа уже существует")

                    if name:
                        groups.append({"name": name, "valute_numer": []})
                        save_groups(groups)
                    else:
                        print("Назовите корректно")

                except Exception as Exceptions:
                    print(Exceptions)

            elif choice_move == "2":
                count = 1
                for place in groups:
                    print(f"{count}. {place['name']}")
                    count = count + 1
                try:
                    numer = int(input("Номер группы: ")) - 1
                    code = input("Код валюты: ").upper()
                    code_upper = code.upper()
                    data = loading_valute()
                    if code_upper not in data:
                        print("Ошибка")
                    elif code_upper in groups[numer]['valute_numer']:
                        print("Валюта уже есть в списке")
                    else:
                        groups[numer]['valute_numer'].append(code_upper)
                        save_groups(groups)
                        print(f"{code_upper} добавлен")
                except:
                    print("Ошибка")

            elif choice_move == "3":
                count = 1
                for place in groups:
                    print(f"{count}. {place['name']}: {', '.join(place['valute_numer'])}")
                    count = count + 1
                try:
                    numer = int(input("Номер группы: ")) - 1
                    code = input("Код для удаления: ").lower()
                    code_upper = code.upper()
                    if code_upper in groups[numer]['valute_numer']:
                        groups[numer]['valute_numer'].remove(code_upper)
                        save_groups(groups)
                        print(f"{code_upper} удален")
                    else:
                        print("Такой валюты нет")
                except:
                    print("Ошибка")

            elif choice_move == "4":
                data = loading_valute()
                for place in groups:

                    print(f"{place['name']}:")
                    if not place['valute_numer']:
                        print("  пусто")
                    for code in place['valute_numer']:
                        v = data.get(code)
                        if v:
                            print(f"{code}: {v['Value']} руб.")

            elif choice_move == "5":
                break

    elif choice == "4":
        print("Доcвидания")
        break