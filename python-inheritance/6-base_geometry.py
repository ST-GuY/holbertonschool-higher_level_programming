#!/usr/bin/python3
"""
Module: 6-base_geometry

Ce module définit la classe BaseGeometry avec une méthode publique 'area'.
La méthode 'area' n'est pas implémentée et doit être surchargée dans les
classes dérivées. Si elle est appelée directement, elle lève une exception.
"""


class BaseGeometry:
    """
    Classe de base pour les objets géométriques.

    Méthodes:
    - area(self): lève une exception indiquant que la méthode
    n'est pas implémentée.
    """

    def area(self):
        raise Exception("area() is not implemented")
