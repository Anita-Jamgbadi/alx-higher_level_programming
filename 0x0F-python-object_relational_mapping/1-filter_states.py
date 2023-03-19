#!/usr/bin/python
'''
This module lists all states starting with N
'''

import MySQLdb
from sys import argv

if __name__ = '__main__':
    '''
    Fetch data from database
    '''

    connect_db = MySQLdb.connect(
            host='localhost', user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    cur = connect_db.cursor()

    cur.execute("SELECT * FROM states WHERE NAME LIKE BINARY 'N%' \
            ORDER BY states.id ASC")

    returned = cur.fetchall()

    for row in returned:
        print(row)
