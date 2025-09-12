#!/usr/bin/python3
"""
Module contenant la fonction say_my_name qui affiche
le prénom et le nom d'une personne.
"""


def say_my_name(first_name, last_name=""):
    """
    Affiche 'My name is <first_name> <last_name>'.

    first_name et last_name doivent être des chaînes de caractères.
    Lève TypeError si l'un des paramètres n'est pas une chaîne.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
