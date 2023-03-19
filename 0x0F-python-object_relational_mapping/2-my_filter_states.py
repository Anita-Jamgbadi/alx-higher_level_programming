#!/usr/bin/python3
'''
takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
'''

import MySQLdb as db
from sys import argv

'''
This module does what is explained above
'''
if __name__ == '__main__':
    my_db = db.connect(
            host='localhost', port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])

    my_cursor = my_db.cursor()

    my_cursor.execute(
            "SELECT * FROM states WHERE NAME LIKE BINARY '{}' ORDER BY \
                    states.id ASC".format(argv[4]))

    returned = my_cursor.fetchall()

    for row in returned:
        print(row)
