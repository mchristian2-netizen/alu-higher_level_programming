#!/usr/bin/python3
"""
Module for converting an object to its JSON string representation.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to serialize.

    Returns:
        str: The JSON string representation.
    """
    return json.dumps(my_obj)
