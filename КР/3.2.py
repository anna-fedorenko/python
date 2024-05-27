def remove_duplicates(lst):
    """
    Функція приймає список чисел та видаляє всі дублікати, зберігаючи початковий порядок елементів.

    :param lst: Вхідний список чисел
    :return: Список без дублікатів з збереженням початкового порядку
    """
    seen = set()
    result = []
    
    for number in lst:
        if number not in seen:
            seen.add(number)
            result.append(number)
    
    return result

# Приклад використання функції
numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
result = remove_duplicates(numbers)
print(result)
