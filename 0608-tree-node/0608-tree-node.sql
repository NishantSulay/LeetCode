# Write your MySQL query statement below

SELECT id, 'Root' AS type FROM Tree
WHERE p_id IS NULL 

UNION

SELECT id, 'Inner' AS type FROM Tree 
WHERE p_id IS NOT NULL AND id IN (SELECT DISTINCT p_id FROM Tree WHERE p_id is NOT NULL)

UNION

SELECT id, 'Leaf' AS type from Tree
WHERE p_id IS NOT NULL and id NOT IN (SELECT DISTINCT p_id FROM Tree WHERE p_id is NOT NULL)
