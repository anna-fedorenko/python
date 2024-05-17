def is_divisible_by_6(number):
    # Перевірка на від’ємність
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)  # Взяття модуля від числа для спрощення подальшого обрахунку
    
    # Перевірка останньої цифри
    last_digit = number % 10  # Отримання останньої цифри числа
    if last_digit % 2 != 0:  # Перевірка, чи є остання цифра парною
        return f"Число {number} неподільне на 6"
    
    # Перевірка суми всіх цифр
    digit_sum = sum(int(digit) for digit in str(number))  # Сума всіх цифр числа
    if digit_sum % 3 != 0:  # Перевірка, чи сума цифр ділиться на 3
        return f"Число {number} неподільне на 6"
    
    # Повернення результату в залежності від від’ємності числа
    return f"Число {number} ділиться на 6" if not is_negative else f"Число {-number} ділиться на 6"

# Тестування функції для списку lst_2
lst_2=[-7, 24, 9, -1, 5, 6, -56, -18, 5, 5]
results = list(map(is_divisible_by_6, lst_2))  # Застосування функції до кожного елементу списку
print(results)  # Виведення результатів
