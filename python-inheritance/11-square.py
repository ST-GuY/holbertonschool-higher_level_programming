#!/usr/bin/python3
"""
Module 10-square
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """
        Instantiates a Square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError/ValueError: If size is invalid.
        """
        # Vérification que size est un entier positif via integer_validator
        self.integer_validator("size", size)

        # Stockage privé
        self.__size = size

        # Appel du constructeur de Rectangle avec width=height=size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the rectangle."""
        return self.__size * self.__size
