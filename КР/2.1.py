def merge_dictionaries(dict1, dict2):
    """
    Функція об'єднує два словники в один.

    :param dict1: Перший вхідний словник
    :param dict2: Другий вхідний словник
    :return: Новий словник, що містить всі пари ключ-значення з обох вхідних словників
    """
    # Створюємо новий словник і об'єднуємо в нього пари ключ-значення з dict1 і dict2
    merged_dict = dict1.copy()  # Копіюємо пари з першого словника
    merged_dict.update(dict2)   # Додаємо пари з другого словника
    
    return merged_dict

# Приклад використання функції
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

result = merge_dictionaries(dict1, dict2)
print(result)
