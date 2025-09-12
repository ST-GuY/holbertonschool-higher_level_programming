#!/usr/bin/python3
"""
Module contenant la fonction add_integer qui additionne deux nombres.
"""


def add_integer(a, b=98):
    """
    Additionne deux nombres a et b.

    a et b doivent être des entiers ou des flottants.
    Les flottants sont convertis en entiers avant l'addition.
    b a une valeur par défaut de 98.
    
    Retour:
        int: la somme de a et b
    """
    # Vérification des types
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    # Gestion des infinis
    if a == float('inf') or a == float('-inf') or b == float('inf') or b == float('-inf'):
        raise OverflowError("Cannot add infinity")

    return int(a) + int(b)
