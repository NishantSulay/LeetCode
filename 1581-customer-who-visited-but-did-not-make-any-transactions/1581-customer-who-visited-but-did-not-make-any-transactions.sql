# Write your MySQL query statement below

SELECT v.customer_id, count(v.visit_id) AS count_no_trans
FROM Visits v 
LEFT JOIN Transactions t 
ON v.visit_id = t.visit_id
WHERE transaction_id is NULL
GROUP BY customer_id
