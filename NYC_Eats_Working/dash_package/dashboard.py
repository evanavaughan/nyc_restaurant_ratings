from __init__ import db, app
from dash_functions import rating_comparison, rating_price_inf, rating_price_ta
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Price v Rating', children=[

dcc.Graph(
    id='price and rating',
    figure={
        'data': [
            {'x': ['$', '$$', '$$$', '$$$$'], 'y': [1, 4, 1],
                'type': 'bar', 'name': 'Infatuation'},
            # {'x': [1, 2, 3], 'y': [1, 2, 3],
            #  'type': 'bar', 'name': u'Montréal'},
        ]
    }
)
]),
    dcc.Tab(label='Tab three', children=[
dcc.Graph(
    id='example-graph-2',
    figure={
        'data': [
            {'x': [1, 2, 3], 'y': [2, 4, 3],
                'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [5, 4, 3],
             'type': 'bar', 'name': u'Montréal'},
        ]
    }
)
]),
    dcc.Tab(label='Tab four', children=[
dcc.Graph(
       id='example-graph',
       figure={
           'data': rating_comparison(),
           'layout': go.Layout(
               xaxis={'title': 'Feature'},
               yaxis={'title': 'Avg Feature Value'})}),
dcc.Markdown('*Note: data for tempo normalized to 0-1 range*')
            ])
        ]),
        dcc.Tab(label='Track Values by Feature', children=[
            html.Div([
# dcc.Dropdown(
#            id='select-artist',
#            options=rating_price_ta(),
#            placeholder="Select an artist", value ='Artist'
#        ),
html.Div(id= 'plot-container'),
dcc.Markdown('*Note: for all features, data for tempo normalized to 0-1 range*')
            ])
        ]),
])

if __name__ == '__main__':
    app.run_server(debug = True)
