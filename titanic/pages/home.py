import dash_core_components as dcc
import dash_html_components as html

import sys, os
BASE_PATH = os.path.abspath(__file__+ './../')
sys.path.append(BASE_PATH)

from inc.prep import *
from inc.styles.style import *
from inc.graphs import (
    sur_age,
    sur_sex,
    sur_far,
    sur_cla,
    sex_age,
    sex_far
)

def create_layout(app):
    return  html.Div([
                html.H1("Titanic Data Analysis", style=styles['H1']),
                sur_age.create_graph(app), 
                sur_sex.create_graph(app),
                sur_far.create_graph(app),
                sur_cla.create_graph(app),
                sex_age.create_graph(app),
                sex_far.create_graph(app)
            ]) 
