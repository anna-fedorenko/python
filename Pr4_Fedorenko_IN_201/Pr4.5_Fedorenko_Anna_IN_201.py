# Сформуємо список list_5 з 12 елементів
list_5 = [1, 1, "ASbvsxT", 2, 4, "A", -1, "qq", 7, 2, 0, "qweT"]
print("Список list_5:", list_5)

# Ініціалізуємо список list_6
list_6 = []

# Проходимо по елементам списку list_5
for i in range(len(list_5)):
    # Якщо елемент - ціле число
    if isinstance(list_5[i], int):
        # Обчислюємо середнє арифметичне наступних числових елементів списку list_5
        next_numbers = [x for x in list_5[i+1:] if isinstance(x, int)]
        if next_numbers:
            average = sum(next_numbers) / len(next_numbers)
            list_6.append(round(average, 2))

print("Список list_6 з середніми значеннями:", list_6)

# Створимо список рядків з елементів списку list_5
list_of_strings = [str(x) for x in list_5 if isinstance(x, str)]

# Виведемо рядки з довжиною більше 2
filtered_strings = [string for string in list_of_strings if len(string) > 2]
print("Рядки з довжиною більше 2:", filtered_strings)
