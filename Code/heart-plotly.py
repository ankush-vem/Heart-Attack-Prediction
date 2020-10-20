import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('/Users/ankushv/PycharmProjects/Heart-Attack-Prediction/Data/heart-attack.csv')

pd.options.plotting.backend='plotly'

fig = None

avg = df[["Age", "Target"]].groupby(['Age'], as_index=False).mean()
fig = px.bar(x='Age', y='Target', data_frame=avg)


app.layout = html.Div(children=[
    html.H1(children='Heart Attack Prediction'),

    html.Div(children='''
        The path to lead a longer life
    '''),
    dcc.Graph(id='graph-with-slider',
              figure=fig),

])


if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')