input_string = "Hello, world!"

# Виведення рядка в зворотньому порядку за допомогою слайсів
print("За допомогою слайсів:", input_string[::-1])

# Виведення рядка в зворотньому порядку за допомогою циклу for
reversed_string_for = ''
for char in input_string:
    reversed_string_for = char + reversed_string_for
print("За допомогою циклу for:", reversed_string_for)

# Виведення рядка в зворотньому порядку за допомогою циклу while
reversed_string_while = ''
index = len(input_string) - 1
while index >= 0:
    reversed_string_while += input_string[index]
    index -= 1
print("За допомогою циклу while:", reversed_string_while)

# Виведення рядка в зворотньому порядку за допомогою методу списків list.reverse()
chars_list = list(input_string)
chars_list.reverse()
reversed_string_method = ''.join(chars_list)
print("За допомогою методу списків list.reverse():", reversed_string_method)
