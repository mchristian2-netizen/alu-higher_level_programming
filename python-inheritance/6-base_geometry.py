#!/usr/bin/python3
"""
Module for BaseGeometry class with area method.
"""


class BaseGeometry:
    """Base geometry class with area method that raises an exception."""

    def area(self):
        """Raises an exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
