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
This project was written in Python 3.6.3 and 