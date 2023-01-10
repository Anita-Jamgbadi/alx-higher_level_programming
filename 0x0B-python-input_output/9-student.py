#!/usr/bin/python3
""" A class Student """


class Student:
    """ This is a class, student """

    def __init__(self, first_name, last_name, age):
        """ Initializes the student with a firstName, lastName, age """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return the dict representation of student """

        return self.__dict__
