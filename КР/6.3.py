def search_element(matrix, target):
    if not matrix or not matrix[0]:
        return []

    M = len(matrix)
    N = len(matrix[0])
    results = []
    closest_diff = float('inf')
    closest_elements = []
    row = 0
    col = N - 1

    while row < M and col >= 0:
        current_element = matrix[row][col]
        current_diff = abs(current_element - target)

        if current_diff < closest_diff:
            closest_diff = current_diff
            closest_elements = [(row, col)]
        elif current_diff == closest_diff:
            closest_elements.append((row, col))

        if current_element == target:
            results.append((row, col))
            col -= 1  # Продовжуємо пошук вліво в поточному рядку
        elif current_element > target:
            col -= 1
        else:
            row += 1

    return results if results else closest_elements

# Приклад використання
matrix = [
    [15, 20, 40, 85],
    [20, 35, 80, 95],
    [30, 55, 95, 105],
    [40, 80, 100, 120]
]

# Випадок, коли елемент є
target = 55
print(search_element(matrix, target))

# Випадок, коли елемента нема
target = 83
print(search_element(matrix, target))
