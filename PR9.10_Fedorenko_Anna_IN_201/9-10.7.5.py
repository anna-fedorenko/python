import plotly.graph_objs as go

# Дані за структурою ВВП за регіонами світу у 2020 році
regions = ['World', 'Europe', 'Ukraine']
gdp_share = [100, 22, 0.5]  # У відсотках

# Підписи для секторів
labels = ['World', 'Europe', 'Ukraine']

# Створення першої кругової діаграми з відображенням значення частки на секторах
fig1 = go.Figure(data=[go.Pie(labels=labels, values=gdp_share, textinfo='label+percent', hole=0.3)])
fig1.update_layout(title='Структура ВВП за регіонами світу у 2020 році')

# Показати діаграму
fig1.show()

# Створення другої кругової діаграми з тінню
fig2 = go.Figure(data=[go.Pie(labels=labels, values=gdp_share, hole=0.3)])
fig2.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20,
                  marker=dict(line=dict(color='#000000', width=2)))

fig2.update_layout(title='Структура ВВП за регіонами світу у 2020 році з тінню')

# Показати діаграму
fig2.show()

# Створення третьої кругової діаграми з розрізанням
fig3 = go.Figure(data=[go.Pie(labels=labels, values=gdp_share, hole=0.3)])
fig3.update_traces(textinfo='label+percent', pull=[0.1, 0.1, 0.3], marker=dict(line=dict(color='#000000', width=2)))

fig3.update_layout(title='Структура ВВП за регіонами світу у 2020 році з розрізанням')

# Показати діаграму
fig3.show()

