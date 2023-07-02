#!/usr/bin/python3
"""imports"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init values"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get values of size"""
        return self.width

    @size.setter
    def size(self, value):
        """set value of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kw):
        """updates the square"""
        if args:
            i = 0
            keys = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, keys[i], arg)
                i += 1
        elif kw:
            for key, value in kw.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary"""
        dyctio = {'id': self.id, 'size': self.size,
               'x': self.x, 'y': self.y}
        return dyctio

    def __str__(self):
        """return rectangle"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")