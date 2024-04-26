import random

# Генеруємо список цілих випадкових чисел list_1 з 10 елементів з діапазону [-3, 6]
list_1 = [random.randint(-3, 6) for _ in range(10)]

print("Початковий список:", list_1)

# Написати функцію, яка повертає список чисел з list_1, що є кратними заданому числу
def multiples_of_n(lst, n):
    return list(filter(lambda x: x % n == 0, lst))

# Обчислити суму квадратів чисел у списку
sum_of_squares = sum(map(lambda x: x ** 2, list_1))

# Підрахувати кількість парних чисел у списку
count_even_numbers = len(list(filter(lambda x: x % 2 == 0, list_1)))

# Знайти суму всіх непарних чисел у списку
sum_of_odd_numbers = sum(filter(lambda x: x % 2 != 0, list_1))

# Знайти добуток всіх чисел у списку (окрім нулів)
product_of_non_zeros = 1
for num in filter(lambda x: x != 0, list_1):
    product_of_non_zeros *= num

# Видалити всі входження конкретного елемента із списку
def remove_element(lst, element):
    return list(filter(lambda x: x != element, lst))

# Написати функцію, яка обчислює середнє арифметичне значення елементів списку,
# і виводить це значення та всі числа, які більше середнього значення
def above_average(lst):
    avg = sum(lst) / len(lst)
    above_avg = list(filter(lambda x: x > avg, lst))
    return avg, above_avg

# Виклик функцій та вивід результатів
n = int(input("Введіть число для перевірки кратності: "))
print("Числа зі списку, що кратні", n, ":", multiples_of_n(list_1, n))
print("Сума квадратів чисел у списку:", sum_of_squares)
print("Кількість парних чисел у списку:", count_even_numbers)
print("Сума всіх непарних чисел у списку:", sum_of_odd_numbers)
print("Добуток всіх чисел у списку (окрім нулів):", product_of_non_zeros)
element_to_remove = int(input("Введіть число для видалення зі списку: "))
print("Список після видалення елемента", element_to_remove, ":", remove_element(list_1, element_to_remove))
avg, above_avg_numbers = above_average(list_1)
print("Середнє арифметичне значення елементів списку:", avg)
print("Числа зі списку, які більше за середнє значення:", above_avg_numbers)
