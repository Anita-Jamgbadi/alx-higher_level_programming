#!/usr/bin/python3
'''
This Module lists all states from a db
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    '''
    Fetch states from db
    '''
    connect_db = MySqldb.connect(
            host='localhost', user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    cursor_db = connect_db.cursor()

    cursor_db.execute("SELECT * FROM states")

    returned = cursor_db.fetchall()

    for row in returned:
        print(row)
