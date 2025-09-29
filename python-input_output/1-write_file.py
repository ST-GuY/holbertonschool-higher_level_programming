#!/usr/bin/python3
def write_file(filename="", text=""):
    """Écrit une chaîne de caractères dans un fichier UTF-8
    et retourne le nombre de caractères écrits"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
