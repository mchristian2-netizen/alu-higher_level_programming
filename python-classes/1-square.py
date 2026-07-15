#!/usr/bin/python3
"""Module for Square class with private size."""

class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
