import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('/Users/ankushv/PycharmProjects/Heart-Attack-Prediction/Data/heart-attack.csv')

pd.options.plotting.backend='plotly'

fig = None

ChestPainType = ['Asymptomatic','Nonanginal','Nontypical','Typical']
Percentage = [47.52,28.38,16.50,7.6]

fig = go.Figure(data=[go.Pie(labels=ChestPainType, values=Percentage, textinfo='label+percent', hole=.3)])

def gender(Sex):
    if Sex == 0:
        return "Female"
    else:
        return "Male"

df['Gender'] = df['Sex'].apply(gender)

def sl(Slope):
    if Slope == 1:
        return "Up-Sloping"
    elif Slope == 2:
        return "Flat"
    else:
        return "Down-Sloping"

df['New_Slope'] = df['Slope'].apply(sl)

avg_age = df[["Age","Target","Gender"]].groupby(["Age","Gender"], as_index=False).mean()

avg_bp = df[["Age","RestBP","Gender"]].groupby(["Age","Gender"], as_index=False).mean()

avg = df[["Age", "MaxHR", "Sex"]].groupby(['Age','Sex'], as_index=False).mean()

cards = [
    dbc.Card(
        [
            html.H2(f"{df['MaxHR'].mean()}", className="card-title"),
            html.P("Max HR", className="card-text"),
        ],
        body=True,
        color="dark",
        inverse=True
    ),
    dbc.Card(
        [
            html.H2(f"{df['Chol'].mean()}", className="card-title"),
            html.P("Chol",className="card-text"),
        ],
        body=True,
        color="dark",
        inverse=True
    ),
]

app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Heart Disease Analysis', style={'text-align': 'center'}),
        html.Div(children='''
        The path to lead a longer life''',
                 style={'text-align': 'center'}),
        dbc.Row([dbc.Col(card) for card in cards]),

        dcc.Graph(id='graph-with-slider',
                  figure=fig),
]),
        html.Div(children=[
            html.Div(
                dcc.Graph(
                    figure= px.scatter(data_frame=df, x="Age", y="Oldpeak", color="New_Slope")

                )
            )
        ])

])


if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')