# SI507_Final

Xinyue(Joy) Huang

[Link to this repository](https://github.com/heybigjoy/SI507_Final)

---

## Project Description

My project will aggregate artist and exhibiton data in MoMA and allow a user see the gender distribution of artists participated in exhibition in MoMA by year by inputting different data into a URL. There will be a route for looking at the visualizations of gender distribution. In another route, data will also be displayed using HTML tables to show all the information with specific details.

## How to run

1. First, you should install all requirements with `pip install -r requirements.txt`
2. Second, you should run `python3 SI507project.py runserver`

## How to use

1. A useful instruction goes here
2. A useful second step here
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

## Routes in this application
- `/home` -> this is the home page
- `/exhibitions` -> this route has HTML table of all the exhibition information
- `/artists` -> this route has HTML table of all the artists information
- `/gender/<year>` -> this route allow user to find out gender distribution of artists participated in exhibitons of a specific year

## How to run tests
1. run `python3 SI507project_tests.py`

## In this repository:
- SI507project_tools.py
- SI507project_tests.py
- /sample_data
  - database_plan.png
  - MoMAExhibitions1929to1989_clean_sample.py
  - moma_data_sample.sqlite
- MoMAExhibitions1929to1989.py
- requirements.txt
- README.md

---
## My Progress and My Next step
- I have now completed cleaning all my data from a downloaded dataset from MoMA, the next step will be putting the data in to a sqlite file.
- I have defined some possible functions in the SI507project_tools.py, but they are not completely functional for now.
- I have only set the route of the greeting for the Flask application, more will be able to set up later.
- I have now experimenting some modules for data visualization, but I haven't incorporate into the code yet, therefore my requirements.txt is not complete, it will change for the final submission.
-



---
## Code Requirements for Grading
Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [ ] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [ ] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [ ] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [ ] Includes at least 3 different routes
- [ ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [ ] Interactions with a database that has at least 2 tables
- [ ] At least 1 relationship between 2 tables in database
- [ ] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [x] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [ ] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [ ] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
