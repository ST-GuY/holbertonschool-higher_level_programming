#!/usr/bin/env python3
"""
Script that lists all states with a given name safely (no SQL injection)
Usage: ./script.py username password database_name state_name
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Vérification du nombre d'arguments
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        # Connexion à la base MySQL
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
        cursor = db.cursor()

        # Requête sécurisée avec placeholder %s
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Affichage des résultats
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
