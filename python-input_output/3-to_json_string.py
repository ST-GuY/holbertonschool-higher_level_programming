#!/usr/bin/python3
"""Module 3-to_json_string: contient la fonction to_json_string
qui retourne la représentation JSON d'un objet."""

import json


def to_json_string(my_obj):
    """Retourne la représentation JSON (sous forme de chaîne)
    d'un objet Python."""
    return json.dumps(my_obj)
