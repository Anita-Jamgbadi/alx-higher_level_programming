#!/usr/bin/python3
""" This module returns all available attributes and methods of an object """


def lookup(obj):
    """ Lookup and return a list of the
    available atts and methods for 'obj' """

    return dir(obj)
