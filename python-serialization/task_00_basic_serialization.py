#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """Sérialise un dictionnaire Python et l’enregistre dans un fichier JSON."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """Charge un fichier JSON et le désérialise en dictionnaire Python."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
