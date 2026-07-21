#!/usr/bin/python3
"""
Module for checking if object is an instance of a class that inherited from.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if inherited from, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
