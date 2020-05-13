import dash_core_components as dcc
import dash_html_components as html

import sys, os
BASE_PATH = os.path.abspath(__file__+ './../../')
sys.path.append(BASE_PATH)

from inc.prep import *
from inc.styles.style import *


# PREPARATION
class_sur = []
classes = [3,2,1]
for clas in classes:
    df_class = df[(df['Pclass']==clas)]
    survived = df_class['Survived'].value_counts()
    survived = [survived[0] if 0 in survived else 0, survived[1] if 1 in survived else 0]
    class_sur.append(survived)

# FUNCTION CREATE GRAPH
def create_graph(app):
    return  dcc.Graph(
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
            )