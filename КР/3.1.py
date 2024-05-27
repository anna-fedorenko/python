def common_unique_elements(x, y):
    """
    Функція приймає два списки і повертає список унікальних елементів, що є в обох списках.

    :param x: Перший список цілих чисел
    :param y: Другий список цілих чисел
    :return: Список унікальних елементів, що є в обох списках
    """
    # Перетворюємо списки на множини для отримання унікальних елементів
    set_x = set(x)
    set_y = set(y)
    
    # Знаходимо перетин множин
    common_elements = set_x.intersection(set_y)
    
    # Перетворюємо результат назад у список
    result_list = list(common_elements)
    
    return result_list

# Приклад використання функції
x = [1, 2, 3, 4, 5, 6]
y = [4, 5, 6, 7, 8, 9]

result = common_unique_elements(x, y)
print(result)
