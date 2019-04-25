# Import statements necessary
import flask
from SI507project_tools import *
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import wtforms
plotly.tools.set_credentials_file(username='Heybigjoy', api_key='aX2IlyeYA0R8HQ6TQaC3')

# My goal:
# Set up application

app = flask.Flask(__name__)

# Routes
@app.route('/')
def welcome():
    cleanup()
    create_table()
    insert_artists()
    insert_exhibitions()
    insert_exhibitions_artists()
    return "Hello, World!"

@app.route('/count/<FromYear>/<ToYear>')
def show_gender(FromYear, ToYear):
    bar = gender_distribution(FromYear, ToYear)
    return flask.render_template('show_gender.html', plot=bar)

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
    app.run(debug = True)
# if __name__ == '__main__':
#     run_simple('localhost', 5000, app,
#                use_reloader=True, use_debugger=True, use_evalex=True)
