-- Compter le nombre d'enregistrements par score
SELECT score, COUNT(*) AS count
FROM second_table
GROUP BY score
ORDER BY count DESC;
