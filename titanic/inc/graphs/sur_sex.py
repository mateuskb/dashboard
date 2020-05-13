import dash_core_components as dcc
import dash_html_components as html

import sys, os
BASE_PATH = os.path.abspath(__file__+ './../../')
sys.path.append(BASE_PATH)

from inc.prep import *
from inc.styles.style import *


# PREPARATION
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


# FUNCTION CREATE GRAPH
def create_graph(app):
    return  html.Div([
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
                html.P(f"Women had {won_sur_perc}% chance of surviving.", style=styles['H1'])
            ])