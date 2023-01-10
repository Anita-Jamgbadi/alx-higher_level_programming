#!/usr/bin/python3
""" This module uses 'append_write' to append txt
to the end of a file """


def append_write(filename="", text=""):
    """ append text to the end of filename """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
