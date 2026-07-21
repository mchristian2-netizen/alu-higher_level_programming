#!/usr/bin/python3
"""
Module for appending a string to a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a UTF-8 text file and returns the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The string to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
