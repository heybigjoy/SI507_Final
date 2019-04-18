# Import statements necessary
from flask import Flask
from SI507project_tools import *

# My goal:
# Set up application
app = Flask(__name__)

# Routes
@app.route('/')
def welcome():
    create_table()
    return '<h1>Hello! Welcome to the movies app!</h1>'

@app.route('/new/movie/<title>/<rating>/<director>')
def new_movie(title, rating, director):
    id = insert_director((director,))
    insert_movie(title, float(rating), id)
    return 'saving new movie {} by {} to our database'.format(title, director)

@app.route('/movies/all')
def movie_data():
    return present_movie()

@app.route('/directors/all')
def director_data():
    return present_director_list()

if __name__ == "__main__":
    app.run(debug=True)
