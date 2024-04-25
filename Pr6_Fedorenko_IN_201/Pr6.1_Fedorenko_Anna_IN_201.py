import random

# Генеруємо списки
list_1 = [random.randint(-3, 5) for _ in range(8)]
list_2 = [random.randint(2, 10) for _ in range(10)]

# Замінюємо від'ємні елементи list_1 їх абсолютними значеннями та створюємо кортеж tuple_1
tuple_1 = tuple(abs(x) for x in list_1)

# Створюємо список чисел, присутніх в обох списках
common_elements = list(set(list_1) & set(list_2))

# Створюємо кортеж, що об'єднує числа, що присутні в обох списках, без дублікатів
unique_common_elements = tuple(set(common_elements))

# Створюємо список чисел, наявних у списку list_2 та відсутніх у list_1
missing_in_list_1 = [x for x in list_2 if x not in list_1]

# Створюємо кортеж парних чисел, які присутні в обох списках
even_common_elements = tuple(x for x in common_elements if x % 2 == 0)

# Створюємо список чисел, що наявні у list_1 та відсутні у list_2, які більше 3
missing_in_list_2_greater_than_3 = [x for x in list_1 if x not in list_2 and x > 3]

# Виводимо результати
print("list_1:", list_1)
print("list_2:", list_2)
print("tuple_1:", tuple_1)
print("Common elements:", common_elements)
print("Unique common elements:", unique_common_elements)
print("Missing in list_1:", missing_in_list_1)
print("Even common elements:", even_common_elements)
print("Missing in list_2 and greater than 3:", missing_in_list_2_greater_than_3)
