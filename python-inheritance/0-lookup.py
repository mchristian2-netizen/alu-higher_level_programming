#!/usr/bin/python3
"""
Module for lookup function that returns attributes and methods.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attribute and method names.
    """
    return dir(obj)
