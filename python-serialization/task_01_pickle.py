#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """Initialise un objet avec un nom, un âge et un statut étudiant."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs de l’objet."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l’objet courant et l’enregistre dans un fichier.
        Si une erreur survient, rien n’est sauvegardé.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error while serializing: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet depuis un fichier.
        Retourne une instance de CustomObject, ou None en cas d’erreur.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                else:
                    return None
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, Exception):
            return None
