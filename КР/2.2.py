def merge_and_sort_dictionaries(dict1, dict2):
    """
    Функція об'єднує два словники в один і сортує пари ключ-значення за ключами в алфавітному порядку.

    :param dict1: Перший вхідний словник
    :param dict2: Другий вхідний словник
    :return: Новий словник, що містить всі пари ключ-значення з обох вхідних словників, відсортовані за ключами
    """
    # Створюємо новий словник і об'єднуємо в нього пари ключ-значення з dict1 і dict2
    merged_dict = dict1.copy()  # Копіюємо пари з першого словника
    merged_dict.update(dict2)   # Додаємо пари з другого словника
    
    # Сортуємо об'єднаний словник за ключами
    sorted_merged_dict = dict(sorted(merged_dict.items()))
    
    return sorted_merged_dict

# Приклад використання функції
dict1 = {'b': 2, 'a': 1, 'c': 3}
dict2 = {'f': 6, 'd': 4, 'e': 5}

result = merge_and_sort_dictionaries(dict1, dict2)
print(result)
