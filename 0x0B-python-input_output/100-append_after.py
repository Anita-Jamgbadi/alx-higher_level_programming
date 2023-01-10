#!/usr/bin/python3
""" Appends text after every occurence of a specified string """


def append_after(filename="", search_string="", new_string=""):
    """ As above """

    txt = ''
    with open(filename) as f:
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, 'w') as f:
        f.write(txt)
