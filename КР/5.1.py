import numpy as np

# Генеруємо два масиви NumPy розміром 4x4 з випадковими цілими числами у діапазоні від -10 до 10
array1 = np.random.randint(-10, 11, size=(4, 4))
array2 = np.random.randint(-10, 11, size=(4, 4))

# Створюємо матриці A та B з цих масивів
matrix_A = np.array(array1)
matrix_B = np.array(array2)

print("Матриця A:")
print(matrix_A)
print("\nМатриця B:")
print(matrix_B)
