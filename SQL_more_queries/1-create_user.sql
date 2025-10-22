-- Crée l'utilisateur si il n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' BY 'user_0d_1_pwd';
-- Met à jour le mot de passe au cas où l'utilisateur existait déjà
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Donne tous les privilèges sur toutes les bases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;