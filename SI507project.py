# Import statements necessary
import flask
from SI507project_tools import *
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from wtforms import Form, IntegerField, SubmitField, validators
from flask_wtf import Form
plotly.tools.set_credentials_file(username='Heybigjoy', api_key='aX2IlyeYA0R8HQ6TQaC3')


# Set up application

app = flask.Flask(__name__)
app.secret_key = 'development key'


class SearchYearRange(Form):
    from_year = IntegerField('fromyear', [
        validators.NumberRange(min=1929, max=1990, message="Year Must between 1929-1990"),
        validators.DataRequired(message="You must input a number"),
    ])

    to_year = IntegerField('toyear', [
        validators.NumberRange(min=1929, max=1990, message="Year Must between 1929-1990"),
        validators.DataRequired(message="You must input a number"),
    ])

    submit = SubmitField('Submit')

class SearchSpecificYear(Form):
    specific_year = IntegerField('specificyear', [
        validators.NumberRange(min=1929, max=1990, message="Year Must between 1929-1990"),
        validators.DataRequired(message="You must input a number"),
    ])

    submit = SubmitField('Submit')

# Routes
@app.route('/')
def welcome():
    cleanup()
    create_table()
    insert_artists()
    insert_exhibitions()
    insert_exhibitions_artists()
    return flask.render_template('index.html')

@app.route('/search/yearrange', methods=('GET', 'POST'))
def seach_year_range():
   form = SearchYearRange(flask.request.form)
   if form.validate_on_submit():
        fromyear = form.from_year.data
        toyear = form.to_year.data
        flask.flash('Search Success!')
        return flask.redirect('/count/'+str(fromyear)+'/'+str(toyear))
   return flask.render_template('search_year_range.html', form=form)

@app.route('/search/specificyear', methods=('GET', 'POST'))
def seach_specific_year():
   form = SearchSpecificYear(flask.request.form)
   if form.validate_on_submit():
        specificyear = form.specific_year.data
        flask.flash('Search Success!')
        return flask.redirect('/count/'+str(specificyear))
   return flask.render_template('search_year.html', form=form)

# @app.route('/search/oneyear')
# def seach():
#    form = SearchForm(wtforms.Form)
#    return flask.render_template('search_year_range.html', form=form)

@app.route('/count/<FromYear>/<ToYear>')
def show_gender(FromYear, ToYear):
    bar = gender_distribution(FromYear, ToYear)
    return flask.render_template('show_gender.html', plot=bar)

@app.route('/count/<Year>')
def gender_pie(Year):
    pie = gender_pie_chart(Year)
    return flask.render_template('gender_pie.html', plot=pie)

if __name__ == '__main__':
    app.run(debug = True)
# if __name__ == '__main__':
#     run_simple('localhost', 5000, app,
#                use_reloader=True, use_debugger=True, use_evalex=True)
