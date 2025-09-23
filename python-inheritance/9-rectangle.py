#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Instantiates a Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.

        Raises:
            TypeError/ValueError: If width or height is invalid.
        """
        # Vérification que width et height sont des entiers positifs
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Stockage privé
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Character string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
