import plotly.plotly as py
import plotly.graph_objs as go
from spotifypackage.etl import *
import numpy as np

updatemenus = list([
    dict(type="buttons",
         active=-1,
         buttons=list([
            dict(label = 'Danceability',
                 method = 'update',
                 args = [{'visible': [True, False, False, False, False]},
                         {'title': 'Tracks by Danceability'}]),
            dict(label = 'Energy',
                 method = 'update',
                 args = [{'visible': [False, True, False, False, False]},
                         {'title': 'Tracks by Energy'}]),
            dict(label = 'Acousticness',
                 method = 'update',
                 args = [{'visible': [False, False, True, False, False]},
                         {'title': 'Tracks by Acousticness'}]),
            dict(label = 'Valence',
                 method = 'update',
                 args = [{'visible': [False, False, False, True, False]},
                         {'title': 'Tracks by Valence'}]),
            dict(label = 'Tempo',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, True]},
                         {'title': 'Tracks by Tempo'}]),
            dict(label = 'All',
                method = 'update',
                args = [{'visible': [True, True, True, True, True]},
                {'title': 'Tracks by All Measures'}])
            ]),

            #     # direction = 'down',
            # x = 0,
            # xanchor = 'left',
            # y = 0,
            # yanchor = 'top',
            # bgcolor = 'white',
            # bordercolor = 'white',
            # fontcolor = 'black',
             font = dict(size=16),
        #     buttons=list([
        #     dict(args=['type', 'surface'],
        #         label='Migos',
        #         method='restyle'
        #     ),
        #
        #     dict(
        #         args=['type', 'heatmap'],
        #         label='Charlie Puth',
        #         method='restyle'
        #     )]),
        #      direction = 'left',
        # pad = {'r': 10, 't': 10},
        # showactive = True,
        # type = 'buttons',
        # x = 0.1,
        # xanchor = 'left',
        # y = 1.1,
        # yanchor = 'top'
    ),
            ])
# dates = [album.release_date for album in Album.query.all() if album.artist_id == 7]
# steps = []
# for i in range(len(dates)):
#     step = dict(
#         method = 'restyle',
#         args = ['visible', [False] * len(dates)],
#     )
#     step['args'][1][i] = True # Toggle i'th trace to "visible"
#     steps.append(step)
#
# sliders = [dict(
#     active = 10,
#     currentvalue = {"prefix": "Frequency: "},
#     pad = {"t": 50},
#     steps = steps
# )]

# x = ['danceability', 'danceability', 'danceability', 'danceability', 'danceability','danceability','danceability', 'danceability', 'danceability', 'danceability', 'danceability','danceability'
# ,'danceability', 'danceability', 'danceability', 'danceability', 'danceability','danceability','danceability','danceability']
#
# trace0 = go.Box(
#     y=features_values('danceability','Migos'),
#     x=box_x_values(genre_input),
#     name='Migos',
#     marker=dict(
#         color='#3D9970'
#     )
# )
# trace1 = go.Box(
#     y=features_values('danceability','The Notorious B.I.G.'),
#     x=box_x_values(genre_input),
#     name='The Notorious B.I.G.',
#     marker=dict(
#         color='#FF4136'
#     )
# )
#
# data_box = [trace0, trace1]
# layout_box = go.Layout(
#     yaxis=dict(
#         title='normalized moisture',
#         zeroline=False
#     ),
#     boxmode='group'
# )

# html.Div([
# dcc.Graph(
# id='generation',
# figure={
# 'data': data_box,'layout': go.Layout(
#    xaxis={'title': 'feature'},
#    yaxis={'title': 'feature value'},
#    boxmode='group',
# )})
# ])
# ]),
