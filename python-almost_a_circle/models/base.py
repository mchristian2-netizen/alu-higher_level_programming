#!/usr/bin/python3
"""
Base class for all other classes in this project.
Manages the id attribute.
"""
import json


class Base:
    """Base class with private class attribute __nb_objects."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): The id to assign. If None, increments __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string. If list is None or empty, returns "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances inheriting from Base.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(dict_list)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list represented by json_string.

        Args:
            json_string (str): String representing a list of dictionaries.

        Returns:
            list: List of dictionaries. If json_string is None or empty, returns [].
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set.

        Args:
            **dictionary: Keyword arguments representing attribute values.

        Returns:
            Base: Instance of cls with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # width, height
        elif cls.__name__ == "Square":
            dummy = cls(1)     # size
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a JSON file.

        Returns:
            list: Instances of cls. If file doesn't exist, returns [].
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                json_str = f.read()
        except FileNotFoundError:
            return []
        dict_list = cls.from_json_string(json_str)
        instances = [cls.create(**d) for d in dict_list]
        return instances
