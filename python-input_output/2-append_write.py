#!/usr/bin/python3
"""Module 2-append_write: contient la fonction append_write
qui ajoute une chaîne de caractères à la fin d'un fichier UTF-8
et retourne le nombre de caractères écrits."""


def append_write(filename="", text=""):
    """Ajoute une chaîne de caractères à la fin d'un fichier UTF-8
    et retourne le nombre de caractères écrits.

    Si le fichier n'existe pas, il est créé.
    Le contenu existant n'est pas écrasé.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
