#!/usr/bin/python3
"""
Square class that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class with size, x, y."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of square.
            x (int): x offset.
            y (int): y offset.
            id (int, optional): id.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Get size (same as width)."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size (width and height) with validation."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assign attributes using no-keyword args or keyword args.

        Args:
            *args: Ordered arguments (id, size, x, y).
            **kwargs: Key-value pairs for attributes.
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    if attrs[i] == 'size':
                        self.size = arg
                    else:
                        setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                elif hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
