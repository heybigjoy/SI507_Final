# Import statements necessary
import flask
from SI507project_tools import *
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
import dash
import dash_core_components as dcc
import dash_html_components as html


# My goal:
# Set up application

server = flask.Flask(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

dash_app1 = dash.Dash(__name__, server = server, url_base_pathname='/exhibitions/all/', external_stylesheets=external_stylesheets)
dash_app2 = dash.Dash(__name__, server = server, url_base_pathname='/reports/', external_stylesheets=external_stylesheets)
dash_app1.layout = html.Div(children=[
    html.H1(children='MoMA App'),

    html.Div(children='''
        This is a diagram to show the gender distribution of MoMA's Exhibitions from 1929 to 1989.
    '''),

    dcc.Graph(
        id='gender-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [1, 2, 3], 'type': 'bar', 'name': 'Male'},
                {'x': [1, 2, 3], 'y':[1, 2, 3], 'type': 'bar', 'name': u'Female'},
            ],
            'layout': {
                'title': 'MoMa Exhibition Visualization'
            }
        }
    )
])


dash_app2.layout = html.Div([html.H1('Hi there, I am app2 for reports/')])

app = DispatcherMiddleware(server, {
    '/dash1/': dash_app1.server,
    '/dash2/': dash_app2.server
})

# Routes
@server.route('/')
def welcome():
    cleanup()
    create_table()
    insert_artists()
    insert_exhibitions()
    insert_exhibitions_artists()
    return "Hello! Welcome to my MoMa Application!"

@server.route('/count/<Year>/<Gender>')
def count(Year, Gender):
    return str(Count_Exhibition(Year, Gender))

@server.route('/count/all')
def count_all():
    male_count = 0
    female_count = 0
    count_list = []
    for year in range(1929,1990):
        male_count += Count_Exhibition(year, 'male')
        female_count += Count_Exhibition(year, 'female' )
        count_list.append((male_count,female_count))
    return str(count_list)

# @server.route('/exhibitions/all/')
# def render_reports():
#     return flask.redirect('/dash1/')
#
# @server.route('/exhibitions/<year>')
# def show_exhibitions(year):
#     return str(Gender_Distribution(year))

# @server.route('/male')
# def show_male():
#     return str(Male_List())

# @server.route('/exhibitions/all')
# def exhibitons_data():
#     pass

# @server.route('/artists')
# def artists():
#     pass
#
# @server.route('/exhibition/graph')
# def graph():
#     pass

if __name__ == '__main__':
    run_simple('localhost', 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)
