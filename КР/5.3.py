import numpy as np

# Встановлюємо seed для відтворюваності
np.random.seed(0)

# Створюємо два масиви з 16 елементів із випадковими цілими числами в діапазоні від -10 до 10
A = np.random.randint(-10, 11, 16).reshape(4, 4)
B = np.random.randint(-10, 11, 16).reshape(4, 4)

# Обчислюємо поелементну суму масивів
sum_matrix = A + B

# Обчислюємо добуток масивів
product_matrix = np.dot(A, B)

# Обчислюємо транспоновану матрицю від добутку
transposed_product_matrix = np.transpose(product_matrix)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Sum Matrix:\n", sum_matrix)
print("Product Matrix:\n", product_matrix)
print("Transposed Product Matrix:\n", transposed_product_matrix)

