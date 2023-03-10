# Write your MySQL query statement below

select employee_id from employees where employee_id not in (select employee_id from salaries)

UNION

select employee_id from salaries where employee_id not in (select employee_id from employees)

ORDER BY employee_id asc