# Створимо список list_3 для прикладу
list_3 = [1, 2, 'a', 'b', 3, 4, 'c']

# Створимо список list_4, що складається тільки з чисел
list_4 = []
for item in list_3:
    if isinstance(item, int):
        list_4.append(item)

# Виведемо всі додатні елементи списку list_4
positive_elements = [x for x in list_4 if x > 0]

# Створимо список квадратів елементів списку list_4
squares = [x ** 2 for x in list_4]

# Виведемо елементи списку list_3, які є літерами, у верхньому регістрі
upper_case_letters = [x.upper() for x in list_3 if isinstance(x, str)]

print("list_4 (тільки числа):", list_4)
print("Додатні елементи list_4:", positive_elements)
print("Квадрати елементів list_4:", squares)
print("Літери у верхньому регістрі:", upper_case_letters)
