from dash import Dash, html, Input, Output ,dcc
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('./world_happiness.csv')

line_fig = px.line(happiness[happiness['country'] == 'United States'],
                   x='year', y='happiness_score',
                   title='Happiness Score in the USA')
app=Dash()


app.layout=html.Div(children=[
    html.H1(children='World Hapiness Dashboard '),
    html.P(children=['This dashboard shows the happiness score. ',
            html.Br(),
            html.A('World Happiness Report Data Source',
                    href='https://worldhappiness.report',
                    target='_blank')]),
    dcc.Dropdown(id='country-dropdown',
                 options=happiness['country'].unique(),
                 value='United States'),
    dcc.Graph(id='happiness-graph')
])

if __name__ == '__main__':
    app.run_server(debug=True)