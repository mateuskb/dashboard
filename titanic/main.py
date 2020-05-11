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

# Preparing



# Survived by age
age_sur = []
ages = [[0, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90]]
for age in ages:
    df_age = df[(df['Age'] >= age[0]) & (df['Age'] < age[1])]
    survived = df_age['Survived'].value_counts()
    survived = [survived[0] if 0 in survived else 0, survived[1] if 1 in survived else 0]
    age_sur.append(survived)



#print(survived[0] if 0 in survived else 0)
#print([survived[1] for survived in age_sur])




# Survived each sex
sex_sur = []
sexs = ['male', 'female']
men_sur_perc = 0
wom_sur_perc = 0
for sex in sexs:
    df_sex = df[(df['Sex']==sex)]
    survived = df_sex['Survived'].value_counts()

    if sex == 'male':
        men_sur_perc = (survived[1] / sum(survived))
    else:
        won_sur_perc = (survived[1] / sum(survived))

    survived = [survived[0] if 0 in survived else 0, survived[1] if 1 in survived else 0]
    sex_sur.append(survived)



# Survived by fare price
fare_sur = []
fares = [[0, 15], [15, 40], [40, 90], [90, 200], [200, 513]]
for fare in fares:
    df_fare = df[(df['Fare'] >= fare[0]) & (df['Fare'] < fare[1])]
    survived = df_fare['Survived'].value_counts()
    survived = [survived[0] if 0 in survived else 0, survived[1] if 1 in survived else 0]
    fare_sur.append(survived)



# Survived by class
class_sur = []
classes = [3,2,1]
for clas in classes:
    df_class = df[(df['Pclass']==clas)]
    survived = df_class['Survived'].value_counts()
    survived = [survived[0] if 0 in survived else 0, survived[1] if 1 in survived else 0]
    class_sur.append(survived)


# Sex by fare price
fare_sex = []
fares = [[0, 15], [15, 40], [40, 90], [90, 200], [200, 513]]
for fare in fares:
    df_fare = df[(df['Fare'] >= fare[0]) & (df['Fare'] < fare[1])]
    sex_fare = df_fare['Sex'].value_counts()
    sex_fare = [sex_fare['female'], sex_fare['male']]
    fare_sex.append(sex_fare)


# Age by fare price

'''Escolher grupo de idade (ex.Criança) mostrar gráfico de barra do número de pessoas referentes ao valor pago'''
fare_age = []
fares_age = [15, 30, 40, 70, 90, 130, 220, 300, 600]
for fare in fares_age:
    df_fare = df[(df['Fare'] >= fare)]
    age_fare = df_fare['Age'].value_counts()
    print(df_fare['Age'].values())
    #age_fare = [age_fare['female'], age_fare['male']]
    fare_age.append(sex_fare)



# Sex by age
age_sex = []
ages = [[0, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90]]
for age in ages:
    df_age = df[(df['Age'] >= age[0]) & (df['Age'] < age[1])]
    sex_age = df_age['Sex'].value_counts()
    sex_age = [sex_age['female'] if 'female' in sex_age else 0 , sex_age['male'] if 'male' in sex_age else 0]
    age_sex.append(sex_age)




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
    ),
    dcc.Graph(
        id='titanic-graph_2',
        figure={
            'data': [
                {
                'x': [f'{i}' for i in sexs],
                'y': [survived[1] for survived in sex_sur],
                'name': 'Survived', 
                'type': 'bar',
                'marker': {
                    'color':'rgb(55, 83, 109)'
                    }
                },
                {
                'x': [f'{i}' for i in sexs],
                'y': [survived[0] for survived in sex_sur],
                'name': 'Not survived', 
                'type': 'bar',
                'marker': {
                    'color':'rgb(202, 14, 35)'
                    }
                }
            ],
            'layout': {
                'title': 'Survived by sex'
            }
        }
    ),
    html.P(f"Men had {men_sur_perc}% chance of surviving.", style=styles['H1']),
    html.P(f"Women had {won_sur_perc}% chance of surviving.", style=styles['H1']),
    dcc.Graph(
        id='titanic-graph_3',
        figure={
            'data': [
                {
                'x': [f'{i[0]} - {i[1]}' for i in fares],
                'y': [survived[1] for survived in fare_sur],
                'name': 'Survived', 
                'type': 'bar',
                'marker': {
                    'color':'rgb(55, 83, 109)'
                    }
                },
                {
                'x': [f'{i[0]} - {i[1]}' for i in fares],
                'y': [survived[0] for survived in fare_sur],
                'name': 'Not survived', 
                'type': 'bar',
                'marker': {
                    'color':'rgb(202, 14, 35)'
                    }
                }
            ],
            'layout': {
                'title': 'Survived by Fare price'
            }
        }
    ),

    dcc.Graph(
        id='titanic-graph_4',
        figure={
            'data': [
                {
                'x': [f'{i}' for i in classes],
                'y': [survived[1] for survived in class_sur],
                'name': 'Survived', 
                'type': 'bar',
                'marker': {
                    'color':'rgb(55, 83, 109)'
                    }
                },
                {
                'x': [f'{i}' for i in classes],
                'y': [survived[0] for survived in class_sur],
                'name': 'Not survived', 
                'type': 'bar',
                'marker': {
                    'color':'rgb(202, 14, 35)'
                    }
                }
            ],
            'layout': {
                'title': 'Survived by class'
            }
        }
    ),
    dcc.Graph(
        id='titanic-graph_5',
        figure={
            'data': [
                {
                'x': [f'{i[0]} - {i[1]}' for i in fares],
                'y': [sex[1] for sex in fare_sex],
                'name': 'Men', 
                'type': 'bar',
                'marker': {
                    'color':'rgb(55, 83, 109)'
                    }
                },
                {
                'x': [f'{i[0]} - {i[1]}' for i in fares],
                'y': [sex[0] for sex in fare_sex],
                'name': 'Women', 
                'type': 'bar',
                'marker': {
                    'color':'rgb(202, 14, 35)'
                    }
                }
            ],
            'layout': {
                'title': 'Sex by Fare price'
            }
        }
    ),
    dcc.Graph(
        id='titanic-graph_7',
        figure={
            'data': [
                {
                'x': [f'{i[0]} - {i[1]}' for i in ages],
                'y': [sex[1] for sex in age_sex],
                'name': 'Men', 
                'type': 'bar',
                'marker': {
                    'color':'rgb(55, 83, 109)'
                    }
                },
                {
                'x': [f'{i[0]} - {i[1]}' for i in ages],
                'y': [sex[0] for sex in age_sex],
                'name': 'Women', 
                'type': 'bar',
                'marker': {
                    'color':'rgb(202, 14, 35)'
                    }
                }
            ],
            'layout': {
                'title': 'Sex by Age'
            }
        }
    ),
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