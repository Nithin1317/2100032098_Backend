-- Query 3
-- 3. Get the details of each order, including the customer name and email.

select c.*,o.OrderId,o.OrderDate from customers c 
inner join orders o on c.CustomerId = o.CustomerId;