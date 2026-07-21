#!/usr/bin/python3
"""
Module for returning the dictionary description for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object with simple data structures.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary of serializable attributes.
    """
    return obj.__dict__
