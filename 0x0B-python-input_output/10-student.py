#!/usr/bin/python3
""" A class Student """


class Student:
    """ This is a class, student """

    def __init__(self, first_name, last_name, age):
        """ Initializes the student with a firstName, lastName, age """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return the dict representation of student """

        if (type(attrs) == list and all (type(txt) == str for txt in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}

        return self.__dict__
