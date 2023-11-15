-- cities_of_california_subquery.
-- Script SQL that lists all the cities of California that can be found data base
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = "California"
);

