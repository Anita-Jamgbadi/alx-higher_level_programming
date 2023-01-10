#!/usr/bin/python3
""" this module adds extra attributes to an obj if possible """


def add_attribute(obj, att, value):
    """ Add new att to an obj if possible """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
