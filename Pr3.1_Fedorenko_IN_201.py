# Заданий рядок
full_name = "Федоренко Анна Сергіївна"

# Довжина рядка та кількість пробілів
length = len(full_name)
spaces_count = full_name.count(' ')

# Виведення довжини та кількості пробілів
print("Довжина рядка:", length)
print("Кількість пробілів у рядку:", spaces_count)

# Виведення імені та прізвища
name_parts = full_name.split()
name_surname = f"{name_parts[1]} {name_parts[0]}"
print("Ім'я та прізвище:", name_surname)

# Виведення ініціалів
initials = ''.join([part[0] for part in name_parts])
print("Ініціали:", initials)

# Зробити усі літери прописними
uppercase_full_name = full_name.upper()
print("Усі літери прописні:", uppercase_full_name)

# Вставка коми та дати народження
birth_date = "2004.11.01"
formatted_full_name = f"{full_name}, {birth_date}"
print("Рядок з доданою комою та датою народження:", formatted_full_name)
