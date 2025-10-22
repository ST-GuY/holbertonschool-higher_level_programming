-- crée la base de données si elle n'existe pas
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
-- crée l'utilisateur si nécessaire (MySQL 5.7.6+ / 8.0+ supporte IF NOT EXISTS)
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- donne uniquement le privilège SELECT sur toutes les tables de la base hbtn_0d_2
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
-- applique immédiatement les changements (optionnel si MySQL gère automatiquement)
FLUSH PRIVILEGES;
