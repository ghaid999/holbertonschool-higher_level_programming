#!/usr/bin/python3
"""function that returns the dictionary description with object"""


def class_to_json(obj):
    """Return the dictionary description of an opject"""
    return obj.__dict__
