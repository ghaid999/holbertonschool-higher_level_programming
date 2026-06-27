#!/usr/bin/env python3
"""Containing Shape class and its inheritances."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract Shape class."""

    @abstractmethod
    def area(self):
        """Return area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initialize circle."""
        self.radius = radius

    def area(self):
        """Calculate area."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * (self.width + self.height)


def shape_info(arg):
    """Print shape information."""
    area = arg.area()
    perimeter = arg.perimeter()

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
