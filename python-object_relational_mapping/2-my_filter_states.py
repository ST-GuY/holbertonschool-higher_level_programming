#!/usr/bin/python3
"""Affiche toutes les lignes de la table states dont le name correspond à l'argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments (pas de validation requise)
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    # Construire la requête avec format() avant d'exécuter
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Récupération et affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
