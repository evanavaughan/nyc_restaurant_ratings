from __init__ import db, app
from dash_functions import rating_comparison, rating_price_inf, rating_price_ta, inf_price_rating_hist_1, inf_price_rating_hist_2, inf_price_rating_hist_3, inf_price_rating_hist_4, ta_price_rating_hist_1, ta_price_rating_hist_2, ta_price_rating_hist_4
from dash_functions3 import ta_price_by_neighborhood, inf_price_by_neighborhood
import dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

app.title = 'NYC Eats'

app.layout = html.Div(
    children=[
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(id='other', label='Infatuation',
        children=[
            dcc.Graph(figure=
            {'data': [
        {
            'values': [i[1] for i in inf_price_by_neighborhood()[0]],
            'labels': [i[0] for i in inf_price_by_neighborhood()[0]],
            'name': 'Cheap Eats',
            'domain': {'x':[.05,.45]},
            'type': 'pie',
            },
        ],
            'layout': {
            'title':'Cheap Eats by Neighborhood - Infatuation',
            'legend': {'x':-.1},
            }}),
            ],
    ),
    dcc.Tab(id='something', label='Trip Advisor',
       children=[
        dcc.Graph(figure=
            {'data' : [
        {
            'values': [i[1] for i in ta_price_by_neighborhood()[0]],
            'labels': [i[0] for i in ta_price_by_neighborhood()[0]],
            'domain': {'x':[.55,.95]},
            'type': 'pie',
        },
    ],
        'layout': {
            'title':'Cheap Eats by Neighborhood - Trip Advisor'
        }})
        ]
    )

    ])
  ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
