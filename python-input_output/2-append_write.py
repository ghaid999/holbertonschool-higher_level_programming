#!/usr/bin/python3
"""function appends a string at the end of a text file (UTF8) """


def append_write(filename="", text=""):
    """appends a UTF-8 text file """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
