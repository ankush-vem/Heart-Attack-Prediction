import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('/Users/ankushv/PycharmProjects/Heart-Attack-Prediction/Data/heart-attack.csv')

pd.options.plotting.backend='plotly'

fig = None

avg = df[["Age", "Target"]].groupby(['Age'], as_index=False).mean()
fig = px.bar(x='Age', y='Target', data_frame=avg)


app.layout = html.Div(children=[
    html.H1(children='Heart Attack Prediction', style={'text-align': 'center'}),

    html.Div(children='''
        The path to lead a longer life
    ''', style={'text-align': 'center'}),

    html.Label('Age'),
    dcc.RangeSlider(
        min=df['Age'].min(),
        max=df['Age'].max(),
        step=1,
        value=[df['Age'].min()+5, df['Age'].max()-5]
    ),

    html.Label('Type of Chest Pain'),
    dcc.Dropdown(
        options=[
            {'label': 'Asymptomatic', 'value': 'Asymptomatic'},
            {'label': 'Non-Anginal', 'value': 'Nonanginal'},
            {'label': 'Non-Typical', 'value': 'Nontypical'},
            {'label': 'Typical', 'value': 'Typical'}
        ],
        value=['Asymptomatic','Typical'],
        multi=True
    ),

    html.Label('Fasting Blood Sugar (Fbs)'),
    dcc.Checklist(
        id='select-all',
        options=[
            {'label': 'Fbs < 120 mg/dl', 'value': 0},
            {'label': 'Fbs > 120 mg/dl', 'value': 1}
        ],
        value= [0]
    ),

    html.Label('Resting Electro Cardio Graphic'),
    dcc.Dropdown(
        options=[
            {'label': 'Normal', 'value': 0},
            {'label': 'Having ST-T Wave Abnormality', 'value': 1},
            {'label': 'Showing probable or definite left ventricular hypertrophy by Estes criteria', 'value': 2}
        ],
        value=[0,1],
        multi=True
    ),

    html.Label('Gender'),
    dcc.Checklist(id='select-all',
                  options=[
                      {'label': 'Male', 'value': 1},
                      {'label': 'Female', 'value': 0}
                  ],
                  value=[0,1]),

    html.Label('Diagnosis of Heart Disease'),
    dcc.Checklist(id='select-all',
                  options=[
                      {'label': '< 50% diameter narrowing', 'value': 0},
                      {'label': '> 50% diameter narrowing', 'value': 1}
                  ],
                  value=[0]),

    html.Label('Thal'),
    dcc.Dropdown(
        options=[
            {'label': 'Normal', 'value': 3},
            {'label': 'Reversable Defect', 'value': 7},
            {'label': 'Fixed Defect', 'value': 6}
        ],
        value=[3,6],
        multi=True
    ),

    html.Label('Number of Blood Vessels'),
    dcc.RangeSlider(
        min=df['Ca'].min(),
        max=df['Ca'].max(),
        step=1,
        value=[df['Ca'].min(), df['Ca'].max()]
    ),

    html.Label('Slope of Peak Exercise'),
    dcc.Dropdown(
        options=[
            {'label': 'Flat', 'value': 2},
            {'label': 'Up Sloping', 'value': 1},
            {'label': 'Down Sloping', 'value': 3}
        ],
        value=[1,2,3],
        multi=True
    ),

    html.Label('Exercise Induced Angina'),
    dcc.Checklist(id='select-all',
                  options=[
                      {'label': 'Yes', 'value': 1},
                      {'label': 'No', 'value': 0}
                  ],
                  value=[1]
    ),

    dcc.Graph(figure=fig),

])

if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')