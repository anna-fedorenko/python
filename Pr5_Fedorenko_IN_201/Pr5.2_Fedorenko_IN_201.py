input_string = "abc83 cde7 1 b 24"

# Із використанням циклу for
print("Із використанням циклу for:")
numbers_for = []
for char in input_string:
    if char.isdigit():
        numbers_for.append(int(char))
print(numbers_for)

# Із використанням циклу while
print("Із використанням циклу while:")
numbers_while = []
index = 0
while index < len(input_string):
    if input_string[index].isdigit():
        numbers_while.append(int(input_string[index]))
    index += 1
print(numbers_while)

# Із використанням спискового включення
print("Спискове включення:")
numbers_list_comprehension = [int(char) for char in input_string if char.isdigit()]
print(numbers_list_comprehension)
