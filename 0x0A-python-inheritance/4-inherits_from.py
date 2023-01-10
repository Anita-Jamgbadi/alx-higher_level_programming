#!/usr/bin/python3
""" Checks if obj is a sub of a_class """


def inherits_from(obj, a_class):
    """ Checks if obj is a sub of a_class """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
