#!/usr/bin/python3
'''
takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
'''

import MySQLdb as db
from sys import argv

'''
Same as above
'''

if __name__ == '__main__':
    my_db = db.connect(
            host='localhost', port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])

    my_cur = my_db.cursor()

    my_cur.execute(
            'SELECT * FROM states WHERE NAME LIKE BINARY \
                    %(name)s ORDER BY states.id ASC', {'name': argv[4]})

    returned = my_cur.fetchall()

    for row in returned:
        print(row)
