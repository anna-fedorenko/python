import plotly.graph_objs as go

# Дані за ВВП на душу населення для вказаних країн у роках 2010, 2015 і 2020 рр.
countries = ['Germany', 'France', 'Czech Republic', 'Poland', 'Romania']
gdp_per_capita_2010 = [40499, 39680, 20699, 13868, 11921]
gdp_per_capita_2015 = [47662, 43722, 25018, 25512, 19994]
gdp_per_capita_2020 = [52603, 51943, 23077, 28633, 23484]

# Створення графіків для кожного року
fig = go.Figure()

fig.add_trace(go.Bar(
    x=countries,
    y=gdp_per_capita_2010,
    name='2010',
    marker_color='rgb(55, 83, 109)'
))

fig.add_trace(go.Bar(
    x=countries,
    y=gdp_per_capita_2015,
    name='2015',
    marker_color='rgb(26, 118, 255)'
))

fig.add_trace(go.Bar(
    x=countries,
    y=gdp_per_capita_2020,
    name='2020',
    marker_color='rgb(255, 153, 51)'
))

# Налаштування параметрів діаграми
fig.update_layout(
    title='ВВП на душу населення за 2010, 2015 та 2020 рр. для обраних країн',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='ВВП на душу населення (в євро)',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,  # Проміжок між стовпцями в одній групі
    bargroupgap=0.1  # Проміжок між групами стовпців
)

# Показати діаграму
fig.show()
