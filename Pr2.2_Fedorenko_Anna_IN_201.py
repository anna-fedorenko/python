import math
# Введення тризначного числа від користувача
number = int(input("Введіть тризначне число: "))
# Піднесення числа до 3-го ступеня
result_kb = number ** 3
# Розрахунок кількості повних мегабайт та гігабайт
megabytes = result_kb // (1024)  # 1 МБ = 1024 КБ
gigabytes = megabytes // (1024)  # 1 ГБ = 1024 МБ
# Закреслення першої цифри зліва та додавання її справа
new_number = int(str(number)[1:] + str(number)[0])
# Знаходження суми і добутку цифр числа
digit_sum = sum(int(digit) for digit in str(number))
digit_product = 1
for digit in str(number):
    digit_product *= int(digit)
# Перестановка цифр сотень і десятків
rearranged_number = int(str(number)[2] + str(number)[1] + str(number)[0])
# Виведення результатів
print("Розмір файлу у МБ:", megabytes)
print("Розмір файлу у ГБ:", gigabytes)
print("Число після закреслення та додавання першої цифри:", new_number)
print("Сума цифр числа:", digit_sum)
print("Добуток цифр числа:", digit_product)
print("Число після перестановки цифр сотень і десятків:", rearranged_number)
