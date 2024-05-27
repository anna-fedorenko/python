import numpy as np

def search_element(matrix, target):
    matrix = np.array(matrix)
    M, N = matrix.shape
    results = []
    row, col = 0, N - 1

    while row < M and col >= 0:
        if matrix[row, col] == target:
            results.append((row, col))
            # Перевірка всіх можливих входжень у поточному рядку
            r, c = row, col - 1
            while c >= 0 and matrix[r, c] == target:
                results.append((r, c))
                c -= 1
            # Перевірка всіх можливих входжень у поточному стовпці
            r, c = row + 1, col
            while r < M and matrix[r, c] == target:
                results.append((r, c))
                r += 1
            # Продовжуємо пошук з наступного рядка і попереднього стовпця
            row += 1
            col -= 1
        elif matrix[row, col] > target:
            col -= 1
        else:
            row += 1

    return results

# Приклад використання
matrix = [
    [15, 20, 40, 85],
    [20, 35, 80, 95],
    [30, 55, 55, 105],
    [40, 80, 100, 120]
]

target = 55
print(search_element(matrix, target)) 
