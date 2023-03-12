# Write your MySQL query statement below
   
 SELECT DISTINCT name from SalesPerson WHERE sales_id NOT IN    
    (
        SELECT sales_id from Orders WHERE com_id =
             (SELECT com_id FROM Company WHERE name = 'RED')

     )
    

