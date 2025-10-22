-- Crée une base de donnée si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Utiliser la base de donnée
USE hbtn_0d_usa;
-- Crée une table cities
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT UNIQUE,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);