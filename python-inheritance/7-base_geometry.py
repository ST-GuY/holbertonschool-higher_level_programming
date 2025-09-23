#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a BaseGeometry class with area() and integer_validator().
"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")
