import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

trace_dance_top = go.Scatter(
    x = [.5, .6, .7,.8],
    y = [90, 100, 82, 77],
    name = 'Top Tracks',
    mode = 'markers',
    marker = dict(
        size = 20,
        color = 'green',

    ),
    text = ['Narcos', 'Motorsport', 'Stir Fry']
)

trace_dance = go.Scatter(
    x = [.3, .98, .7,.10],
    y = [65, 77, 60, 70],
    name = 'Other Tracks',
    mode = 'markers',
    marker = dict(
        size = 20,
        color = 'blue',
        line = dict(
            width = 2,
        )
    ),
    text = ['Other', 'Other2', 'Other3']
)
trace_pitch_top = go.Scatter(
    x = [.55, .20, .1,.8],
    y = [90, 100, 82, 77],
    name = 'Top Tracks',
    mode = 'markers',
    marker = dict(
        size = 20,
        color = 'green',

    ),
    text = ['Narcos', 'Motorsport', 'Stir Fry']
)

trace_pitch = go.Scatter(
    x = [.8, .5, .03,.60],
    y = [65, 77, 60, 70],
    name = 'Other Tracks',
    mode = 'markers',
    marker = dict(
        size = 20,
        color = 'blue',
        line = dict(
            width = 2,
        )
    ),
    text = ['Other', 'Other2', 'Other3']
)

data = [trace_dance, trace_dance_top, trace_pitch, trace_pitch_top]

# high_annotations=[dict(x='2016-03-01',
#                        y=df.High.mean(),
#                        xref='x', yref='y',
#                        text='High Average:<br>'+str(df.High.mean()),
#                        ax=0, ay=-40),
#                   dict(x=df.High.idxmax(),
#                        y=df.High.max(),
#                        xref='x', yref='y',
#                        text='High Max:<br>'+str(df.High.max()),
#                        ax=0, ay=-40)]
# low_annotations=[dict(x='2015-05-01',
#                       y=df.Low.mean(),
#                       xref='x', yref='y',
#                       text='Low Average:<br>'+str(df.Low.mean()),
#                       ax=0, ay=40),
#                  dict(x=df.High.idxmin(),
#                       y=df.Low.min(),
#                       xref='x', yref='y',
#                       text='Low Min:<br>'+str(df.Low.min()),
#                       ax=0, ay=40)]

updatemenus = list([
    dict(type="buttons",
         active=-1,
         buttons=list([
            dict(label = 'Dance',
                 method = 'update',
                 args = [{'visible': [True, True, False, False]},
                         {'title': 'Tracks by Dance Measure'}]),
            dict(label = 'Pitch',
                 method = 'update',
                 args = [{'visible': [False, False, True, True]},
                         {'title': 'Tracks by Pitch Measure'}]),
            dict(label = 'All',
                 method = 'update',
                 args = [{'visible': [True, True, True, True]},
                         {'title': 'All Measures'}])]),
            #     # direction = 'down',
            # x = 0,
            # xanchor = 'left',
            # y = 0,
            # yanchor = 'top',
            # bgcolor = 'white',
            # bordercolor = 'white',
            # fontcolor = 'black',
             font = dict(size=20),
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
