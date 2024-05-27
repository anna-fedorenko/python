# Запитуємо користувача про початок і кінець діапазону
start = int(input("Введіть початок діапазону (start): "))
end = int(input("Введіть кінець діапазону (end): "))

# Перевіряємо, чи start менше або дорівнює end
if start > end:
    print("Помилка: початок діапазону повинен бути меншим або рівним кінцю діапазону.")
else:
    # Обчислюємо суму всіх чисел у діапазоні від start до end включно
    suma = 0
    for number in range(start, end + 1):
        suma += number

    # Виводимо результат
    print(f"Сума чисел у діапазоні від {start} до {end} включно становить: {suma}")
