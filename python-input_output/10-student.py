#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student ."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the instance."""
        if type(attrs) is list and all(type(item) is str for item in attrs):
            return {key: self.__dict__[key]
                    for key in attrs
                    if key in self.__dict__}

        return self.__dict__
