# from __init__ import db, app
# from dash_functions import rating_comparison, rating_price_inf, rating_price_ta
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd
# import plotly.graph_objs as go
# from dash.dependencies import Input, Output, State
#
# def movie_count_by_month_graph():
#     return dcc.Graph(
#         id='bar-graph-movies-in-month',
#         figure ={'data': [
#                 {'x': ['$', '$$'], 'y': [4, 6], 'type': 'bar'}],
#             'layout': {
#                 'title': 'Movies Released by Month'
#         }})
#
#
# app.layout = html.Div(children=[
#     html.H1('Welcome to our Movie Database.'),
#     html.H3('To fully enjoy your experience, play around with different routes to learn more about movie performance.'),
#
#     # dcc.Tabs(
#     #     tabs=[
#     #         {'label': 'Rating', 'value': 'M'},
#     #         {'label': 'Genres', 'value': 'G'},
#     #         {'label': 'Directors', 'value': 'D'},
#     #     ],
#     #     value='M',
#     #     id='children'
#     # ),
#     article_div], style={'width': '90%','fontFamily': 'Sans-Serif', 'margin-left': 'auto', 'margin-right': 'auto'})
#
# @app.callback(Output('tab-output1', 'children'), [Input('tabs', 'value')])
# def display_content(value):
#     data1 = [
#         {'x': ['$','$$','$$$'], 'y': [1,4,5], 'name': 'President Obama 2007-2009', 'marker': {'color': democrat_blue}, 'type': ['bar']},
#         {'x': ['$','$$','$$$'], 'y': [3,5,2], 'name': 'President Trump 2016-2018', 'marker': {'color': republican_red}, 'type': ['bar']}]
#     data2 = [
#         {'values': [obama_total_article_count, trump_total_article_count], 'name':'Article Chart by President', 'marker': {'colors': [democrat_blue, republican_red]}, 'type': 'pie', 'labels': ['President Obama', 'President Trump'],  'textfont': {'size': 20}}]
#
#     if value == 1:
#         return html.Div([
#             dcc.Graph(id='graph', figure={'data': data1, 'layout': {'title': 'Number of Articles Written by Month','margin-left': 'auto', 'margin-right': 'auto', 'legend': {'x': 0, 'y': 1}}}), html.Div(' '.join('created: by: Catherine Huang, Christopher Pease'))
#             ])
#     elif value == 2:
#         return html.Div([
#             dcc.Graph(id='graph', figure={'data': data2, 'layout': {'title': 'Article Breakdown by President'}}), html.Div(' '.join('created by: Catherine Huang, Christopher Pease'))
#             ])
# #     dcc.Dropdown(
# #             id='class-dropdown',
# #             options=[],
# #             value='M-CT'
# #     ),
# #     html.Div(id='class-graphs'),
# # ])
#
# # @app.callback(
# #     Output(component_id = 'class-dropdown', component_property='options'),
# #     [Input(component_id= 'children', component_property='value')]
# #     )
# # def update_dropdown(value):
# #     if value=='M':
# #         return [{'label': 'Count', 'value': 'M-CT'},
# #         {'label': 'Average Revenue per Month', 'value': 'AVG-Month'},
# #         {'label': 'Average Revenue per Season', 'value': 'AVG-Season'},
# #         ]
# #     elif value=='G':
# #         return [{'label': 'Count', 'value': 'G-CT'},
# #         {'label': 'Total', 'value': 'TOT'},
# #         {'label': 'Average', 'value': 'AVG'}
# #         ]
# #     elif value=='D':
# #         return [{'label': 'Count', 'value': 'D-CT'},
# #         {'label': 'Revenue', 'value': 'D-Rev'}
# #         ]
# #
# # @app.callback(
# #     Output(component_id = 'class-graphs', component_property='children'),
# #     [Input(component_id= 'class-dropdown', component_property='value')]
# #     )
# # def update_output(value):
# #     if value=='M-CT':
# #         return movie_count_by_month_graph()
# #     elif value=='AVG-Month':
# #         return movie_count_by_month_graph()
# #     elif value=='AVG-Season':
# #         return movie_count_by_month_graph()
# #
# # app.callback(
# #     Output(component_id = 'genre-specific', component_property='options'),
# #     [Input(component_id= 'children', component_property='value')
# #     ])
# # def update_checklists(value):
# #     if value=='G':
# #         return genre_setup()
# #     else:
# #         return []
#
# if __name__ == '__main__':
#     app.run_server(debug = True)
