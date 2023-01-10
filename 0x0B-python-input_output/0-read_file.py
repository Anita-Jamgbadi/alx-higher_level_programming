#!/usr/bin/python3
""" This module contains a read_file function that reads
data from a file and prints it to stdout """


def read_file(filename=""):
    """ Reads data from <filename> and prints to stdout """

    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content, end='')
