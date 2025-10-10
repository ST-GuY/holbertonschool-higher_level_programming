#!/usr/bin/env python3
"""
Simple Flask API exercise
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire qui stockera les utilisateurs en mémoire
users = {}


@app.route('/')
def home():
    """Endpoint racine : affiche un message de bienvenue"""
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """Endpoint /status : indique que l'API fonctionne"""
    return "OK"


@app.route('/data')
def get_data():
    """Endpoint /data : renvoie la liste des noms d'utilisateurs"""
    return jsonify(list(users.keys()))


@app.route('/users/<username>')
def get_user(username):
    """Endpoint /users/<username> : renvoie les infos d'un utilisateur"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint /add_user :
    - Accepte une requête POST avec des données JSON
    - Ajoute un nouvel utilisateur dans le dictionnaire
    """
    data = request.get_json()

    # Vérifier si les données contiennent un "username"
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data  # Stocker l'utilisateur

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == '__main__':
    # Lancer le serveur Flask sur le port 5000
    app.run(host='0.0.0.0', port=5000)
