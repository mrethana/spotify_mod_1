import dash_core_components as dcc
import dash_html_components as html
from spotifypackage import app
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from spotifypackage.charts import *
import json

app.layout = html.Div(children= [html.H1('Artist Features Plot'),
dcc.Graph(id = 'artist_features',
figure = {
'data': data,
'layout': {'title' :  'Artist Features', 'updatemenus': updatemenus

             }}
)
])


# html.P("Adding some cool graph here soon:"),dcc.Graph(
# id = "uber_pricing_graph",
# figure = {'data': [{'x' :data[0]['x'], 'y': data[0]['y'], 'type':data[0]['type'], 'name': data[0]['name']},
# {'x': data[1]['x'], 'y': data[1]['y'], 'type': data[1]['type'], 'name': data[1]['name']}],
# 'layout': {'title': "Uber Pricing in Brooklyn and Manhattan"}}
# )])
