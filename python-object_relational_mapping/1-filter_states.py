#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    # Création d’un curseur pour exécuter les requêtes
    cur = db.cursor()
    # Exécution de la requête SQL
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    # Récupération et affichage de tous les résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
