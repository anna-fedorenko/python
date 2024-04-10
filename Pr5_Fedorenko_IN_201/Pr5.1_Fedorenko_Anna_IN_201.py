def calculate_sum(x, n):
    sum_result = 0
    for i in range(1, n + 1):
        term = ((-1) ** (i - 1)) * (x ** i) / i
        sum_result += term
        if i > 1:
            # Перевіряємо різницю між поточним і попереднім доданками
            if abs(term) < 0.01 * abs(sum_result):
                break
    return sum_result, i

def main():
    x = float(input("Введіть дійсне число x: "))
    n = 10  # За завданням n=10
    while True:
        if 0.5 <= x <= 3:
            sum_result, iterations = calculate_sum(x, n)
            print(f"Сума: {sum_result}, n = {iterations}")
            break
        else:
            print("Число x повинно бути в межах [0.5, 3]")
            x = float(input("Введіть дійсне число x: "))

if __name__ == "__main__":
    main()
    