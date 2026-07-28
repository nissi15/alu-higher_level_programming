-- Lists records that have a name, ordered by descending score
SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
