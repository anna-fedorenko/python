# Функція для обчислення площі прямокутника
def rectangle_area(width, height):
    return width * height

# Функція для виведення вітання з ім'ям та віком користувача
def greet_user(name, age):
    return f"Hello, {name}! You are {age} years old."

# Функція для обчислення добутку двох чисел
def multiply_numbers(a, b):
    return a * b

# Функція для обчислення середнього арифметичного чисел у списку
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Функція для додавання двох чисел
def add_numbers(a, b):
    return a + b

# Функція для фільтрації чисел, які діляться на певне число
def filter_divisible_numbers(divider, numbers):
    return [num for num in numbers if num % divider == 0]

# Приклад використання функцій:
print("Rectangle Area:", rectangle_area(width=5, height=3))
print("Greeting:", greet_user(name="Alice", age=25))
print("Product:", multiply_numbers(4, b=7))
print("Average:", calculate_average([1, 2, 3, 4, 5]))
print("Sum:", add_numbers(10, 20))
print("Filtered Numbers:", filter_divisible_numbers(divider=3, numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
