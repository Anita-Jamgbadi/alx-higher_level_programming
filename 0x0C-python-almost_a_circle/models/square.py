#!/usr/bin/python3
""" This module is a square that inherits from rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ This shows that a square is also a rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Init the square """

        self.size = size
        self.x = x
        self.y = y
        self.width = size
        self.height = size
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Prints info about the square """

        return (f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}')
