#!/usr/bin/python3
class MyList(list):
    """Une sous-classe de list avec une méthode supplémentaire pour afficher la liste triée."""

    def print_sorted(self):
        """Tri et affiche la liste en place"""
        print(sorted(self))

