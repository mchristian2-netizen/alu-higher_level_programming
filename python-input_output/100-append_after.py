#!/usr/bin/python3
"""
Module for inserting a line of text after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after lines containing search_string.
    """
    new_content = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            new_content.append(line)
            if search_string in line:
                new_content.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_content)
