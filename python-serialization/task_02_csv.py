#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en fichier JSON.
    Lit le CSV et écrit le JSON dans 'data.json'.
    Retourne True si la conversion est réussie, sinon False.
    """
    try:
        # Lire le contenu du fichier CSV
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
            # chaque ligne devient un dictionnaire

        # Écrire le contenu dans un fichier JSON
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
