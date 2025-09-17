#!/usr/bin/python3
"""Empty class that defines a rectangle."""


class Rectangle:
    """Classe qui définit un rectangle par sa largeur et sa hauteur."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialisation du rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Retourne l’aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Retourne le périmètre du rectangle.
        Si width ou height vaut 0, retourne 0.
        """
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une chaîne représentant le rectangle avec #."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))
# Construit le rectangle : répète '#' sur la largeur
# pour chaque ligne de la hauteur,
# puis assemble toutes les lignes en les séparant par des retours à la ligne

    def __repr__(self):
        """
        Retourne une représentation officielle du rectangle
        permettant de recréer l'objet avec eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Affiche un message quand un objet Rectangle est supprimé."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
