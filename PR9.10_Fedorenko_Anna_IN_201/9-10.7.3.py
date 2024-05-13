import plotly.graph_objs as go

# Дані для країн 3-ї групи (роки вступу 2004 року та пізніше)
countries = ['Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Estonia', 'Hungary', 'Latvia', 'Lithuania', 'Malta', 'Poland', 'Romania', 'Slovakia', 'Slovenia']
gdp_per_capita = [9318, 17566, 24167, 23077, 24154, 19279, 18603, 19626, 28739, 28633, 23484, 2168, 1782]

# Колір прямокутників (стовпчиків)
colors = ['red', 'orange', 'yellow', 'green', 'lightblue', 'blue', 'purple', 'pink', 'brown', 'gray', 'black', 'cyan', 'magenta']

# Побудова горизонтальної стовпчикової діаграми
fig = go.Figure(go.Bar(
    y=countries,
    x=gdp_per_capita,
    orientation='h',
    marker=dict(color=colors),
))

# Задамо параметри діаграми
fig.update_layout(
    title='ВВП на душу населення за 2020 рік для країн 3-ї групи',
    xaxis_title='ВВП на душу населення (в євро)',
    yaxis_title='Країни',
    legend_title='Показники',
    legend=dict(x=1.1, y=0.5),
)

# Показати діаграму
fig.show()
