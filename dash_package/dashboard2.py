from __init__ import db, app
from dash_graph_data import *
from dash_functions import *
import dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

app.title = 'NYC Eats'

app.layout = html.Div(
    html.Div([
        html.Div([
            html.H1(children='NYC Eats',
                    className = 'nine columns'),
        ], className = 'row'),
        dcc.Tabs(id='tabs', children=[
            dcc.Tab(label='Rating & Price', children=[
                html.Div(
                    [
                        html.Div(
                            [
                                html.P('Choose Infatuation Rating Category:'),
                                dcc.Checklist(
                                        id = 'Inf-Rating',
                                        options = [{'label': k, 'value': k} for k in inf_rating_data.keys()],
                                        values=['Rating <2'],
                                        labelStyle={'display': 'inline-block'}
                                ),
                            ],
                            className='six columns',
                            style={'margin-top': '10'}
                        ),
                        html.Div(
                        [
                            html.P('Choose Trip Advisor Rating Category:'),
                            dcc.Checklist(
                                    id = 'Ta-Rating',
                                    options=[{'label': k, 'value': k} for k in ta_rating_data.keys()],
                                    values=['Rating 4-4.25'],
                                    labelStyle={'display': 'inline-block'}
                            ),
                        ],
                        className='six columns',
                        style={'margin-top': '10'}
                    )
                    ], className='row'
                ),
                html.Div([
                    html.Div([
                        dcc.Graph(
                            id='inf-rating-graph'
                        )
                    ], className = 'six columns'),
                html.Div([
                    dcc.Graph(
                        id='ta-rating-graph'
                    )
                ], className = 'six columns')
            ], className = 'row')
            ]),
        dcc.Tab(label='Rating Variation', children=[
            html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(
                                figure = fig, id='box-plot'
                        ),
                ],
                className='twelve columns',
            ),
        ])
        ]),
        dcc.Tab(label='Restaurant Map', children=[
            html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(
                                figure = map_fig, id='map'
                        ),
                ],
                className='twelve columns',
            ),
        ])
        ]),
        dcc.Tab(label='Cheap Eats by Neighborhood', children=[
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Cheap Eats by Neighborhood',
                    style={'width':'100%', 'margin':5, 'textAlign': 'center'}),
                    dcc.Graph(id='g1', figure=
                        {'data' : [
                    {
                        'values': [i[1] for i in inf_price_by_neighborhood()[0]],
                        'labels': [i[0] for i in inf_price_by_neighborhood()[0]],
                        'type': 'pie',
                    },
                ],
                    'layout': {
                        'title':'Infatuation',
                    }})
                ], className="six columns"),

                html.Div([
                    html.H3('Cheap Eats by Neighborhood',
                    style={'width':'100%', 'margin':5, 'textAlign': 'center'}),
                    dcc.Graph(id='g2', figure=
                    {'data': [
                {
                    'values': [i[1] for i in ta_price_by_neighborhood()[0]],
                    'labels': [i[0] for i in ta_price_by_neighborhood()[0]],
                    'name': 'Cheap Eats',
                    'type': 'pie',
                    },
                ],
                    'layout': {
                    'title':'Trip Advisor',
                    }})
                ], className="six columns"),
            ], className="row")
        ])
        ])
])
])
)
@app.callback(
    dash.dependencies.Output('inf-rating-graph', 'figure'),
    [dash.dependencies.Input('Inf-Rating', 'values')])
def update_graph_src(selector):
    data = []
    for city in selector:
        data.append({'x': inf_rating_data[city]['x'], 'y': inf_rating_data[city]['y'],
                    'type': 'bar', 'name': city})
    figure = {
        'data': data,
        'layout': {
            'title': 'Infatuation',
            'xaxis' : dict(
                title='Price',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='Count',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('ta-rating-graph', 'figure'),
    [dash.dependencies.Input('Ta-Rating', 'values')])
def update_graph_src(selector):
    data = []
    for city in selector:
        data.append({'x': ta_rating_data[city]['x'], 'y': ta_rating_data[city]['y'],
                    'type': 'bar', 'name': city})
    figure = {
        'data': data,
        'layout': {
            'title': 'Trip Advisor',
            'xaxis' : dict(
                title='Price',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='Count',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
