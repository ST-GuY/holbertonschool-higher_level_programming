#!/usr/bin/python3
""" Vérifie si l'objet est une instance d'une classe qui hérite (directement
ou indirectement) de 'a_class', mais pas de 'a_class' elle-même.
"""


def inherits_from(obj, a_class):
    """
    True si 'obj' est une instance d'une sous-classe de 'a_class', False sinon.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
