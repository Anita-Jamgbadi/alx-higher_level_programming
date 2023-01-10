#!/usr/bin/python3
""" This module uses class_to_json to return the dictionary
description with simple data structure for json serialization
of an object """


def class_to_json(obj):
    """ Does as above """

    return obj.__dict__
