#!/usr/bin/python3
"""Module that defines BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise an exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
