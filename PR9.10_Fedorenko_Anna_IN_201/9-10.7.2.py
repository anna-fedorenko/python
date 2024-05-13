import plotly.graph_objs as go

# Завантаження даних
countries = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 
             'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 
             'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 
             'Spain', 'Sweden']
gdp = [45000, 40000, 20000, 18000, 33000, 30000, 55000, 32000, 46000, 43000, 48000, 28000, 25000, 72000, 
       42000, 28000, 27000, 90000, 36000, 52000, 32000, 30000, 25000, 20000, 28000, 34000, 42000]
population = [9000000, 11500000, 7000000, 4100000, 1200000, 10700000, 5800000, 1300000, 5500000, 67000000, 
              83000000, 11000000, 9900000, 4900000, 60000000, 1900000, 2800000, 600000, 400000, 17500000, 
              38000000, 10000000, 19000000, 5500000, 4500000, 47000000, 10000000]
gdp_per_capita = [50000, 35000, 15000, 20000, 38000, 32000, 45000, 28000, 42000, 40000, 46000, 24000, 26000, 
                  62000, 36000, 22000, 24000, 100000, 40000, 48000, 28000, 29000, 13000, 18000, 32000, 34000, 
                  35000]
life_expectancy = [81, 82, 75, 78, 83, 79, 81, 77, 81, 82, 81, 82, 76, 83, 83, 74, 75, 83, 83, 82, 77, 81, 
                   75, 75, 79, 83, 82]
category = [3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

# Побудова діаграми розсіювання між ВВП та кількістю населення
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=gdp, y=population, mode='markers', text=countries, 
                          marker=dict(color='blue', size=10),
                          name='ВВП vs Кількість населення'))

# Задання параметрів діаграми
fig1.update_layout(title='Залежність між ВВП та кількістю населення для країн ЄС у 2020 році',
                   xaxis_title='ВВП (USD)',
                   yaxis_title='Кількість населення',
                   showlegend=True)

# Побудова діаграми розсіювання між ВВП на душу населення та середньою тривалістю життя
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=gdp_per_capita, y=life_expectancy, mode='markers', text=countries, 
                          marker=dict(color='green', size=10),
                          name='ВВП на душу населення vs Середня тривалість життя'))

# Задання параметрів діаграми
fig2.update_layout(title='Залежність між ВВП на душу населення та середньою тривалістю життя для країн ЄС у 2020 році',
                   xaxis_title='ВВП на душу населення (USD)',
                   yaxis_title='Середня тривалість життя',
                   showlegend=True)

# Побудова діаграми розсіювання для ВВП на душу населення та середньою тривалістю життя, розфарбованої за категоріями країн
# та з розміром точок, що відповідає витратам на охорону здоров’я на душу населення
fig3 = go.Figure()
for cat in range(1, 4):
    filtered_countries = [countries[i] for i in range(len(countries)) if category[i] == cat]
    filtered_gdp_per_capita = [gdp_per_capita[i] for i in range(len(gdp_per_capita)) if category[i] == cat]
    filtered_life_expectancy = [life_expectancy[i] for i in range(len(life_expectancy)) if category[i] == cat]
    fig3.add_trace(go.Scatter(x=filtered_gdp_per_capita, y=filtered_life_expectancy, mode='markers', 
                              text=filtered_countries, 
                              marker=dict(size=gdp_per_capita, color=cat, opacity=0.7),
                              name=f'Category {cat}'))

# Задання параметрів діаграми
fig3.update_layout(title='Залежність між ВВП на душу населення та середньою тривалістю життя для країн ЄС у 2020 році',
                   xaxis_title='ВВП на душу населення (USD)',
                   yaxis_title='Середня тривалість життя',
                   showlegend=True)

# Показати діаграми
fig1.show()
fig2.show()
fig3.show()
