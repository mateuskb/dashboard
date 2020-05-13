import dash_core_components as dcc
import dash_html_components as html

import sys, os
BASE_PATH = os.path.abspath(__file__+ './../../')
sys.path.append(BASE_PATH)

from inc.prep import *


# PREPARATION
fare_sex = []
fares = [[0, 15], [15, 40], [40, 90], [90, 200], [200, 513]]
for fare in fares:
    df_fare = df[(df['Fare'] >= fare[0]) & (df['Fare'] < fare[1])]
    sex_fare = df_fare['Sex'].value_counts()
    sex_fare = [sex_fare['female'], sex_fare['male']]
    fare_sex.append(sex_fare)


#print(survived[0] if 0 in survived else 0)
#print([survived[1] for survived in age_sur])


# FUNCTION CREATE GRAPH
def create_graph(app):
    return  dcc.Graph(
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
            )