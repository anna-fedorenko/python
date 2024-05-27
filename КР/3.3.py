def average(lst):
    """
    Функція обчислює середнє значення послідовності чисел першого списку, використовуючи генератор для економії пам'яті.

    :param lst: Список чисел
    :return: Середнє значення послідовності чисел
    """
    total = 0
    count = 0
    
    for number in lst:
        total += number
        count += 1
    
    return total / count if count > 0 else 0

# Приклад використання функції
numbers = [1, 2, 3, 4, 5]
result = average(numbers)
print(result)
