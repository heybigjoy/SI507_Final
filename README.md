# SI507_Final

Xinyue(Joy) Huang

[Link to this repository](https://github.com/heybigjoy/SI507_Final)

---

## Project Description

My project will aggregate artist and exhibiton data in MoMA from 1929 to 1989 and allow a user see the gender distribution of artists participated in exhibition in MoMA by year by inputing year constraints in search form, or directly inputting different data into a URL. There will be a route for looking at the visualizations of gender distribution through years in scatter graph, and another route for the gender distribution of a specific in pie chart.

## How to run

1. First, you should install all requirements with `pip install -r requirements.txt`
2. Second, you should run `python3 SI507project.py runserver`

## How to use

1. First, in your browser, put `localhost:5000` in the URL. (This has to be done before putting in anyother urls)
2. Second, you can navigate by clicking links in the home page, to search or view all data.
3. Third, in either one of the search pages, input numbers between 1929 to 1989 in the text field, and click submit to see the visualization of the data.
4. Or, you can also type the URLs mannually(see below), to navigate through different pages.

## Routes in this application
- `/` -> this is the home page, which also allow user to access other links.
- `/count/<FromYear>/<ToYear>` -> this route visualize the gender distribution in a specific year range in a scatter graph.
- `/count/<Year>` -> this route visualize the gender distribution of a specific year in a pie chart.
- `/search/yearrange` -> this route allow user to input a year range into a form, which will lead to the according diagram page.
- `/search/specificyear` -> this route allow user to input a single year into a form, which will lead to the according diagram page.

## How to run tests
1. run `python3 SI507project_tests.py`

## In this repository:
- SI507project_tools.py
- SI507project_tests.py
- /sample_data
  - database_plan.png
  - MoMAExhibitions1929to1989_clean_sample.py
  - moma_data_sample.sqlite
  - pie_chart_sample.png
  - scatter_graph_sample_png
- /templates
  - index.html
  - search_year.html
  - search_year_range.html
  - show_gender.html
  - gender_pie.html
- MoMAExhibitions1929to1989.py
- requirements.txt
- README.md

---
## Main Features/Requirements I have Completed
- I have organized and cleaned up a downloaded dataset, MoMAExhibitions1929to1989.csv (from the MoMA github page) of the exhibitions and artists information from 1929 to 1989 into a clean csv file (MoMAExhibitions1929to1989_clean.csv).
- I set up the SQL database (moma_data.sqlite) with three tables: Artists, Exhibitions, and a joint table of Exhibition_Artist
- I defined different functions to manipulate the data, focusing on counting the number of artists of different genders of specific year, which helps provide data to my data visualization.
- I used a plotly module to visualize my data into scatter graph and pie chart.
- I set up different routes of my Flask application in my SI507project.py file, which allow user to navigate through different pages.
- I incorporate wtforms module to handling forms in Flask to allow user to input information to search. 
- I set up different HTML templates to layout my pages in the templates folder.
- I set up tests in the SI507project_tests.py file to test some results in the csv file and the count function have the correct results.

---
## Code Requirements for Grading
Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [x] Use of a new module: Plotly
- [x] Use of a second new module: wtforms
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [x] A many-to-many relationship in your database structure: between Artists and Exhibitions
- [x] At least one form in your Flask application: use it for search
- [x] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s: links are in the index page, and some of them can be access through search page.
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
