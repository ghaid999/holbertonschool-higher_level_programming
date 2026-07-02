#!/usr/bin/python3
"""function  that writes a string to a text file (UTF8)."""


def write_file(filename="", text=""):
    """write a UTF-8 text file """
    with open(filename, "w", encoding="utf-8") as file:
         return file.write(text)
