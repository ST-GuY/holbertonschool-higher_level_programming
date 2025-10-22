-- Crée la base de données si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Utilise la base de données
USE hbtn_0d_usa;
-- Crée la table states si elle n'existe pas
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT UNIQUE,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
