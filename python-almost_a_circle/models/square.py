#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class inheriting from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ init values """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns information """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """ returns size """
        return self.width

    @size.setter
    def size(self, value):
        """ sets size of square """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kw):
        """updates values of square"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            try:
                self.id = kw.get('id', self.id)
                self.size = kw.get('size', self.size)
                self.x = kw.get('x', self.x)
                self.y = kw.get('y', self.y)
            except Exception:
                pass

    def to_dictionary(self):
        """ returns dict """
        selfDict = {'id': self.id, 'x': self.x,
                    'size': self.size, 'y': self.y}
        return selfDict
