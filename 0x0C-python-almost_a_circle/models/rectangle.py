#!/usr/bin/python3
"""A Rectangle class"""
from base import Base


class Rectangle(Base):
    """Defines a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates a Rectangle object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieves the width of a Rectangle object"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of a rectangle object
        Args:
            value (int): value of rectangle width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of a rectangle object"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of a rectangle height
        Args:
            value (int): value of rectangle height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes the area of Rectangle object"""
        return self.__width * self.__height

    def display(self):
        """Prints a graphical representation of rectangle object"""
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
            for n in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
            __class__.__name__,
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        )

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute of the object
        Args:
            args (list): list of arguments passed to the function
            kwargs (dict): contains named arguments passed
        """
        if args is not None and len(args):
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.__width = v
                elif k == 2:
                    self.__height = v
                elif k == 3:
                    self.__x = v
                elif k == 4:
                    self.__y = v
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v
