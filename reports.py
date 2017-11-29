#!/usr/bin/env python3

import psycopg2


def popular_article():
    '''
    Connect to the news database and
    extract the 3 most popular articles.

    The WITH query makes 2 lists
        * slug_list
        * log_list

    slug_list:
        * Takes the title and slug from all the articles
        * Modifies the slug and add a % in front of the slug

    log_list:
        * Takes the path and creates a num column
        * It groups all the same path together and counts the total of each

    The main SELECT:
        * Outputs the title and num
        * It compares both log_list and slug_list
        * It will look in all the paths and will only return the ones which compare to path_q
        * The list will be ordered with the most views on top and limited to the first 3
    '''
    c.execute(
        "WITH slug_list AS ( \
        SELECT title, '%' || slug AS path_q \
        FROM articles \
        ), log_list AS ( \
        SELECT path, count(*) AS num \
        FROM log\
        GROUP BY path) \
        SELECT title, num \
        FROM slug_list, log_list \
        WHERE path LIKE path_q \
        ORDER BY num DESC \
        LIMIT 3"
    )
    a = c.fetchall()
    return a


if __name__ == '__main__':
    # Open the database and store the connection in con
    con = psycopg2.connect("dbname=news")
    # Assign a cursor 'c' to the connection
    c = con.cursor()

    # 1. What are the 3 most popular articles.
    for title, views in popular_article():
        print("{} -- {} views".format(title, views))

    # Close the Database
    con.close()
