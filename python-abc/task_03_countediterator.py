#!/usr/bin/env python3
"""CountedIterator mlass"""


class CountedIterator:
    """Define a class CountedIterator"""

    def __init__(self, iterable):
        """Initialize iterator and counter """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Return counter"""
        return self.counter

    def __next__(self):
        """Return next item and increment counter"""
        item = next(self.iterator)
        self.counter += 1
        return item
