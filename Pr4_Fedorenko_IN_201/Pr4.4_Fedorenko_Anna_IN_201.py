# Заданий список list_3
list_3 = [-7, 0, 7, 3, -1, 0, 3, 7, -6, 5, 'A', 'b', 'Bd', '12a057cdF#']
print("Заданий список list_3:", list_3)

# Сформувати список list_4, що складається тільки з чисел
list_4 = [x for x in list_3 if isinstance(x, int)]
print("Список list_4, що складається тільки з чисел:", list_4)

# Вивести всі додатні елементи списку list_4 за допомогою спискового включення
positive_numbers = [x for x in list_4 if x > 0]
print("Додатні елементи списку list_4 за допомогою спискового включення:", positive_numbers)

# Вивести всі додатні елементи списку list_4 за допомогою функції filter та map
positive_numbers_filtered = list(filter(lambda x: x > 0, list_4))
print("Додатні елементи списку list_4 за допомогою функції filter та map:", positive_numbers_filtered)

# Створити список квадратів елементів списку list_4
squares_list_4 = [x**2 for x in list_4]
print("Список квадратів елементів списку list_4:", squares_list_4)

# Вивести елементи списку list_3, які є літерами, у верхньому регістрі за допомогою спискового включення
upper_case_letters = [x.upper() for x in list_3 if isinstance(x, str) and x.isalpha()]
print("Елементи списку list_3, які є літерами, у верхньому регістрі за допомогою спискового включення:", upper_case_letters)

# Вивести елементи списку list_3, які є літерами, у верхньому регістрі за допомогою функції filter та map
upper_case_letters_filtered = list(map(lambda x: x.upper(), filter(lambda x: isinstance(x, str) and x.isalpha(), list_3)))
print("Елементи списку list_3, які є літерами, у верхньому регістрі за допомогою функції filter та map:", upper_case_letters_filtered)
