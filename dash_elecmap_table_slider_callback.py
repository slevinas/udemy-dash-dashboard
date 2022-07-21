import re
from dash import Dash, html, dcc ,dash_table, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


logfil_cloudwatch_lgsinsigh_results= '/Users/sagilevinas/Downloads/cloudwatchlogs-fri-july8-agg-3col.csv'
#df23 = pd.read_csv(logfile23, header=None)
df_fri = pd.read_csv(logfil_cloudwatch_lgsinsigh_results)
top10queries = df_fri.loc[:,['Tag','g_size']].nlargest(n=10,columns=['g_size'])

electricity = pd.read_csv('~/Downloads/electricity.csv')

min_year = electricity['Year'].min()
max_year = electricity['Year'].max()


app = Dash(external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div([
    html.H1('Electricity Prices by Us State'),

    dcc.RangeSlider(id='year-slider',
                    min=min_year,
                    max=max_year,
                    value=[min_year, max_year],
                    marks={i:str(i) for i in range(min_year, max_year + 1)} ),

    dcc.Graph(id='map-graph'),
    html.Div(id='click-children'),
    dash_table.DataTable(id='price-info', data=electricity.to_dict('records'))
    #dash_table.DataTable(id='price-info',data=top10queries.to_dict('records'))
    
                      ])
            
  
@app.callback(
    Output('map-graph','figure'),
    Input('year-slider','value'))
def update_map(selected_years):
    filtered_electricity = electricity[(
        electricity['Year'] >= selected_years[0]) & (electricity['Year'] <= selected_years[1])]

    avg_price_electricity = filtered_electricity.groupby('US_State')['Residential Price'].mean().reset_index()

    map_fig = px.choropleth(avg_price_electricity,
                            locations='US_State', locationmode='USA-states',
                            color='Residential Price', scope='usa',
                            color_continuous_scale='reds')
    return map_fig

@app.callback(
    Output('click-children','children'),
    Input('map-graph','clickData')
)
def print_click_data(clicked_data):
    return str(clicked_data)





if __name__ == '__main__':
    app.run_server(debug=True)