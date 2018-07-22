import dash_core_components as dcc
import dash_html_components as html
from spotifypackage import app
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from spotifypackage.charts import *
import json
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


app.layout = html.Div(children= [html.H1('Artist Features Plot'),dcc.Dropdown(
        id='select-artist',
        options=list_of_artists_for_dropdown(),
        value="Artist"
    ),
html.Div(id= 'scatter-container')

])

def generate_scatter(scatter_data):
    return dcc.Graph(id = 'artist_features',
    figure = {
    'data': scatter_data,
    'layout': {'title' :  'Artist Features', 'updatemenus': updatemenus}})

@app.callback(Output(component_id = 'scatter-container', component_property ='children'), #sorting the values of children within food_table
[Input(component_id = 'select-artist',component_property = 'value' )]
)

def filter_plot(input_value):
    # pdb.set_trace()
    # using global to make sure we are accessing the imported data object
    global data
    trace_list = list_of_traces(input_value)
    top_tracks = trace_list[0]
    oth_tracks = trace_list[1]
    data = top_tracks + oth_tracks
    return generate_scatter(data)
