#!/usr/bin/python3
"""Module 0-read_file: contient la fonction read_file
qui lit un fichier UTF-8 et affiche son contenu."""


def read_file(filename=""):
    """Lit un fichier UTF-8 et affiche son contenu"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
