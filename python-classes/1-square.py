#!/usr/bin/python3
class Square:
    """Classe qui définit un carré avec un attribut privé size."""

    def __init__(self, size):
        """Initialise un carré avec une taille donnée.
        Aucun contrôle de type ou de valeur n’est effectué.
        """
        self.__size = size
