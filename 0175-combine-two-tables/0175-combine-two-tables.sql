# Write your MySQL query statement below
SELECT p.firstName, p.LastName, city, state
FROM Person p LEFT JOIN Address a ON p.personId = a.personId
ORDER BY p.firstName ASC

