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
    return '<h1>Hello! Welcome to my MoMA app!</h1>'

@app.route('/exhibition')
def exhibiton(title, rating, director):
    pass

@app.route('/artist')
def artists():
    pass

@app.route('exhibition/graph')
def graph():
    pass

if __name__ == "__main__":
    app.run(debug=True)
