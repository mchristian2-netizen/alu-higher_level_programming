#!/usr/bin/python3
"""
Module for a LockedClass that prevents dynamic attribute creation.
"""


class LockedClass:
    """
    A class that only allows the 'first_name' attribute to be set dynamically.
    Uses __slots__ to restrict attribute creation.
    """
    __slots__ = ['first_name']
