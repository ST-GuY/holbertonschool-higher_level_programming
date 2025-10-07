#!/usr/bin/python3
"""
Description: Récupère les posts depuis JSONPlaceholder en utilisant requests,
les affiche et les enregistre dans un fichier CSV.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Récupère les publications depuis JSONPlaceholder et affiche le code d'état
    et les titres de toutes les publications.
    """
    # URL de l'API pour récupérer tous les posts
    url = "https://jsonplaceholder.typicode.com/posts"
    # Envoi d'une requête GET à l'API
    response = requests.get(url)

    # Affichage du code de statut HTTP (200 = succès)
    print(f"Status Code: {response.status_code}")

    # Si la requête a réussi (code 200)
    if response.status_code == 200:
        # Conversion de la réponse JSON en liste de dictionnaires Python
        posts = response.json()
        # Parcours de chaque post et affichage du titre
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """
    Récupère les publications de JSONPlaceholder et les enregistre
    dans un fichier CSV
    avec les colonnes suivantes : id, titre, corps.
    """
    # URL de l'API pour récupérer tous les posts
    url = "https://jsonplaceholder.typicode.com/posts"
    # Envoi d'une requête GET à l'API
    response = requests.get(url)
    # Si la requête a réussi (code 200)
    if response.status_code == 200:
        # Conversion de la réponse JSON en liste de dictionnaires Python
        posts = response.json()

        # Préparation des données : on ne garde que id, title et body
        # pour chaque post, et on crée une nouvelle liste de dictionnaires
        data = [{"id": post["id"],
                "title": post["title"], "body": post["body"]}
                for post in posts]

        # Ouverture du fichier CSV en mode écriture
        # 'newline=""' pour éviter les lignes vides entre les lignes du CSV
        # 'encoding="utf-8"' pour gérer les caractères spéciaux
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            # Création d'un écrivain CSV qui écrit des dictionnaires
            writer = csv.DictWriter(csvfile, fieldnames=[
                "id", "title", "body"])
            # Écriture de l'en-tête (noms des colonnes)
            writer.writeheader()
            # Écriture de toutes les lignes du CSV à partir de la liste data
            writer.writerows(data)
    else:
        print("Failed to fetch posts for saving.")
