#!/usr/bin/python3
""" A locked class """


class LockedClass:
    """ Allows init of an attribut called first_name ONLY """

    __slots__ = ['first_name']
