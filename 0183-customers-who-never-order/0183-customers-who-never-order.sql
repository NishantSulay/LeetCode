select c.name as 'Customers' 
from Customers c 
left join Orders o 
on c.id = o.customerId
where customerId is NULL