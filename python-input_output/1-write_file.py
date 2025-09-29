#!/usr/bin/python3
"""Module 1-write_file: contient la fonction write_file
qui écrit une chaîne dans un fichier UTF-8 et
retourne le nombre de caractères écrits."""


def write_file(filename="", text=""):
    """Écrit une chaîne de caractères dans un fichier UTF-8
    et retourne le nombre de caractères écrits"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
