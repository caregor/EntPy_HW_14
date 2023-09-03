"""
Задание No6
📌 Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
📌 Передавайте необходимые данные из основного кода проекта.
-------------------------------------------------------------------
Пользовательские классы исключения. Для задач 3,5 и домашней задачи (rectangle.py)
"""


class UserExceptions(Exception):
    pass


class ErrorLevel(UserExceptions):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Уровень доступа пользователя выше вашего уровня - {self.value}.'


class ErrorAccept(UserExceptions):
    def __str__(self):
        return 'Доступ запрещен'


class NoData(UserExceptions):
    pass


class WrongLenData(UserExceptions):
    def __str__(self):
        return 'Неверный формат данных. Пожалуйста, введите имя и ID через пробел.'


class NegativeNumber(UserExceptions):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Сторона прямоугольника не может быть отрицательной. Вы ввели значение: {self.value}'


class RangeError(UserExceptions):
    def __init__(self, value, min_value, max_value):
        self.value = value
        self.max_value = max_value
        self.min_valu = min_value

    def __str__(self):
        return f'Ошибка! Значение должно лежать в промежутке от {self.min_valu} до {self.max_value}. Вы ввели значение: {self.value}'
