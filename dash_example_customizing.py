import re
from dash import Dash, html, Input, Output ,dcc, State
import pandas as pd
import plotly.express as px
from pyrsistent import v

soccer = pd.read_csv('/Users/sagilevinas/Desktop/tutorials/dash-udemy-course/section8-customizing-dash-look/fifa_soccer_players.csv')

app=Dash()


app.layout=html.Div([
    html.H1('Soccer Players Dashboard', 
            style={
                'textAlign': 'center', 
                'fontFamily': 'fantacy',
                'fontSize': 50,
                'color': 'blue'}),

    html.P(['Source:',
            html.A('Sofifa', 
                    href='https://sofifa.com', 
                    target='_blank')],
            style={'border': 'solid'}),
    html.Label('Player name'),
    dcc.Dropdown(
                options=soccer['long_name'].unique(),
                value=soccer['long_name'].unique()[0],
                style={'background': 'lightblue'}
    ),
],
    style={'padding':100, 'border': 'solid'})
#     dcc.RadioItems( id='data-radio',
#                     options={
#                         'happiness_score': 'Happiness Score',
#                         'happiness_rank': 'Happiness Rank'
#                             },
#                     value='happiness_score'
#                     ),
#     html.Br(),
#     html.Button(id='submit-button',
#                 n_clicks=0 ,
#                 children='Update the output'),

#     dcc.Graph(id='happiness-graph'),
#     html.Div(id='avarage-div')
#                     ])

# @app.callback(
#     Output('country-dropdown','options'),
#     Output('country-dropdown','value'),
#     Input('region-radio','value'),    
# )
# def update_dropdown(selected_region):
#     filtered_happines = happiness[happiness['region']==selected_region]
#     country_options = filtered_happines['country'].unique()
#     return country_options, country_options[0]




# @app.callback(
#     Output('happiness-graph','figure'),
#     Output('avarage-div','children'),
#     Input('submit-button','n_clicks'),
#     State('country-dropdown','value'),    
#     State('data-radio','value'),
# )

# def update_graph(button_click, selected_country,selected_data_field):
#     filtered_happines = happiness[happiness['country']==selected_country]
#     line_fig = px.line(filtered_happines,
#                    x='year', y=selected_data_field,
#                    title=f'{selected_data_field} in the {selected_country}')
#     selected_avg = filtered_happines[selected_data_field].mean()
#     return line_fig, f'The average {selected_data_field} for {selected_country} ' \
#                      f'is {selected_avg}'


if __name__ == '__main__':
    app.run_server(debug=True)