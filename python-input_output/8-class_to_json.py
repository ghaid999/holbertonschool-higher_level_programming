#!/usr/bin/python3
"""function that returns the dictionary description with simple data structur."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization."""
    return obj.__dict__
