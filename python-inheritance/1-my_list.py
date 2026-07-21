#!/usr/bin/python3
"""
Module for MyList class that inherits from list.
"""


class MyList(list):
    """
    A custom list class with a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        The original list remains unchanged.
        """
        print(sorted(self))
