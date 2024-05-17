# a) Ініціалізація множин для чисел, що діляться на 3, 5, або обидва, та множини для інших чисел
fizz = set()
buzz = set()
fizzbuzz = set()
others = set()

# Прохід по числах від 1 до 50
for num in range(1, 51):
    # Перевірка подільності числа на 3 та 5
    if num % 3 == 0 and num % 5 == 0:
        fizzbuzz.add(num)  # Додаємо число до множини для FizzBuzz
    # Перевірка подільності числа на 3
    elif num % 3 == 0:
        fizz.add(num)  # Додаємо число до множини для Fizz
    # Перевірка подільності числа на 5
    elif num % 5 == 0:
        buzz.add(num)  # Додаємо число до множини для Buzz
    else:
        others.add(num)  # Додаємо число до множини для Others (якщо не подільне на 3 або 5)

# b) Створення множини чисел, які є у Fizz, але відсутні у Buzz
fizz_not_buzz = fizz - buzz

# c) Створення списку перетину множин Fizz та Buzz
fizz_and_buzz = list(fizz & buzz)

# d) Створення списку об'єднання множин Fizz та Buzz
fizz_or_buzz = list(fizz | buzz)

# Виведення результатів
print("Множина Fizz:", fizz)
print("Множина Buzz:", buzz)
print("Множина FizzBuzz:", fizzbuzz)
print("Множина Others:", others)
print("Множина чисел у Fizz, але не у Buzz:", fizz_not_buzz)
print("Список перетину множин Fizz та Buzz:", fizz_and_buzz)
print("Список об'єднання множин Fizz та Buzz:", fizz_or_buzz)
