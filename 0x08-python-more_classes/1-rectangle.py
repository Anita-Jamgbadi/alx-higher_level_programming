#!/usr/bin/python3
""" This module defines a Rectangle """


class Rectangle:
    """ A rectangle with properties and fields """

    def __init__(self, width=0, height=0):
        """ Assign private instance attributes width and height """

        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(width, int):
            raise TypeError('width must be an integer')

        if height < 0:
            raise ValueError('height must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for the property 'width' """

        return (self.__width)

    @width.setter
    def width(self, value):
        """ Width setter with conditons: type(value) == int & w >= 0 """

        if value < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        self.__width = value

    @property
    def height(self):
        """ Getter for the property 'height' """

        return (self.__height)

    @height.setter
    def height(self, value):
        """ Height setter with conditons: type(value) == int & h >= 0 """

        if value < 0:
            raise ValueError('height must be >= 0')
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        self.__height = value
