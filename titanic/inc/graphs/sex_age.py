import dash_core_components as dcc
import dash_html_components as html

import sys, os
BASE_PATH = os.path.abspath(__file__+ './../../')
sys.path.append(BASE_PATH)

from inc.prep import *
from inc.styles.style import *


# PREPARATION
age_sex = []
ages = [[0, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90]]
for age in ages:
    df_age = df[(df['Age'] >= age[0]) & (df['Age'] < age[1])]
    sex_age = df_age['Sex'].value_counts()
    sex_age = [sex_age['female'] if 'female' in sex_age else 0 , sex_age['male'] if 'male' in sex_age else 0]
    age_sex.append(sex_age)


# FUNCTION CREATE GRAPH
def create_graph(app):
    return  dcc.Graph(
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
            )