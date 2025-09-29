#!/usr/bin/python3
"""Ce module contient une fonction pour
convertir une chaîne JSON en objet Python."""
import json


def from_json_string(my_str):
    """Convertit une chaîne JSON en un objet Python."""
    return json.loads(my_str)
