import math
# Запитати користувача на введення двох цілих чисел a і b
a = int(input("Введіть перше число a: "))
b = int(input("Введіть друге число b: "))
# Обчислити результати математичних операцій
сума = a + b
різниця = a - b
добуток = a * b
ділення = round(a / b, 2)
залишок = a % b
логарифм = round(math.log10(a), 2)
піднесення_до_степеня = a ** b
квадратний_корінь = round(math.sqrt(a ** b), 2)
# Поміняти значення a та b місцями
a, b = b, a
# Вивести результати
print("Сума:", сума)
print("Різниця між a і b:", різниця)
print("Добуток:", добуток) 
print("Ділення a на b:", ділення)
print("Залишок від ділення a на b:", залишок)
print("Десятковий логарифм числа a:", логарифм)
print("Результат піднесення числа a в ступінь b:", піднесення_до_степеня)
print("Квадратний корінь з числа a (після попередньої операції):", квадратний_корінь)
print("Після обміну значень a та b:", "a =", a, ", b =", b)
