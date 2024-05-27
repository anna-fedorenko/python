def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return -1, -1  # Порожня матриця
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Починаємо з верхнього правого кута
    row = 0
    col = cols - 1
    
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return row, col  # Знайдено елемент
        elif matrix[row][col] > target:
            col -= 1  # Рухаємося вліво
        else:
            row += 1  # Рухаємося вниз
    
    return -1, -1  # Елемент не знайдено

# Приклад використання
matrix = [
    [15, 20, 40, 85],
    [20, 35, 80, 95],
    [30, 55, 95, 105],
    [40, 80, 100, 120]
]

target = 55

result = search_matrix(matrix, target)
if result != (-1, -1):
    print(f"Елемент {target} знаходиться на позиції {result}")
else:
    print(f"Елемент {target} не знайдений у матриці")

