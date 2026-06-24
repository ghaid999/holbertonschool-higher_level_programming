#!/usr/bin/python3
"""Module that defines Square"""

Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize square"""
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Return square area"""
        return self.__size* self.__size

