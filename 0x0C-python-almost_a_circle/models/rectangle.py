#!/usr/bin/python3
""" This module contains the rectangle class """


from models.base import Base


class Rectangle(Base):
    """ This class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the rectangle class """

        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')

        self.__width = width
        
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')

        self.__height = height

        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')

        self.__x = x

        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')

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
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ Set value for height """

        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @x.setter
    def x(self, value):
        """ Set value for x """

        if type(value) is not int:
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @y.setter
    def y(self, value):
        """ Set value for y """

        if type(value) is not int:
            raise TypeError('y must be an integer')

        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value
