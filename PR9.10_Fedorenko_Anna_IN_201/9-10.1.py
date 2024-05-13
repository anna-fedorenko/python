import numpy as np
import matplotlib.pyplot as plt

# Задаємо інтервал та крок
x = np.arange(-2*np.pi, 2*np.pi, 0.5)
y1 = np.sin(x)
y2 = np.sin(2*x + np.pi/4)
y3 = np.cos(3*x - np.pi/3)

# Побудова графіків
plt.figure(figsize=(10, 6))  # Розмір графіку
plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-', marker='o', markersize=5)  # Графік y1
plt.plot(x, y2, color='green', linestyle='--', marker='s', markersize=5, label='sin(2x + pi/4)')  # Графік y2
plt.plot(x, y3, label='cos(3x - pi/3)', color='red', linestyle='-.', marker='^', markersize=5)  # Графік y3

# Додавання сітки
plt.grid(True)

# Додавання легенди
plt.legend()

# Додавання тексту анотації
plt.annotate('Максимум', xy=(1.57, 1), xytext=(2, 1.1), arrowprops=dict(facecolor='green', arrowstyle='->'))

# Налаштування вісей
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графіки функцій')

# Виведення графіків
plt.show()
