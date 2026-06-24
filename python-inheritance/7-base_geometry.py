#!/usr/bin/python3
"""Module that defines BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise an exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
