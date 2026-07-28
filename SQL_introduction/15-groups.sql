-- Lists the number of records for each score, most frequent first
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score ORDER BY number DESC;
