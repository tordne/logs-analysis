#!/usr/bin/env python3

import psycopg2


def create_view():
    '''
    Connect to the news database and
    first drop the VIEW info_log if exists
    then create a VIEW info_log which joins info about the author
    and articles with the logs

    The WITH query makes 2 lists
        * slug_list
        * log_list

    slug_list:
        * Takes the author, title and slug from all the articles
        * Modifies the slug and add a % in front of the slug

    log_list:
        * Takes the path and creates a num column
        * It groups all the same path together and counts the total of each

    The main SELECT:
        * Outputs the author, title, path and num
        * It compares both log_list and slug_list
        * It will look in all the paths
          and will only return the ones which compare to path_q
    '''
    c.execute("DROP VIEW IF EXISTS info_log")
    c.execute(
        "CREATE VIEW info_log AS \
        WITH slug_list AS ( \
        SELECT author, title, '%' || slug AS path_q \
        FROM articles \
        ), log_list AS ( \
        SELECT path, count(*) AS num \
        FROM log \
        GROUP BY path ) \
        SELECT author, title, path, num \
        FROM slug_list, log_list \
        WHERE path LIKE path_q"
    )


def popular_article():
    '''
    Use the info_log VIEW and extract the following information:
        * title and num

    The list will be ordered with the most views on top and limited to the first 3 # noqa
    '''
    c.execute(
        "SELECT title, num \
        FROM info_log \
        ORDER BY num DESC \
        LIMIT 3"
    )
    a = c.fetchall()
    return a


def popular_authors():
    '''
    Using the info_log VIEW and extract the following information:
            * author id and num of views

    There will be a join between the authors and info_log tables
    to extract the names of the authors.
    The table will group all the articles together by author
    and it will make a SUM() of the number of views of all articles per author

    This list will be ordered by most views first.
    '''
    c.execute(
        "SELECT name, sum(num) AS total \
        FROM authors RIGHT JOIN info_log \
        ON authors.id = info_log.author \
        GROUP BY name \
        ORDER BY total DESC"
    )
    a = c.fetchall()
    return a


def days_with_errors():
    '''
    Using the log table calculate the percentage of errors per day
    and list the days with more than 1% of errors

    The WITH statement consist of 3 lists
        * list_total: A list with 2 culumns Date and the total requests per day
        * list_error: list all the 404 reqs, grouped in date and total columns
        * list_perc: This list calculates the percentage per day

    The main SELECT uses list_perc and only shows the days with more than 1% errors # noqa
    '''
    c.execute(
        "WITH list_total AS ( \
        SELECT date(time) AS lt_date, count(date(time)) AS lt_total \
        FROM log \
        GROUP BY lt_date \
        ), list_error AS ( \
        SELECT date(time) as le_date, count(date(time)) AS le_total \
        FROM log \
        WHERE status LIKE '404%' \
        GROUP BY le_date \
        ), list_perc AS ( \
        SELECT lt_date, ( le_total * 100 / lt_total ) AS perc_error_req  \
        FROM list_total AS lt JOIN list_error AS le \
        ON lt.lt_date = le.le_date ) \
        SELECT to_char(lt_date, 'FMMonth dd, YYYY') AS re_date, \
        perc_error_req \
        FROM list_perc \
        WHERE perc_error_req >= 1"
    )
    a = c.fetchall()
    return a


if __name__ == '__main__':
    # Open the database and store the connection in con
    con = psycopg2.connect("dbname=news")
    # Assign a cursor 'c' to the connection
    c = con.cursor()

    # First drop if exists and then reate a VIEW called info_log
    create_view()

    # 1. What are the 3 most popular articles
    print("The 3 most popular articles")
    print("===========================")
    for title, views in popular_article():
        print("{} -- {} views".format(title, views))
    print("")

    # 2. What are the most popular authors from a descending list
    print("The most popular authors")
    print("========================")
    for name, views in popular_authors():
        print("{} -- {} views".format(name, views))
    print("")

    # 3. Days with more than 1% error requests
    print("Days with more than 1% error requests")
    print("=====================================")
    for date, perc_error_req in days_with_errors():
        print("{} -- {}% errors".format(date, perc_error_req))

    # Close the Database
    con.close()
