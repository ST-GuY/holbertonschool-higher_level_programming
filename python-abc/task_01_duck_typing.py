#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def aera(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def aera(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def aera(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(Shape):
    print(f"Aera: {Shape.aera()}")
    print(f"Perimeter: {Shape.perimeter()}")
