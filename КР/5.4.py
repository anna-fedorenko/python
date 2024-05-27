import numpy as np

# Створюємо два масиви NumPy з випадковими цілими числами в діапазоні від -10 до 10
array_A = np.random.randint(-10, 11, size=16)
array_B = np.random.randint(-10, 11, size=16)

# Виводимо початкові масиви
print("Початковий масив A:")
print(array_A)
print("\nПочатковий масив B:")
print(array_B)

# Змінюємо форму матриці B
reshaped_B_1 = array_B.reshape(2, 8)
reshaped_B_2 = array_B.reshape(16, 1)
reshaped_B_3 = array_B.reshape(16)

# Виводимо отримані матриці B з різними формами
print("\nМатриця B з формою (2, 8):")
print(reshaped_B_1)
print("\nМатриця B з формою (16, 1):")
print(reshaped_B_2)
print("\nМатриця B з формою (16,):")
print(reshaped_B_3)
