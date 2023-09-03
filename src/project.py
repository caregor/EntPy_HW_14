import json
from .error import NoData, WrongLenData, ErrorAccept, ErrorLevel, RangeError

from .person import Person


def get_user_data():
    user_input = input("Введите имя и ID через пробел: ")
    data = user_input.split()
    if len(data) != 2:
        raise WrongLenData
    else:
        name, id = data
        return name, id


def add_to_bd(filename, current_data):
    name, user_id, level = current_data.split()

    if not (1 < int(level) < 8):
        raise RangeError(level, 1,8)

    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[str(level)] = {str(user_id): name}

    with open(filename, "w") as file:
        json.dump(data, file, indent=2)


class Project:
    def __init__(self, file_db='../db/test_db.json'):
        self.users = set()
        self.file_db = file_db
        self.get_users()

    def add_user(self, user):
        self.users.add(user)

    def login(self, name, uid):
        user_to_login = Person(name, uid, None)

        for user in self.users:
            if user == user_to_login:
                return user.level

        raise ErrorAccept

    def get_users(self):

        try:
            with open(self.file_db, 'r', encoding='utf-8') as fj:
                dict_bd = json.load(fj)

            for level, subdict in dict_bd.items():
                for id_cod, name in subdict.items():
                    self.add_user(Person(name, id_cod, level))

        except FileNotFoundError:
            NoData

    def add_new_user(self, data_new_user, current_user_level):
        name, id, level = data_new_user.split()
        if int(level) >= current_user_level:
            add_to_bd(self.file_db, data_new_user)
        else:
            raise ErrorLevel(current_user_level)
        return "Пользователь добавлен"


if __name__ == '__main__':
    access = Project()

    try:
        name, uid = get_user_data()
        user_level = access.login(name, uid)
        print(f"Добро пожаловать, Ваш уровень доступа {user_level}!")

        current_data = input(f'Введите имя, id, уровень доступа(1 - 7) через пробел: \n ')
        access.add_new_user(current_data, user_level)
    except Exception as e:
        print(e)
