#!/usr/bin/python3
"""
Ce module définit la classe MyList qui hérite de list.
Il ajoute une méthode publique print_sorted qui affiche
les éléments de la liste dans l'ordre croissant sans
modifier la liste originale.
"""


class MyList(list):
    """
    Classe qui hérite de list et fournit une méthode
    pour afficher la liste triée en ordre croissant.
    """

    def print_sorted(self):
        """
        Affiche les éléments de la liste dans l'ordre croissant
        sans modifier la liste originale.
        """
        print(sorted(self))
