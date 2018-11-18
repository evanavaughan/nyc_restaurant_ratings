from dash_functions import rating_comparison, rating_price_inf, rating_price_ta, inf_price_rating_hist_1, inf_price_rating_hist_2, inf_price_rating_hist_3, inf_price_rating_hist_4, ta_price_rating_hist_1, ta_price_rating_hist_2, ta_price_rating_hist_4, inf_rating, ta_rating, map_data
import plotly.graph_objs as go

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

map_data = [ dict(
        type = 'scattergeo',
        locations = 'NY',
        locationmode = 'USA-states',
        lon = long_list,
        lat = lat_list,
        text = text_list,
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            cmin = 0,
        ))]

map_layout = dict(
        title = 'NYC Restaurants)',
        colorbar = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )

map_fig = dict( data=map_data, layout=map_layout )
