#!/usr/bin/python3
""" This module defines a Rectangle """


class Rectangle:
    """ A rectangle with properties and fields """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Assign private instance attributes width and height """

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ Prints the rectangle to the screen with '#' character """

        if self.__width == 0 or self.__height == 0:
            return ('')

        rect = ''
        for x in range(self.__height):
            for y in range(self.__width):
                rect += '#'
            if x < self.__height - 1:
                rect += '\n'
        return (rect)

    def __repr__(self):
        """return a string representation of the rectangle to be able
        to recreate a new instance by using eval()"""

        return ('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        """ Says goodbye when an instance is deleted """

        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """ Calculate and return the area of the rectangle """

        return (self.__width * self.__height)

    def perimeter(self):
        """ Calculates and returns the rectangles perimeter """

        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))
