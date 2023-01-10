#!/usr/bin/python3
"""This module checks if one class is a sub of another """


def is_same_class(obj, a_class):
    """ Checks if obj is a sub of a_class """

    if type(obj) == a_class:
        return True
    return False
