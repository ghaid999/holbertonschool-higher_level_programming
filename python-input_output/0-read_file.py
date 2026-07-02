#!/usr/bin/python3
"""Module that provides a function to read a UTF-8 text file."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
