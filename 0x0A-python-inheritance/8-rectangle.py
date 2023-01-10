#!/usr/bin/python3
""" This module contains a class called base geometry """


class BaseGeometry():
    """ Base geometry class """

    def area(self):
        """ Calculates area """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if not isinstance(name, str):
            raise TypeError('{} must be an string'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """ Rectangle inherits fron BaseGeometry """

    def __init__(self, width, height):
        """ Initialize a rectangle """

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
