#!/usr/bin/python3

import sys


if __name__ == "__main__":

    arguments = sys.argv[1:]
    # Récupère tous les arguments sauf le nom du script
    entier = [int(arg) for arg in arguments]  # Conversion en entier
    total = sum(entier)
    print(total)
