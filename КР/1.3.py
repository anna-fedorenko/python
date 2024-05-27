import math

# Запитуємо користувача про число n
n = int(input("Введіть число n для перевірки, чи є воно простим: "))

# Перевіряємо, чи є n простим числом
if n <= 1:
    print("Число повинно бути більше 1.")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"Число {n} є простим.")
    else:
        print(f"Число {n} не є простим.")
