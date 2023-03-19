#!/usr/bin/python3
'''
this script that lists all cities from the
database hbtn_0e_4_usa
'''

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    '''
    Access DB and list all Cities
    '''

    my_db = db.connect(
            host='localhost', port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])

    my_cur = my_db.cursor()

    my_cur.execute(
            'SELECT cities.id, cities.name, states.name \
                    FROM cities JOIN states ON cities.state_id \
                    = states.id ORDER BY cities.id ASC')

    returned = my_cur.fetchall()

    for row in returned:
        print(row)
