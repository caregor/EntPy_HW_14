import unittest
from src.number import process_number


class TestNumber(unittest.TestCase):
    def test_two_digits(self):
        self.assertEqual('Введено двузначное число. Произведение цифр: 12', process_number(34))

    def test_tree_digits(self):
        self.assertEqual('Введено трехзначное число. Зеркальное отображение: 321', process_number(123))

    def test_four_digits(self):
        self.assertEqual('Ошибка: Введено число, не попадающее в диапазон от 1 до 999.', process_number(1001))


if __name__ == '__main__':
    unittest.main(verbosity=2)
