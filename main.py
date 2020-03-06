import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

from style import Style

styles = Style.styles

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=external_stylesheets)
server = app.server

df = pd.read_csv("data/titanic.csv")

age_sur = []
ages = [[0, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90]]
for age in ages:
    df_age = df[(df['Age'] >= age[0]) & (df['Age'] < age[1])]
    survived = df_age['Survived'].value_counts()
    survived = [survived[0] if 0 in survived else 0, survived[1] if 1 in survived else 0]
    age_sur.append(survived)

#print(survived[0] if 0 in survived else 0)
#print([survived[1] for survived in age_sur])

app.layout = html.Div([
    html.H1("Titanic Data Analysis", style=styles['H1']),
    #dcc.Input(id='my-id', value='initial value', type='text'),
    #html.H2(id='my-div'),
    dcc.Graph(
        id='titanic-graph',
        figure={
            'data': [
                {
                'x': [f'{i[0]} - {i[1]}' for i in ages],
                'y': [survived[1] for survived in age_sur],
                'name': 'Survived', 
                'type': 'bar',
                'marker': {
                    'color':'rgb(55, 83, 109)'
                    }
                },
                {
                'x': [f'{i[0]} - {i[1]}' for i in ages],
                'y': [survived[0] for survived in age_sur],
                'name': 'Not survived', 
                'type': 'bar',
                'marker': {
                    'color':'rgb(202, 14, 35)'
                    }
                }
            ],
            'layout': {
                'title': 'Survived by Age'
            }
        }
    )
]) 
'''
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)
'''

if __name__ == '__main__':
    app.run_server(debug=True)