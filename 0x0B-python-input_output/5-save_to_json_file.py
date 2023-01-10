#!/usr/bin/python3
""" writes an obj to a text file in json representation """
import json


def save_to_json_file(my_obj, filename):
    """ write my_obj into filename using json rep """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
