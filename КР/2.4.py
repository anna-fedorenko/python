def merge_and_sort_dictionaries(dict1, dict2):
    """
    Функція об'єднує два словники в один, обробляючи дубльовані ключі,
    і сортує пари ключ-значення за ключами в алфавітному порядку.

    :param dict1: Перший вхідний словник
    :param dict2: Другий вхідний словник
    :return: Новий словник, що містить всі пари ключ-значення з обох вхідних словників, відсортовані за ключами,
             або повідомлення про помилку, якщо ключі не є рядками.
    """
    # Перевірка типів ключів у першому словнику
    for key in dict1:
        if not isinstance(key, str):
            return "Помилка: всі ключі у першому словнику повинні бути рядками."
    
    # Перевірка типів ключів у другому словнику
    for key in dict2:
        if not isinstance(key, str):
            return "Помилка: всі ключі у другому словнику повинні бути рядками."
    
    # Створюємо новий словник і об'єднуємо в нього пари ключ-значення з dict1 і dict2
    merged_dict = dict1.copy()  # Копіюємо пари з першого словника
    
    # Додаємо пари з другого словника, замінюючи значення дубльованих ключів
    for key, value in dict2.items():
        merged_dict[key] = value
    
    # Сортуємо об'єднаний словник за ключами
    sorted_merged_dict = dict(sorted(merged_dict.items()))
    
    return sorted_merged_dict

# Приклад використання функції
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'd': 4, 'e': 5}

result = merge_and_sort_dictionaries(dict1, dict2)
print(result)

# Приклад використання функції з нестроковими ключами
dict1_invalid = {1: 'one', 2: 'two'}
dict2_invalid = {'b': 20, 'd': 4, 'e': 5}

result_invalid = merge_and_sort_dictionaries(dict1_invalid, dict2_invalid)
print(result_invalid)
