#!/usr/bin/env python3
"""
Exemple complet d’API Flask sécurisée
Fonctionnalités :
- Authentification basique (Basic Auth)
- Authentification par jeton (JWT)
- Contrôle d’accès par rôle (Role-based Access Control)
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

# Création de l’application Flask
app = Flask(__name__)

# Clé secrète utilisée pour signer les JWT (à garder confidentielle)
app.config["JWT_SECRET_KEY"] = "super_secret_key_123"

# Initialisation du gestionnaire JWT
jwt = JWTManager(app)

# Initialisation du système d’authentification basique
auth = HTTPBasicAuth()

# ---------------------------------------------------------------------
# Dictionnaire contenant les utilisateurs (stockés en mémoire)
# ---------------------------------------------------------------------
# On utilise "generate_password_hash" pour ne jamais stocker de mots de passe en clair
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ---------------------------------------------------------------------
# AUTHENTIFICATION BASIQUE (Basic Auth)
# ---------------------------------------------------------------------

@auth.verify_password
def verify_password(username, password):
    """
    Vérifie le nom d’utilisateur et le mot de passe fournis.
    Si les identifiants sont valides, renvoie le nom d’utilisateur.
    Sinon, renvoie None (ce qui provoque une erreur 401).
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    Route protégée par authentification basique.
    Accessible uniquement si l’utilisateur fournit de bons identifiants.
    """
    return jsonify(message="Basic Auth: Access Granted"), 200


# ---------------------------------------------------------------------
# AUTHENTIFICATION PAR JETON (JWT)
# ---------------------------------------------------------------------

@app.route("/login", methods=["POST"])
def login():
    """
    Route permettant de se connecter.
    Si les identifiants sont corrects, on renvoie un jeton JWT.
    """
    data = request.get_json()

    # Vérifie que le corps de la requête contient un nom d’utilisateur et un mot de passe
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Nom d’utilisateur ou mot de passe manquant"}), 401

    username = data.get("username")
    password = data.get("password")

    # Récupère l’utilisateur dans notre dictionnaire
    user = users.get(username)

    # Vérifie si l’utilisateur existe et si le mot de passe est correct
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Identifiants invalides"}), 401

    # Crée un jeton JWT contenant les informations de l’utilisateur (nom + rôle)
    access_token = create_access_token(identity={"username": username, "role": user["role"]})

    # Renvoie le jeton d’accès au client
    return jsonify(access_token=access_token), 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    Route protégée par un jeton JWT.
    Accessible uniquement si le client fournit un token valide.
    """
    return jsonify(message="JWT Auth: Access Granted"), 200


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Route accessible uniquement aux utilisateurs ayant le rôle 'admin'.
    Si le rôle de l’utilisateur n’est pas 'admin', on renvoie une erreur 403.
    """
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Accès administrateur requis"}), 403
    return jsonify(message="Admin Access: Granted"), 200


# ---------------------------------------------------------------------
# GESTION DES ERREURS JWT (toutes doivent renvoyer 401)
# ---------------------------------------------------------------------

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Gère le cas où aucun token n’est fourni dans la requête.
    """
    return jsonify({"error": "Jeton manquant ou invalide"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Gère le cas où le token JWT est invalide (mauvais format, altéré, etc.).
    """
    return jsonify({"error": "Jeton invalide"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """
    Gère le cas où le token JWT a expiré.
    """
    return jsonify({"error": "Jeton expiré"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """
    Gère le cas où le token a été révoqué (retiré par le serveur).
    """
    return jsonify({"error": "Jeton révoqué"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """
    Gère le cas où un token "frais" est nécessaire pour certaines actions sensibles.
    """
    return jsonify({"error": "Jeton récent requis"}), 401


# ---------------------------------------------------------------------
# Lancement du serveur Flask
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # Le serveur écoute sur toutes les interfaces, port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
