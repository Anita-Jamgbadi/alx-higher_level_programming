#!/usr/bin/python3
'''
takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
'''

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    '''
    takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa
    '''

    my_db = db.connect(
            host='localhost', port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])

    my_cur = my_db.cursor()

    my_cur.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
            })

    returned = my_cur.fetchall()

    if returned is not None:
        print(", ".join([row[1] for row in returned]))
