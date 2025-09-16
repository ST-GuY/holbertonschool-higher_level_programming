#!/usr/bin/python3
"""Empty class that defines a rectangle."""


class Rectangle:
    """Classe qui définit un rectangle par sa largeur et sa hauteur."""
    pass

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle avec validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle avec validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width and self.height == 0:
            return 0
