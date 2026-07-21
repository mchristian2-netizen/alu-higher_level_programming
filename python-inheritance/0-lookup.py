#!/usr/bin/python3
"""
Module for lookup function.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: List of attributes and methods.
    """
    return dir(obj)
