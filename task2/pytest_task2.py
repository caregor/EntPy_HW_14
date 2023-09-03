import pytest
from src.number import process_number
def test_two_digits():
    result = process_number(45)
    assert result == 'Введено двузначное число. Произведение цифр: 20'


def test_tree_digits():
    result = process_number(867)
    assert result == 'Введено трехзначное число. Зеркальное отображение: 768'

def test_four_digits():
    result = process_number(2678)
    assert result == 'Ошибка: Введено число, не попадающее в диапазон от 1 до 999.'

if __name__ == '__main__':
    pytest.main(['-v'])