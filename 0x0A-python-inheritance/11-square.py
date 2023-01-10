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

    def area(self):
        """ Return the area of the rect """

        return (self.__width * self.__height)

    def __str__(self):
        """ prints a rect to stdout """

        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))


class Square(Rectangle):
    """ A square is also a rectangle """

    def __init__(self, size):
        """ initialize a square """

        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ prints a nice square """

        return ('[Square] {}/{}'.format(self.__size, self.__size))
