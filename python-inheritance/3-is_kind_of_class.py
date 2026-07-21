#!/usr/bin/python3
"""
Module for checking if object is an instance of or inherited from a class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or inherited from, a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if instance or inherited, False otherwise.
    """
    return isinstance(obj, a_class)
