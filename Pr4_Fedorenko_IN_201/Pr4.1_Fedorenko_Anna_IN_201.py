# Сформуємо список list_1 із цілих чисел із діапазону [0, 20] із кроком 2
list_1 = list(range(0, 21, 2))
# Виведемо елементи з непарними індексами
print("Елементи з непарними індексами:")
for i in range(1, len(list_1), 2):
    print(list_1[i], end=" ")
print("\n")
# Виведемо елементи з початку і до 5-го включно, з 3-го і до передостаннього включно з кроком 2
print("Елементи з початку і до 5-го включно, з 3-го і до передостаннього включно з кроком 2:")
print(list_1[:6])
print(list_1[2:-1:2])
print("\n")

# Виведемо елементи списку у зворотному порядку
print("Елементи списку у зворотному порядку з використанням слайдів:")
print(list_1[::-1])

print("Елементи списку у зворотному порядку з використанням методу списків:")
list_1.reverse()
print(list_1)
print("\n")

# Поміняємо місцями перший та останній елементи списку
print("Поміняємо місцями перший та останній елементи списку:")
list_1[0], list_1[-1] = list_1[-1], list_1[0]
print(list_1)
print("\n")

# Перевіримо, чи є число 0 у списку
print("Перевіримо, чи є число 0 у списку:")
if 0 in list_1:
    print("Так, число 0 є у списку.")
else:
    print("Ні, число 0 відсутнє у списку.")
