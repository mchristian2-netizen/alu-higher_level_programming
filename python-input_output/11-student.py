#!/usr/bin/python3
"""
Module for Student class with reload_from_json method.
"""


class Student:
    """Defines a student with serialization/deserialization."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name.
            last_name (str): The last name.
            age (int): The age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes with names in attrs are returned.

        Args:
            attrs (list): Optional list of attribute names to include.

        Returns:
            dict: A dictionary containing the specified attributes.
        """
        if attrs is None:
            return self.__dict__
        result = {}
        for attr in attrs:
            if attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a dictionary.

        Args:
            json (dict): A dictionary with attribute names as keys and new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
