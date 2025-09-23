#!/usr/bin/python3
"""
Module 8-rectangle
Defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Instantiates a Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError/ValueError: If width or height is invalid.
        """
        # Vérifie que width et height sont des entiers positifs
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Stocke width et height dans des attributs privés
        self.__width = width
        self.__height = height
