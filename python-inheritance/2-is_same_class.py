#!/usr/bin/python3
"""
Module 2-is_same_class

Ce module contient une fonction qui vérifie si un objet est exactement
une instance d'une classe donnée, sans tenir compte des sous-classes.
"""


def is_same_class(obj, a_class):
    """
    Retourne True si obj est exactement une instance de a_class, sinon False.
    """
    return type(obj) is a_class
