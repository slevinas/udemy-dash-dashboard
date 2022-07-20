import re
from dash import Dash, html, Input, Output ,dcc
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('./world_happiness.csv')


app=Dash()


app.layout=html.Div(children=[
    html.H1(children='World Hapiness Dashboard '),

    html.P(children=['This dashboard shows the happiness score. ',

            html.Br(),

            html.A('World Happiness Report Data Source', href='https://worldhappiness.report', target='_blank')]
           ),

    dcc.Dropdown(id='country-dropdown',
                 options=happiness['country'].unique(),
                 value='United States'),

    dcc.Graph(id='happiness-graph')])

@app.callback(
    Output('happiness-graph','figure'),
    Input('country-dropdown','value')    
)

def update_graph(selected_country):
    filtered_happines = happiness[happiness['country']==selected_country]
    line_fig = px.line(filtered_happines,
                   x='year', y='happiness_score',
                   title=f'Happiness Score in the {selected_country}')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)