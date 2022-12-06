#!/usr/bin/python3
'''
Prints integers from a list, one on each new line
'''


def print_list_integer(my_list=[]):
    for i in my_list:
        print('{:d}'.format(i))
