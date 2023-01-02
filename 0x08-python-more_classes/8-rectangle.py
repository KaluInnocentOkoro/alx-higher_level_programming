#!/usr/bin/python3
"""A Rectangle class"""


class Rectangle:
    """Defines a Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiates a Rectangle object
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Initializes the width of the rectangle object
        Args:
            value (int): value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of the height of the Rectangle object"""
        return self.__height

    @height.setter
    def height(self, value):
        """initializes the height of the rectangle object
        Args:
            value (int): value of the height of rectangle object
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes and returns the area of a rectangle object"""
        return self.__width * self.__height

    def perimeter(self):
        """computes and returns the perimeter of rectangle object"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the rectangle object with '#'"""
        my_rect = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for idx in range(0, self.__height):
            my_rect.append(str(self.print_symbol) * self.__width)
        return "\n".join(my_rect)

    def __repr__(self):
        """return a string representation of the rectangle object"""
        return "{}({}, {})".format(__class__.__name__, self.__width,
                                   self.__height)

    def __del__(self):
        """deletes a Rectangle object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two instances of a Rectangle
        Args:
            rect_1 (Rectangle)
            rect_2 (Rectangle)
        Return:
            rect_1 if area is bigger else rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 >= area2:
            return rect_1
        return rect_2
