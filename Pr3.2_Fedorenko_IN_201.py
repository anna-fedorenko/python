# Заданий рядок
string = "https://istories.media/workshops/2020/11/11/vvedenie-v-python-chast-2-stroki/"

# Чи складається рядок із цифр
is_digits = any(char.isdigit() for char in string)

# Чи складається рядок із цифр або букв
is_alpha_numeric = any(char.isalnum() for char in string)

# Чи складається рядок із символів у нижньому регістрі
is_lower_case = any(char.islower() for char in string)

# Чи складається рядок із символів, що не відображаються
contains_non_printable = any(not char.isprintable() for char in string)

# Чи містить цей рядок підрядок “11”
contains_substring_11 = "11" in string

# Виведення результатів
print("Чи складається рядок із цифр:", is_digits)
print("Чи складається рядок із цифр або букв:", is_alpha_numeric)
print("Чи складається рядок із символів у нижньому регістрі:", is_lower_case)
print("Чи складається рядок із символів, що не відображаються:", contains_non_printable)
print("Чи містить цей рядок підрядок “11”:", contains_substring_11)

