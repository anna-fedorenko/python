import matplotlib.pyplot as plt

# Дані для років 2010, 2015 та 2020 рр. для кожної країни
countries = ['Germany', 'France', 'Czech Republic', 'Poland', 'Romania']
gdp_2010 = [41787, 38476, 21247, 17913, 13733]  # ВВП на душу населення для 2010 р.
gdp_2015 = [47933, 44162, 26625, 25280, 19966]  # ВВП на душу населення для 2015 р.
gdp_2020 = [46413, 43678, 38425, 36170, 24521]  # ВВП на душу населення для 2020 р.

# Розміри діаграми
plt.figure(figsize=(10, 6))

# Ширина стовпців
bar_width = 0.2

# Побудова групової стовпчикової діаграми
plt.bar(countries, gdp_2010, width=bar_width, color='b', align='center', label='2010')
plt.bar([x + bar_width for x in range(len(countries))], gdp_2015, width=bar_width, color='g', align='center', label='2015')
plt.bar([x + 2*bar_width for x in range(len(countries))], gdp_2020, width=bar_width, color='r', align='center', label='2020')

# Додавання легенди
plt.legend()

# Підписи для вісей
plt.xlabel('Країни')
plt.ylabel('ВВП на душу населення')
plt.title('ВВП на душу населення за 2010, 2015 та 2020 рр. для країн Німеччина, Франція, Чехія, Польща та Румунія')

plt.grid(True)
plt.show()
