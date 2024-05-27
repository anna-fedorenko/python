def search_element(matrix, target):
    if not matrix or not matrix[0]:
        return []

    M = len(matrix)
    N = len(matrix[0])
    results = []
    row = 0
    col = N - 1

    while row < M and col >= 0:
        if matrix[row][col] == target:
            # Зберігаємо знайдений елемент
            results.append((row, col))

            # Перевірка всіх можливих входжень у поточному рядку
            c = col - 1
            while c >= 0 and matrix[row][c] == target:
                results.append((row, c))
                c -= 1

            # Перевірка всіх можливих входжень у поточному стовпці
            r = row + 1
            while r < M and matrix[r][col] == target:
                results.append((r, col))
                r += 1

            # Продовжуємо пошук з наступного рядка і попереднього стовпця
            row += 1
            col -= 1

        elif matrix[row][col] > target:
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

