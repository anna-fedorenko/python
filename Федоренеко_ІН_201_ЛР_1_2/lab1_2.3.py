# Створюємо список lst_3 використовуючи range()
lst_3 = list(range(21, 8, -2))

# a) Список квадратів елементів lst_3
result_a = list(map(lambda x: x**2, lst_3))
# або: result_a = [x**2 for x in lst_3]

# b) Список парних елементів lst_3
result_b = list(filter(lambda x: x % 2 == 0, lst_3))
# або: result_b = [x for x in lst_3 if x % 2 == 0]

# c) Список залишків від ділення на 3 елементів lst_3
result_c = list(map(lambda x: x % 3, lst_3))
# або: result_c = [x % 3 for x in lst_3]

# d) Кортеж з елементів lst_3 та їх індексів
result_d = list(zip(lst_3, range(len(lst_3))))

# Виведення результатів
print("a) Список квадратів елементів lst_3:", result_a)
print("b) Список парних елементів lst_3:", result_b)
print("c) Список залишків від ділення на 3 елементів lst_3:", result_c)
print("d) Кортеж з елементів lst_3 та їх індексів:", result_d)
