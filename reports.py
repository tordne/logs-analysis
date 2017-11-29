#!/usr/bin/env python3

import psycopg2


def popular_article():
    '''
    Connect to the news database and
    extract the 3 most popular articles.
    '''

    pass


if __name__ == '__main__':
    # Open the database and store the connection in con
    con = psycopg2.connect("dbname=news")
    # Assign a cursor 'c' to the connection
    c = con.cursor()

    # 1. What are the 3 most popular articles.
    popular_article()

    # Close the Database
    con.close()
