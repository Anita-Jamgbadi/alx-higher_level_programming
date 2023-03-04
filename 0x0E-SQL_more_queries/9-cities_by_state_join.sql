-- lists all cities contained in the DB
-- format city.id -- city.name -- state.name, in ascending order by city.id

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
