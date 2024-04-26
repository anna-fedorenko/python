def print_dict(dictionary):
    for key, value in dictionary.items():
        print(key, ':', value)

def sort_keys_by_values(dictionary):
    return sorted(dictionary.keys(), key=lambda x: dictionary[x])

def sum_of_arguments(*args):
    return sum(args)

def sum_of_list(numbers, **kwargs):
    return sum(numbers)

def average_of_list(*args):
    return sum(args) / len(args)

# Приклад використання:
my_dict = {'b': 2, 'c': 3, 'a': 1}

print("Друк словника та його ключів і значень:")
print_dict(my_dict)

print("Список ключів, впорядкованих за їхніми значеннями в порядку зростання:")
print(sort_keys_by_values(my_dict))

print("Сума позиційних числових аргументів:")
print(sum_of_arguments(1, 2, 3, 4))

print("Сума чисел у списку:")
print(sum_of_list([1, 2, 3, 4]))

print("Середнє значення чисел у списку:")
print(average_of_list(1, 2, 3, 4))


