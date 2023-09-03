def process_number(number):
    """
    >>> process_number(34)
    'Введено двузначное число. Произведение цифр: 12'
    >>> process_number(123)
    'Введено трехзначное число. Зеркальное отображение: 321'
    >>> process_number(1000)
    'Ошибка: Введено число, не попадающее в диапазон от 1 до 999.'
    """

    if 1 <= number <= 9:
        square = number ** 2
        return f"Введено однозначное число. Квадрат числа: {square}"
    elif 10 <= number <= 99:
        digit1 = number // 10
        digit2 = number % 10
        product = digit1 * digit2
        return f"Введено двузначное число. Произведение цифр: {product}"
    elif 100 <= number <= 999:
        reversed_number = int(str(number)[::-1])
        return f"Введено трехзначное число. Зеркальное отображение: {reversed_number}"
    else:
        return "Ошибка: Введено число, не попадающее в диапазон от 1 до 999."

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
