from collections import defaultdict

# Введений рядок
text = "Take the first step in faith. You don’t have to see the whole staircase, just take the first step. Only two things are infinite — the universe and human stupidity, and I’m not sure about the former"

# Видаляємо знаки пунктуації та пробіли і перетворюємо всі літери в нижній регістр
cleaned_text = ''.join(char.lower() for char in text if char.isalpha())

# Створення словника для підрахунку кількості входжень кожної букви
char_count = defaultdict(int)
for char in cleaned_text:
    char_count[char] += 1

# Виведення довжини словника та всіх пар ключ-значення
print("Довжина словника:", len(char_count))
print("Пари ключ-значення:")
for char, count in char_count.items():
    print(char, "-", count)

# Визначення кількості разів зустрічання літер 'a' та 'j'
count_a = char_count['a']
count_j = char_count['j']
print("Кількість 'a':", count_a)
print("Кількість 'j':", count_j)

# Знаходження букви, яка найчастіше зустрічалася у рядку
most_common_char = max(char_count, key=char_count.get)
print("Найчастіше зустрічалася буква:", most_common_char)

# Знаходження букви, яка найрідше зустрічалася у рядку
least_common_char = min(char_count, key=char_count.get)
print("Найрідше зустрічалася буква:", least_common_char)

# Додавання літер, які не зустрічались, до словника зі значенням 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in alphabet:
    if char not in char_count:
        char_count[char] = 0

# Виведення оновленого словника з усіма літерами алфавіту
print("Оновлений словник з усіма літерами алфавіту:")
for char, count in sorted(char_count.items()):
    print(char, "-", count)
