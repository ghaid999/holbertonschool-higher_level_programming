#!/usr/bin/env python3
"""pickling a custom object."""

import pickle


class CustomObject:
    """Represent a custom object"""

    def __init__(self, name, age, is_student):
        """Initialize."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display ."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializ"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
