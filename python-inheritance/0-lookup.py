#!/usr/bin/python3
"""Ce module fournit la fonction lookup qui retourne la liste
des attributs et méthodes disponibles d'un objet.
"""


def lookup(obj):
    """Retourne la liste des attributs et méthodes disponibles d'un objet."""
    return dir(obj)
