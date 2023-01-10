#!/usr/bin/python3
""" This module uses from_json_string to return an
obj repped by json string """
import json


def from_json_string(my_str):
    """ return an obj repped by json string """

    return json.loads(my_str)
