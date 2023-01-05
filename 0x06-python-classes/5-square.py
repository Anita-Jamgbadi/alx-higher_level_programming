#!/usr/bin/python3
"""Further implementation of Square """


class Square:
    """ the class, square """

    def __init__(self, size=0):
        """ Initializes size """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        """ Gets the size """

        return (self.__size)

    @size.setter
    def size(self, value):
        """ sets size """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >=0')
        else:
            self.__size = value

    def area(self):
        """ Returns Square area """

        return (self.__size * self.__size)

    def my_print(self):
        """ Prints the square """

        if self.__size == 0:
            print()
        for row in range(self.__size):
            for col in range(self.__size):
                print('#', end='')
            print()
