import matplotlib.pyplot as plt

# Дані за структурою ВВП за регіонами світу у 2020 році
regions = ['World', 'Europe', 'Ukraine']
gdp_share = [100, 22, 0.5]  # У відсотках

# Підписи для секторів
labels = ['World', 'Europe', 'Ukraine']

# Кольори
colors = ['skyblue', 'lightgreen', 'lightcoral']

# Створення кругової діаграми з відображенням значення частки на секторах
plt.figure(figsize=(10, 6))
plt.pie(gdp_share, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Структура ВВП за регіонами світу у 2020 році')
plt.axis('equal')  # Забезпечення круглого вигляду
plt.show()

# Створення кругової діаграми з тінню
plt.figure(figsize=(10, 6))
plt.pie(gdp_share, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, shadow=True)
plt.title('Структура ВВП за регіонами світу у 2020 році з тінню')
plt.axis('equal')  # Забезпечення круглого вигляду
plt.show()

# Створення кругової діаграми з розрізанням
explode = (0.1, 0.1, 0.3)  # Розрізання для кожного сектора
plt.figure(figsize=(10, 6))
plt.pie(gdp_share, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, explode=explode)
plt.title('Структура ВВП за регіонами світу у 2020 році з розрізанням')
plt.axis('equal')  # Забезпечення круглого вигляду
plt.show()
