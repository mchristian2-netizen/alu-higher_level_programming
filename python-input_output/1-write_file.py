#!/usr/bin/python3
"""
Module for writing a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file and returns the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The string to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
