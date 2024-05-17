str_3 = "7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15@@"

# a) Виводимо останні 4 елементи рядка
last_four_elements = str_3[-4:]
print("Останні 4 елементи рядка:", last_four_elements)

# b) Замінюємо символ @ на &
modified_str = str_3.replace('@', '&')
print("Рядок після заміни символу @ на &:", modified_str)

# c) Створюємо список з чисел, які містяться в рядку
import re
numbers_list = re.findall(r'\d+', str_3)
numbers_list = [int(num) for num in numbers_list]
print("Список чисел з рядка:", numbers_list)

# d) Знаходимо суму рядків str_1 та str_3
str_1 = "Remember that the most dangerous prison is the one in your head"
sum_of_strings = len(str_1) + len(str_3)
print("Сума довжин рядків str_1 та str_3:", sum_of_strings)
