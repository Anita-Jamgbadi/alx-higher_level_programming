#!/usr/bin/python3
""" This module contains the rectangle class """


from models.base import Base


class Rectangle(Base):
    """ This class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the rectangle class """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ returns the value of width """
        return self.__width

    @property
    def height(self):
        """ returns te value of height """
        return self.__height

    @property
    def x(self):
        """ returns the value of x """
        return self.__x

    @property
    def y(self):
        """ returns the of y """
        return self.__y

    @width.setter
    def width(self, value):
        """ Set value for width """

        if type(value) is not int:
            raise TypeError('Value must be an integer')

        if value <= 0:
            raise ValueError('Value must be greater then 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ Set value for height """

        if type(value) is not int:
            raise TypeError('Value must be an integer')

        if value <= 0:
            raise ValueError('Value must be greater then 0')

        self.__height = value

    @x.setter
    def x(self, value):
        """ Set value for x """

        if type(value) is not int:
            raise TypeError('Value must be an integer')

        if value <= 0:
            raise ValueError('Value must be greater then 0')

        self.__x = value

    @y.setter
    def y(self, value):
        """ Set value for y """

        if type(value) is not int:
            raise TypeError('Value must be an integer')

        if value <= 0:
            raise ValueError('Value must be greater then 0')

        self.__y = value
