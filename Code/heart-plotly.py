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

app.layout = html.Div(children=[
    html.H1(children='Heart Attack Prediction'),

    html.Div(children='''
        The path to lead a longer life
    '''),
    dcc.Graph(id='graph-with-slider',
              figure=fig),
    dcc.Slider(
        id='Age-slider',
        min=df['Age'].min(),
        max=df['Age'].max(),
        value=df['Age'].min(),
        marks={str(int): str(int) for age in df['Age'].unique()},
        step=None
    )

])

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('Age-slider', 'value')])

def update_figure(selected_age):
    df = df[df.Age == selected_age]

    fig = px.bar(df, x="ChestPain", y="Age",
                     color="Thal")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')