#!/usr/bin/python3
"""
Module 8-rectangle
Defines a Rectangle class that inherits from BaseGeometry.
"""


class Rectangle:
    """Rectangle class that inherits from BaseGeometry."""


def __init__(self, width, height):
    self.integer_validator("width", width)
    self.integer_validator("height", height)
    self.__width = width
    self.__height = height
