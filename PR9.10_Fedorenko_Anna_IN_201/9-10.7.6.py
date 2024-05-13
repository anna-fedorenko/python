import plotly.graph_objs as go

# Дані для структури ВВП (промисловість, сільське господарство, послуги) за 2010 та 2020 рр.
countries = ['USA', 'Germany', 'Turkey', 'Poland', 'Ukraine']
industrial_2010 = [20331, 926, 116, 356, 131]
agriculture_2010 = [1682, 68, 65, 62, 91]
services_2010 = [11703, 2762, 566, 627, 382]

industrial_2020 = [22429, 1225, 243, 521, 121]
agriculture_2020 = [1783, 58, 70, 70, 90]
services_2020 = [15684, 4005, 869, 1096, 476]

# Створення діаграм
fig = go.Figure()

# Додавання стовпчиків для 2010 року
fig.add_trace(go.Bar(x=countries, y=industrial_2010, name='Industrial 2010', marker_color='blue'))
fig.add_trace(go.Bar(x=countries, y=agriculture_2010, name='Agriculture 2010', marker_color='green', 
                     opacity=0.7, base=industrial_2010))
fig.add_trace(go.Bar(x=countries, y=services_2010, name='Services 2010', marker_color='red', 
                     opacity=0.7, base=[industrial_2010[j] + agriculture_2010[j] for j in range(len(countries))]))

# Додавання стовпчиків для 2020 року
fig.add_trace(go.Bar(x=countries, y=industrial_2020, name='Industrial 2020', marker_color='cyan', 
                     width=0.3, offset=-0.15))
fig.add_trace(go.Bar(x=countries, y=agriculture_2020, name='Agriculture 2020', marker_color='magenta', 
                     width=0.3, offset=-0.15, opacity=0.7, base=industrial_2020))
fig.add_trace(go.Bar(x=countries, y=services_2020, name='Services 2020', marker_color='yellow', 
                     width=0.3, offset=0.15, opacity=0.7, base=[industrial_2020[j] + agriculture_2020[j] for j in range(len(countries))]))

# Задамо параметри діаграми
fig.update_layout(barmode='relative', title='GDP Structure by Industry, Agriculture, and Services for 2010 and 2020',
                  xaxis_title='Countries', yaxis_title='GDP', legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99))

# Показати діаграму
fig.show()
