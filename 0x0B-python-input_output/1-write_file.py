#!/usr/bin/python3
""" This module contains write_file which writes into a file
and returns the no of characters written """


def write_file(filename="", text=""):
    """ write text into filename and return the no of chars written """

    with open(filename, 'r+', encoding='utf-8') as f:
        return f.write(text)
