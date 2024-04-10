# Сформуємо список list_5 з 12 елементів: 8 цілих чисел та 4 рядки
list_5 = [1, 0, "AbxT", 9, -6, "j", -1, "qkl", 8, 5, 0, "riT"]

# Створимо список list_6 з 8 числових елементів, 
# в яких кожен елемент дорівнює середньому арифметичному 
# наступних числових елементів списку list_5
list_6 = []
strings = []

for i in range(len(list_5)):
    if isinstance(list_5[i], int):
        total = 0
        count = 0
        for j in range(i + 1, len(list_5)):
            if isinstance(list_5[j], int):
                total += list_5[j]
                count += 1
        if count > 0:
            avg = round(total / count, 2)
            list_6.append(avg)
        else:
            list_6.append(0)
    elif isinstance(list_5[i], str) and len(list_5[i]) > 2:
        strings.append(list_5[i])

print("list_6:", list_6)
print("Рядки з довжиною більше 2:", strings)
