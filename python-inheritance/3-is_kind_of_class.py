#!/usr/bin/python3
"""Ce module contient une fonction qui permet de vérifier si un objet est
une instance d'une classe donnée ou d'une sous-classe de cette classe.
"""


def is_kind_of_class(obj, a_class):
    """Vérifie si un objet est une instance d'une classe ou d'une sous-classe.
    """
    return isinstance(obj, a_class)
