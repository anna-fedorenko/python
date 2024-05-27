def filtered_and_transformed_list(lst, criteria1, criteria2, transform_rule):
    """
    Функція приймає список чисел та два критерії фільтрації. Повертає новий список, що містить числа з вихідного списку,
    які задовольняють обидва критерії фільтрації, та перетворює їх за певним правилом.

    :param lst: Вхідний список чисел
    :param criteria1: Перший критерій фільтрації (функція, яка повертає True або False)
    :param criteria2: Другий критерій фільтрації (функція, яка повертає True або False)
    :param transform_rule: Правило перетворення чисел
    :return: Новий список чисел, що задовольняють обидва критерії фільтрації та перетворені за певним правилом
    """
    result = []
    for number in lst:
        if criteria1(number) and criteria2(number):
            result.append(transform_rule(number))
    return result

# Приклад використання функції
def is_even(n):
    return n % 2 == 0

def is_positive(n):
    return n > 0

def square(n):
    return n ** 2

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
result = filtered_and_transformed_list(numbers, is_even, is_positive, square)
print(result)
