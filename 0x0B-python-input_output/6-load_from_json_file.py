#!/usr/bin/python3
""" This module creates an object from a json file """
import json


def load_from_json_file(filename):
    """ create an obj from a json file """
    with open(filename) as f:
        json.load(f)
