#!/usr/bin/python3
""" a rebel class that inherits from int """


class MyInt(int):
    """ this class inverts inverts == and != """

    def __eq__(self, value):
        """ change == to != """
        return self.real != value

    def __ne__(self, value):
        """ swap != to =="""
        return self.real == value
