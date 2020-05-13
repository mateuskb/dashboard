import dash_core_components as dcc
import dash_html_components as html

import sys, os
BASE_PATH = os.path.abspath(__file__+ './../../')
sys.path.append(BASE_PATH)

from inc.prep import *
from inc.styles.style import *


# PREPARATION
fare_sur = []
fares = [[0, 15], [15, 40], [40, 90], [90, 200], [200, 513]]
for fare in fares:
    df_fare = df[(df['Fare'] >= fare[0]) & (df['Fare'] < fare[1])]
    survived = df_fare['Survived'].value_counts()
    survived = [survived[0] if 0 in survived else 0, survived[1] if 1 in survived else 0]
    fare_sur.append(survived)

# FUNCTION CREATE GRAPH
def create_graph(app):
    return  dcc.Graph(
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
            )