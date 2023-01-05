#!/usr/bin/python3
"""Further implementation of Square """


class Square:
    """ the class, square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes size """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

        """ Position """
        if not isinstance(position, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

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

    @property
    def position(self):
        """ Gets the position """

        return self.__position

    @position.setter
    def position(self, value):
        """ sets position on the consition that the value is a tuple """

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """ Prints the square """

        if self.__size == 0:
            print()

        for x in range(self.__position[1]):
            print()

        for row in range(self.__size):

            for y in range(self.__position[0]):
                print(' ', end='')

            for col in range(self.__size):
                print('#', end='')

            print()
