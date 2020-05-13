import dash_core_components as dcc
import dash_html_components as html

import sys, os
BASE_PATH = os.path.abspath(__file__+ './../../')
sys.path.append(BASE_PATH)

from inc.prep import *


# PREPARATION
age_sur = []
ages = [[0, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90]]
for age in ages:
    df_age = df[(df['Age'] >= age[0]) & (df['Age'] < age[1])]
    survived = df_age['Survived'].value_counts()
    survived = [survived[0] if 0 in survived else 0, survived[1] if 1 in survived else 0]
    age_sur.append(survived)

#print(survived[0] if 0 in survived else 0)
#print([survived[1] for survived in age_sur])


# FUNCTION CREATE GRAPH
def create_graph(app):
    return  dcc.Graph(
                id='sur-age-graph',
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