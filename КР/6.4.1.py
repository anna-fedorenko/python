import numpy as np

def search_element(matrix, target):
    matrix = np.array(matrix)
    M, N = matrix.shape
    row, col = 0, N - 1

    while row < M and col >= 0:
        if matrix[row, col] == target:
            return row, col
        elif matrix[row, col] > target:
            col -= 1
        else:
            row += 1

    return None

# Приклад використання
matrix = [
    [15, 20, 40, 85],
    [20, 35, 80, 95],
    [30, 55, 95, 105],
    [40, 80, 100, 120]
]

target = 55
print(search_element(matrix, target))  # Очікуваний результат: (2, 1)
