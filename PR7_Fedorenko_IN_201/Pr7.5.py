def indices_and_values_greater_than_10(numbers):
    return [(index, value) for index, value in enumerate(numbers) if value > 10]

def words_to_index_dict(words):
    return {word: index for index, word in enumerate(words)}

def indices_and_even_numbers(numbers):
    return [(index, value) for index, value in enumerate(numbers) if value % 2 == 0]

def split_string_with_indices(string):
    return [(index, word) for index, word in enumerate(string.split())]

def names_starting_with_letter(names, letter):
    return [(index, name) for index, name in enumerate(names) if name.startswith(letter)]

# Приклад використання:

numbers_list = [5, 15, 3, 20, 10, 25]
print("Індекси та значення, які більше 10:", indices_and_values_greater_than_10(numbers_list))

words_list = ["apple", "banana", "orange", "pear"]
print("Словник з індексами слів:", words_to_index_dict(words_list))

print("Індекси та парні числа:", indices_and_even_numbers(numbers_list))

string = "I have a beautiful flowers"
print("Рядки та їхні індекси:", split_string_with_indices(string))

names_list = ["Alice", "Bob", "Charlie", "David"]
letter = "B"
print(f"Імена, що починаються на букву '{letter}':", names_starting_with_letter(names_list, letter))
