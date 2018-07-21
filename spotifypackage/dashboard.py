import dash_core_components as dcc
import dash_html_components as html
from spotifypackage import app


app.layout = html.Div(children= html.H1('Check it out! This app has Flask AND Dash!'))

# html.P("Adding some cool graph here soon:"),dcc.Graph(
# id = "uber_pricing_graph",
# figure = {'data': [{'x' :data[0]['x'], 'y': data[0]['y'], 'type':data[0]['type'], 'name': data[0]['name']},
# {'x': data[1]['x'], 'y': data[1]['y'], 'type': data[1]['type'], 'name': data[1]['name']}],
# 'layout': {'title': "Uber Pricing in Brooklyn and Manhattan"}}
# )])
