#!/usr/bin/python3
"""
Module for Square class with custom string representation.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with custom string representation."""

    def __init__(self, size):
        """
        Initialize a Square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is <= 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
