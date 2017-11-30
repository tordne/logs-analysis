# Logs Analysis -- Udacity FSWD -- Project 3
##Synopsis
This reporting tool answers 3 specific questions using psycopg2 and a postgresql database.
The Database was created by Udacity and cosisted of several articles written by a handful of authors and a logs table with all the views of these articles.
Udacity required for the 3 questions to be answered each in a single database query.
#### 1. What are the most popular three articles of all time?
The information extracted from the database is a sorted list with the most popular article at the top.
With the following syntax:
`'Title of the article' -- 19 views`
#### 2. Who are the most popular article authors of all time?
Sum up all the different articles per author and check which one gets the most page views.
The information extracted from the database is a sorted list with the most popular author at the top.
With the following syntax:
`Agatha Christie -- 29 views`
#### 3. On which days did more than 1% of requests lead to errors?
The information extracted from the log table contains 2 HTTP status codes 404 and 200.
With the following syntax:
`November 28, 2017 -- 39% errors`

## Prerequisites
This project was written in Python 3.6 and postgresql 9.5.10

### Linux Instructions
Check you have the correct versions installed with
`python3 --version`
and for postgresql
`psql --version`

## How to install
### Linux Instructions
#### Download Project
Open a terminal command line and download the full project:
`git clone https://github.com/tordne/logs-analysis.git`

#### Virtual Environment
Enter the newly created folder and create a new venv
`python3 -m venv env`
Activate the environment
`source env/bin/activate`
and install all the required packages
`pip install -r requirements.txt`

#### News database
First unzip the Database
`unzip newsdata.zip`
Then import the database into postgresql with
`psql -d news -f newsdata.sql`

## How to run the site
### Linux Instructions
Open a terminal command line and go to the projects directory, start the venv with:
`source env/bin/activate`
and run the reporting program with:
`python reports.py`

## Project contents
### reports.py
This is the only program file containing all the code to run the app.
The file contains several a main function which outputs all the data to the terminal.

There are 4 functions
* create_view(): this creates info_log which is used by 'popular articles' and 'popular authors'
* popular_article(): this returns a list of the 3 most popular articles
* popular_authors(): this returns a list of all the authors ordered by most views.
* days_with_errors: this returns a list of all the days with more than 1% error requests.

All the VIEWS are created and dropped if exists.