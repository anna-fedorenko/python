def main():
    #Запитуємо у користувача три цілі числа
    num1 = int(input("Введіть перше ціле число: "))
    num2 = int(input("Введіть друге ціле число: "))
    num3 = int(input("Введіть третє ціле число: "))
    
    #Знаходимо мінімальне та максимальне значення
    min_num = min(num1, num2, num3)
    max_num = max(num1, num2, num3)
    
    #Знаходимо середнє число
    middle_num = num1 + num2 + num3 - max_num - min_num
    
    #Виводимо числа впорядковані за зростанням
    print("Числа у впорядкованому вигляді за зростанням:", min_num, middle_num, max_num)

if __name__ == "__main__":
    main()
