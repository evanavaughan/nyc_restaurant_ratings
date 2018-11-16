from __init__ import db, app
from dash_functions import rating_comparison, rating_price_inf, rating_price_ta, inf_price_rating_hist_1, inf_price_rating_hist_2, inf_price_rating_hist_3, inf_price_rating_hist_4, ta_price_rating_hist_1, ta_price_rating_hist_2, ta_price_rating_hist_4
import dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

inf_rating_data = {
    'Rating <2': {'x': ['$', '$$', '$$$','$$$$'], 'y': [inf_price_rating_hist_1()[0], inf_price_rating_hist_2()[0], inf_price_rating_hist_3()[0], inf_price_rating_hist_4()[0]]},
    'Rating 2-3': {'x': ['$', '$$', '$$$','$$$$'], 'y': [inf_price_rating_hist_1()[1], inf_price_rating_hist_2()[1], inf_price_rating_hist_3()[1], inf_price_rating_hist_4()[1]]},
    'Rating >=4': {'x': ['$', '$$', '$$$','$$$$'], 'y': [inf_price_rating_hist_1()[2], inf_price_rating_hist_2()[2], inf_price_rating_hist_3()[2], inf_price_rating_hist_4()[2]]}
}

ta_rating_data = {
    'Rating 4-4.25': {'x': ['$', '$$ - $$$','$$$$'], 'y': [ta_price_rating_hist_1()[0], ta_price_rating_hist_2()[0], ta_price_rating_hist_4()[0]]},
    'Rating 4.25-4.75': {'x': ['$', '$$ - $$$','$$$$'], 'y': [ta_price_rating_hist_1()[1], ta_price_rating_hist_2()[1], ta_price_rating_hist_4()[1]]},
    'Rating 4.75-5': {'x': ['$', '$$ - $$$','$$$$'], 'y': [ta_price_rating_hist_1()[2], ta_price_rating_hist_2()[2], ta_price_rating_hist_4()[2]]}
}
app.title = 'NYC Eats'

app.layout = html.Div(
    html.Div([
        html.Div([
            html.H1(children='NYC Eats',
                    className = "nine columns"),
            # html.Img(
            #     src="http://test.fulcrumanalytics.com/wp-content/uploads/2015/10/Fulcrum-logo_840X144.png",
            #     className='three columns',
            #     style={
            #         'height': '14%',
            #         'width': '14%',
            #         'float': 'right',
            #         'position': 'relative',
            #         'margin-top': 20,
            #         'margin-right': 20
            #     },
            # ),
            html.Div(children='''
                        A guide to NYC restaurants.
                        ''',
                    className = 'nine columns')
        ], className = "row"),

        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose Infatuation Rating Category:'),
                        dcc.Checklist(
                                id = 'Cities',
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
                            id = 'Cities2',
                            options=[{'label': k, 'value': k} for k in ta_rating_data.keys()],
                            values=['Rating 4-4.25'],
                            labelStyle={'display': 'inline-block'}
                    ),
                ],
                className='six columns',
                style={'margin-top': '10'}
            )
            ], className="row"
        ),
        html.Div([
            html.Div([
                dcc.Graph(
                    id='example-graph'
                )
            ], className = 'six columns'),
        html.Div([
            dcc.Graph(
                id='example-graph-2'
            )
        ], className = "six columns")
    ], className = "row")
    ], className='ten columns offset-by-one')
)

@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('Cities', 'values')])
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
                title='x Axis',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='y Axis',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('example-graph-2', 'figure'),
    [dash.dependencies.Input('Cities2', 'values')])
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
                title='x Axis',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='y Axis',
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
