#!/usr/bin/python3
"""imports"""


from models.base import Base


class Rectangle(Base):
    """Rect base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init values """
        argVals = [width, height, x, y]
        argNam = ["width", "height", "x", "y"]
        for ind, arg in enumerate(argVals):
            if type(arg) != int:
                raise TypeError(f"{argNam[ind]} must be an integer")
        for ind, arg in enumerate(argVals[0:2]):
            if arg < 1:
                raise ValueError(f"{argNam[ind]} must be > 0")
        for ind, arg in enumerate(argVals[2:]):
            if arg < 0:
                raise ValueError(f"{argNam[ind + 2]} must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def to_dictionary(self):
        """returns dict representation"""
        dic = {'id': self.id, 'width': self.width, 'height': self.height,
               'x': self.x, 'y': self.y}
        return dic

    def area(self):
        return self.width * self.height

    def update(self, *args, **kw):
        """updates values of rectangle **ugly** """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
        else:
            try:
                self.id = kw.get('id', self.id)
                self.width = kw.get('width', self.width)
                self.height = kw.get('height', self.height)
                self.x = kw.get('x', self.x)
                self.y = kw.get('y', self.y)
            except Exception:
                pass

    def display(self):
        """prints a rect"""
        print(f"{chr(10) * self.y}", end="")
        for i in range(self.height):
            print(f"{' ' * self.x}{'#' * self.width}")

    def __str__(self):
        """gets rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.x, self.y,
            self.width, self.height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
