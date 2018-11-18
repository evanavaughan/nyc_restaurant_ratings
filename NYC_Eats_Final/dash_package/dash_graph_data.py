from dash_functions import inf_price_rating_hist_1, inf_price_rating_hist_2, inf_price_rating_hist_3, inf_price_rating_hist_4, ta_price_rating_hist_1, ta_price_rating_hist_2, ta_price_rating_hist_4, inf_rating, ta_rating, map_data
import plotly.graph_objs as go
import plotly.plotly as py
mapbox_access_token='pk.eyJ1Ijoia2FoYXJ0bWFuIiwiYSI6ImNqb214MWlwbjBxM28zcW85cmU2N3dkMnIifQ.VsLrl5DVttNGvSo266pf3A'

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

trace_list = [inf_rating('Upper East Side'), inf_rating('Upper West Side'), inf_rating('Greenwich Village and Soho'), inf_rating('Hells Kitchen'), inf_rating('Chelsea')]

trace0 = go.Box(
    y = trace_list[0],
    name = 'Upper East Side',
    boxpoints = False,
)

trace1 = go.Box(
    y = trace_list[1],
    name = 'Upper West Side',
    boxpoints = False,
)

trace2 = go.Box(
    y = trace_list[2],
    name = 'West Village & Soho',
    boxpoints = False,
)

trace3 = go.Box(
    y = trace_list[3],
    name = 'Chelsea',
    boxpoints = False,
)

trace4 = go.Box(
    y = trace_list[4],
    name = 'Hell\'s Kitchen',
    boxpoints = False,
)

box_data = [trace0, trace1, trace2, trace3, trace4]
box_layout = go.Layout(title='Infatuation Neighborhood Ratings')
fig = go.Figure(data=box_data,layout=box_layout)

name_list = [i[0] for i in map_data()]
rating_list = [str(i[3]) for i in map_data()]
price_list = [str(i[4]) for i in map_data()]
text_list = []
for i in range(len(map_data())):
    text_list.append(name_list[i]+' , '+rating_list[i]+' , '+price_list[i])
lat_list = [i[1] for i in map_data()]
long_list = [i[2] for i in map_data()]

map_data = [
    go.Scattermapbox(
        lat=lat_list,
        lon=long_list,
        mode='markers',
        marker=dict(
            size=9
        ),
        text=text_list,
    )
]

map_layout = go.Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=40.730610,
            lon=-73.935242
        ),
        pitch=0,
        zoom=5
    ),
)

map_fig = dict( data=map_data, layout=map_layout )
