#!/usr/bin/python3
"""
Définit la classe Student avec des attributs publics et une méthode to_json().
"""


class Student:
    """
    Classe qui définit un étudiant avec son prénom, son nom et son âge.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise un nouvel étudiant.

        Args:
            first_name (str): Le prénom de l'étudiant.
            last_name (str): Le nom de famille de l'étudiant.
            age (int): L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne une représentation dictionnaire (JSON) de l'objet Student.

        Si `attrs` est une liste de chaînes de caractères, seule la liste des
        attributs dont le nom est présent dans cette liste sera retournée.

        Sinon, tous les attributs de l'objet seront retournés.

        Args:
            attrs (list, optionnel): Liste de noms d'attributs à inclure.
                                     Si None, tous les attributs sont inclus.

        Returns:
            dict: Dictionnaire contenant les paires clé/valeur de l'étudiant.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
