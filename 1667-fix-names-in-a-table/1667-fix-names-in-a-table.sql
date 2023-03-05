# Write your MySQL query statement below

SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
From Users
ORDER BY user_id
