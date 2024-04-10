input_string = "abc83 cde7 1 b 24"
# З використанням циклу for
print("З використанням циклу for:")
numbers_for = []
current_number = ''
for char in input_string:
    if char.isdigit():
        current_number += char
    elif current_number:
        numbers_for.append(int(current_number))
        current_number = ''
if current_number:
    numbers_for.append(int(current_number))
print(numbers_for)
# З використанням циклу while
print("З використанням циклу while:")
numbers_while = []
index = 0
current_number = ''
while index < len(input_string):
    if input_string[index].isdigit():
        current_number += input_string[index]
    elif current_number:
        numbers_while.append(int(current_number))
        current_number = ''
    index += 1
if current_number:
    numbers_while.append(int(current_number))
print(numbers_while)
