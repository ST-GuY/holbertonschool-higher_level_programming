-- Lists all cities in hbtn_0d_usa with the format:
SELECT CONCAT(cities.id, ' - ', cities.name, ' - ', states.name) AS city_info
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;