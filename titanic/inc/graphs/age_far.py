import dash_core_components as dcc
import dash_html_components as html

import sys, os
BASE_PATH = os.path.abspath(__file__+ './../../')
sys.path.append(BASE_PATH)

from inc.prep import *
from inc.styles.style import *


# PREPARATION
'''Escolher grupo de idade (ex.Criança) mostrar gráfico de barra do número de pessoas referentes ao valor pago'''
fare_age = []
fares_age = [15, 30, 40, 70, 90, 130, 220, 300, 600]
for fare in fares_age:
    df_fare = df[(df['Fare'] >= fare)]
    age_fare = df_fare['Age'].value_counts()
    #print(df_fare['Age'].values())
    #age_fare = [age_fare['female'], age_fare['male']]
    fare_age.append(sex_fare)


# FUNCTION CREATE GRAPH
def create_graph(app):
    return  'TODO'