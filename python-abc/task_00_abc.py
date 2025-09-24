#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Animal(ABC):  # Définition de la classe abstraite Animal
    @abstractmethod
    def sound(self):
        """Méthode abstraite que les sous-classes doivent implémenter."""
        pass


class Dog(Animal):  # Création de la sous-classe Dog
    def sound(self):
        return "Bark"


class Cat(Animal):  # Création de la sous-classe Cat
    def sound(self):
        return "Meow"


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

print(dog.sound())
print(cat.sound())
