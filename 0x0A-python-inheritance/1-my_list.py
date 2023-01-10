#!/usr/bin/python3
""" This module prints a list in ascending order """


class MyList(list):
    """ This class inherits from list """

    def print_sorted(self):
        """ This function prints an int list in ascending order """

        print(sorted(self))
