import matplotlib.pyplot as plt
import numpy as np

# Дані для структури ВВП (промисловість, сільське господарство, послуги) за 2010 та 2020 рр.
countries = ['USA', 'Germany', 'Turkey', 'Poland', 'Ukraine']
industrial_2010 = [20331, 926, 116, 356, 131]
agriculture_2010 = [1682, 68, 65, 62, 91]
services_2010 = [11703, 2762, 566, 627, 382]

industrial_2020 = [22429, 1225, 243, 521, 121]
agriculture_2020 = [1783, 58, 70, 70, 90]
services_2020 = [15684, 4005, 869, 1096, 476]

# Розміщення стовпців
bar_width = 0.3
index = np.arange(len(countries))

# Побудова групової стовпчикової діаграми з накопиченням
plt.figure(figsize=(10, 6))
plt.bar(index, industrial_2010, color='b', width=bar_width, label='Industrial 2010')
plt.bar(index, agriculture_2010, color='g', width=bar_width, bottom=industrial_2010, label='Agriculture 2010')
plt.bar(index, services_2010, color='r', width=bar_width, bottom=np.array(industrial_2010) + np.array(agriculture_2010), label='Services 2010')

plt.bar(index + bar_width, industrial_2020, color='c', width=bar_width, label='Industrial 2020')
plt.bar(index + bar_width, agriculture_2020, color='m', width=bar_width, bottom=industrial_2020, label='Agriculture 2020')
plt.bar(index + bar_width, services_2020, color='y', width=bar_width, bottom=np.array(industrial_2020) + np.array(agriculture_2020), label='Services 2020')

# Додавання легенди та підписів для вісей
plt.xlabel('Countries')
plt.ylabel('GDP')
plt.title('GDP Structure by Industry, Agriculture, and Services for 2010 and 2020')
plt.xticks(index + bar_width / 2, countries)
plt.legend()

plt.grid(True)
plt.show()
