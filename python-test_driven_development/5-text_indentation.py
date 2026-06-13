#!/usr/bin/python3
"""Module that contains text_indentation function"""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    skip_space = False

    while i < len(text):
        char = text[i]

        if char in ".?:":
            print(char)
            print()
            skip_space = True

        elif char == " " and skip_space:
            pass

        else:
            if skip_space:
                skip_space = False
            print(char, end="")

        i += 1

