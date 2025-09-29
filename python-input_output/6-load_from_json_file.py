#!/usr/bin/python3
"""Ce module contient une fonction pour lire un fichier JSON et
le convertir en objet Python."""
import json


def load_from_json_file(filename):
    """Lit un fichier JSON et retourne l'objet Python correspondant."""
    with open(filename, 'r') as f:
        return json.load(f)
