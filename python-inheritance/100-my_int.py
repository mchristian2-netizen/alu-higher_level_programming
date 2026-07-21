#!/usr/bin/python3
"""
Module for MyInt class that inverts == and != operators.
"""


class MyInt(int):
    """
    MyInt inherits from int but reverses the behavior of == and !=.
    """

    def __eq__(self, other):
        """
        Overrides == to return the opposite of the normal comparison.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides != to return the opposite of the normal comparison.
        """
        return super().__eq__(other)
