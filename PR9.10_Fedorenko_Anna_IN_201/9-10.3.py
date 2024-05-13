import matplotlib.pyplot as plt

# Дані для країн 3-ї групи (роки вступу 2004 року та пізніше)
countries = ['Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Estonia', 'Hungary', 'Latvia', 'Lithuania', 'Malta', 'Poland', 'Romania', 'Slovakia', 'Slovenia']
gdp_per_capita = [9318, 17566, 24167, 23077, 24154, 19279, 18603, 19626, 28739, 28633, 23484, 2168, 1782]

# Колір прямокутників (стовпчиків)
colors = ['red', 'orange', 'yellow', 'green', 'lightblue', 'blue', 'purple', 'pink', 'brown', 'gray', 'black', 'cyan', 'magenta']

# Побудова горизонтальної стовпчикової діаграми
plt.figure(figsize=(10, 6))
plt.barh(countries, gdp_per_capita, color=colors)
plt.xlabel('ВВП на душу населення (в євро)')
plt.ylabel('Країни')
plt.title('ВВП на душу населення за 2020 рік для країн 3-ї групи')

# Додавання легенди
plt.legend(['ВВП на душу населення'])

# Встановлення підписів для вісей
plt.xticks(rotation=45)  # Поворот підписів на вісі x на 45 градусів

plt.grid(True)
plt.show()
