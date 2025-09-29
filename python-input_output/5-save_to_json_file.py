#!/usr/bin/python3
"""Ce module contient une fonction pour écrire un objet
Python dans un fichier au format JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """Écrit un objet Python dans un fichier en utilisant le format JSON.
    """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
