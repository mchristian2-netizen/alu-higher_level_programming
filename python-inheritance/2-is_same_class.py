#!/usr/bin/python3
"""
Module for checking exact instance of a class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if exactly an instance, False otherwise.
    """
    return type(obj) is a_class
