#!/usr/bin/python3
class Rectangle:
    """verifie si ce sont des entier positif"""


def __init__(self, width, height):
    self.integer_validator("width", width)
    self.integer_validator("height", height)
    self.__width = width
    self.__height = height


def area(self):
    """return l'air d'un rectangle"""
    return self.__width * self.__height


def 